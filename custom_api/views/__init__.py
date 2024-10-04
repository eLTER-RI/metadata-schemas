import json
import requests

from flask import Blueprint, Response, current_app

api = Blueprint('ingest_api', __name__)

def get_ingest_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': current_app.config["INGEST_API_KEY"]
    }

def get_workflows_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {current_app.config["WORKFLOWS_API_KEY"]}'
    }

batch_ingest_service = 'batch-ingest-api'
batch_ingest_namespace = 'data-ingest'

api_suffix = '.svc.cluster.local'

batch_api = '/v1/ingest/batch'


@api.route('%s/temp-data-upload/credentials' % batch_api)
def get_credentials():
    api_hostname = current_app.config["INGEST_API_HOSTNAME"]
    url = f'{api_hostname}/api{batch_api}/temp-data-upload/credentials'
    return requests.get(url, headers=get_ingest_headers()).json()

@api.route('%s/temp-bucket-data-source/<string:workflowId>' % batch_api, methods=['POST'])
def run_ingest(workflow_id):
    return Response(json.dumps({"text": "Hello World"}), mimetype='application/json')


workflows_api = '/v1/workflows'


@api.route('%s/status/<int:id>' % workflows_api)
def get_workflows_status(id):
    return Response(json.dumps({"text": "Hello World"}), mimetype='application/json')

@api.route('%s/status' % workflows_api)
def get_workflows_status_overview():
    return Response(json.dumps({"text": "Hello World"}), mimetype='application/json')

@api.route('%s/report/{id}' % workflows_api)
def get_workflows_report(id):
    return Response(json.dumps({"text": "Hello World"}), mimetype='application/json')
