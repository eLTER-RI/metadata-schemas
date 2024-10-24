from invenio_records_resources.services import FileServiceConfig
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from .processors import MeasurementFileExtractionProcessor


class ELterServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    file_processors = [
        MeasurementFileExtractionProcessor(),
    ]
    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
    ]