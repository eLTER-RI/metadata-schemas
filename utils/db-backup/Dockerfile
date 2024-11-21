FROM postgres:17.1-bullseye

RUN apt-get update && apt-get install jq curl bash -y

RUN curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o $HOME/minio-binaries/mc

RUN chmod +x $HOME/minio-binaries/mc
RUN export PATH=$PATH:$HOME/minio-binaries/

WORKDIR /backup
COPY backup.sh .
RUN chmod +x backup.sh

CMD ["./backup.sh"]