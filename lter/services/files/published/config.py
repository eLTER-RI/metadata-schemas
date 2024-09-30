from lter.services.files.config import LterFileServiceConfig


class LterFilePublishedServiceConfig(LterFileServiceConfig):
    service_id = "published_lter_file"

    @property
    def components(self):
        return [*super().components]
