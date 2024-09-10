ARG OAREPO_DEVELOPMENT_IMAGE=oarepo/oarepo-base-development:12
ARG OAREPO_PRODUCTION_IMAGE=oarepo/oarepo-base-production:12
ARG BUILDPLATFORM=linux/amd64
ARG DEPLOYMENT_VERSION=0.0.1

FROM --platform=$BUILDPLATFORM $OAREPO_DEVELOPMENT_IMAGE as production-build

COPY .. /repository

# build the repository
WORKDIR /repository
RUN rm -rf .nrp .pdm-build .venv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN PYTHON=`which python3` ./nrp build --override-config venv_dir=/invenio/venv --override-config invenio_instance_path=/invenio/instance

# cleanup
RUN rm -rf .nrp .pdm-build .venv
RUN find . -name "__pycache__" -type d -exec rm -rf {} +


FROM --platform=$BUILDPLATFORM ${OAREPO_PRODUCTION_IMAGE} as production

ARG REPOSITORY_SITE_ORGANIZATION="LTER"
ARG REPOSITORY_SITE_NAME="DAR"
ARG REPOSITORY_IMAGE_URL="http://localhost/bla"
ARG REPOSITORY_AUTHOR="Dominik"
ARG REPOSITORY_GITHUB_URL="github"
ARG REPOSITORY_URL="https://catalog.elter-ri.eu/"
ARG REPOSITORY_DOCUMENTATION="ToDo"
ARG DEPLOYMENT_VERSION="0.0.5"

LABEL maintainer="${REPOSITORY_SITE_ORGANIZATION}" \
    org.opencontainers.image.authors="${REPOSITORY_AUTHOR}" \
    org.opencontainers.image.title="LTER DAR production image" \
    org.opencontainers.image.url="${REPOSITORY_IMAGE_URL}" \
    org.opencontainers.image.source="${REPOSITORY_GITHUB_URL}" \
    org.opencontainers.image.documentation="${REPOSITORY_DOCUMENTATION}"

ENV DEPLOYMENT_VERSION=${DEPLOYMENT_VERSION}

# copy build from production build - just the final directories, not the whole build

COPY --from=production-build /invenio /invenio
COPY --from=production-build /repository /repository

# copy uwsgi.ini - keep the path the same as in invenio
RUN mkdir -p /opt/invenio/src/uwsgi/

# TODO(mesemus): consider if this is really needed by production profile
# in reality, this would be overriden by the uwsgi.ini k8s config map
#
#COPY ./docker/development.crt /development.crt
#COPY ./docker/development.key /development.key
#
#COPY ./docker/production/uwsgi.ini /opt/invenio/src/uwsgi/uwsgi.ini

ENV PATH=/invenio/venv/bin:${PATH}

RUN /invenio/venv/bin/pip install --no-cache-dir uwsgi uwsgi-tools

RUN ( echo "Contents of /repository"; ls -lR /repository )
RUN ( echo "Contents of /invenio"; ls -lR /invenio )

ENTRYPOINT [ "sh", "-c" ]