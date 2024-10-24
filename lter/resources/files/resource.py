from oarepo_ui.resources.file_resource import S3RedirectFileResource


class LterFileResource(S3RedirectFileResource):
    """LterFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class LterFileDraftResource(S3RedirectFileResource):
    """LterFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
