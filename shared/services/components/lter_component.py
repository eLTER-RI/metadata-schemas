from invenio_records_resources.services.records.components.base import ServiceComponent

# TODO this is only a template for future work
# This component has to be added to lter/services/records/config.py to extend
# each API call - create/update/delete/...
class LterComponent(ServiceComponent):
    def create(self, identity, **kwargs):
        pass