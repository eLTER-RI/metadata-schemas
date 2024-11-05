from invenio_drafts_resources.services.records.components.base import ServiceComponent

# TODO this is only a template for future work
# This component has to be added to lter/services/records/config.py to extend
# each API call - create/update/delete/...
class LterComponent(ServiceComponent):

    def update_draft(self, identity, data=None, record=None, **kwargs):
        if record and record.state in ['validated', 'error']:
            record.state = 'draft'
        self.fill_external_workflow(data, record)

    def create(self, identity, data=None, record=None, **kwargs):
        self.fill_external_workflow(data, record)

    @staticmethod
    def fill_external_workflow(data, record):
        external_workflow = record.setdefault("externalWorkflow", {})
        actual_type_id = data.get('externalWorkflow', {}).get('defaultWorkflowTemplateId')
        if actual_type_id:
            external_workflow['defaultWorkflowTemplateId'] = actual_type_id
