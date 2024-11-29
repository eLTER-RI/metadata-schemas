import requests

from flask import Blueprint, current_app
from flask_cors import CORS
from flask_login import login_required

api = Blueprint('ingest_api', __name__)

CORS(api, resources={r"/api/infra/*": {"origins":
    [
        "https://localhost",
        "https://127.0.0.1",
        "https://catalog.elter-ri.eu/",
        "https://catalog.elter.cerit-sc.cz/"
    ]
}})

def get_workflows_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {current_app.config["WORKFLOWS_API_KEY"]}'
    }

workflows_api = '/infra/qc'

@api.route('%s/status/<id>' % workflows_api)
@login_required
def get_workflows_status(id):
    api_hostname = current_app.config["WORKFLOWS_API_HOSTNAME"]
    url = f'{api_hostname}/api/v1/workflows/executions/{id}/status'
    response = requests.get(url, headers=get_workflows_headers())

    if response.ok:
        return response.json(), response.status_code

    return response.text, response.status_code



@api.route('%s/report/<id>' % workflows_api)
@login_required
def get_workflows_report(id):
    api_hostname = current_app.config["WORKFLOWS_API_HOSTNAME"]
    url = f'{api_hostname}/api/v1/workflows/executions/{id}/report'
    response = requests.get(url, headers=get_workflows_headers())
    if response.ok:
        return response.json(), response.status_code

    return response.text, response.status_code
