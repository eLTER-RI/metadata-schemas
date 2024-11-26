from oarepo_ui.resources.components import UIResourceComponent
from datetime import datetime
from itertools import groupby


class LterResourceCustomComponent(UIResourceComponent):
    def before_ui_detail(self, *, api_record, record, identity, args, view_args, ui_links, extra_context, **kwargs, ):
        data = record.get('externalWorkflow', {}).get('history', [])

        if data:
            sorted_data = sorted(data, key=lambda x: (x['workflowHandle'], datetime.strptime(x['date'], '%b %d, %Y, %I:%M:%S\u202f%p')), reverse=True)
            newest_data = [next(group) for _, group in groupby(sorted_data, key=lambda x: x['workflowHandle'])]
            newest_data.sort(key=lambda x: datetime.strptime(x['date'], '%b %d, %Y, %I:%M:%S\u202f%p'), reverse=True)
            extra_context['wf_latest_history'] = newest_data
            self.fill_is_admin(identity.provides, extra_context)

    def fill_is_admin(self, identity_provides, extra_context):
        role = self.get_role(identity_provides)
        extra_context['is_admin'] = role == 'admin'

    def get_role(self, provides: set):
        return next((provide.value for provide in provides if provide.method == "role"), None)
