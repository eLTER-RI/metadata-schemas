from invenio_drafts_resources.services.records.components.base import ServiceComponent

# TODO this is only a template for future work
# This component has to be added to lter/services/records/config.py to extend
# each API call - create/update/delete/...
class LterComponent(ServiceComponent):

    def update_draft(self, identity, data=None, record=None, **kwargs):
        if record and record.state in ['validated', 'error']:
            record.state = 'draft'
