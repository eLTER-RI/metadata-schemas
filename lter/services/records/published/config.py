from oarepo_published_service.services.config import PublishedServiceConfig
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin


class LterPublishedServiceConfig(PublishedServiceConfig, PermissionsPresetsConfigMixin):
    service_id = "published_lter"

    @property
    def components(self):
        return [*super().components]
