import json
import requests

from flask import Blueprint, Response, current_app, request

api = Blueprint('ingest_api', __name__)


def get_ingest_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': current_app.config["INGEST_API_KEY"]
    }


def get_workflows_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': current_app.config["WORKFLOWS_API_KEY"]
    }


batch_ingest_service = 'batch-ingest-api'
batch_ingest_namespace = 'data-ingest'

api_suffix = '.svc.cluster.local'

batch_api = '/v1/ingest/batch'


@api.route('%s/temp-data-upload/credentials' % batch_api, methods=['GET'])
def get_credentials():
    metadata_name = request.args.get('metadataFileName')
    file_names = request.args.getlist('fileNames')

    api_hostname = current_app.config["INGEST_API_HOSTNAME"]
    url = f'{api_hostname}/api{batch_api}/temp-data-upload/credentials'

    params = {
        'metadataFileName': metadata_name,
        'fileNames': ','.join(file_names)
    }

    response = requests.get(url, headers=get_ingest_headers(), params=params)

    return response.json()


@api.route(f'{batch_api}/temp-bucket-data-source/<string:workflow_id>', methods=['POST'])
def run_ingest(workflow_id):
    data = request.json
    api_hostname = current_app.config["INGEST_API_HOSTNAME"]
    url = f'{api_hostname}/api{batch_api}/temp-bucket-data-source/{workflow_id}'

    try:
        response = requests.post(url, headers=get_ingest_headers(), json=data)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.RequestException as e:
        current_app.logger.error(f"Error while making request: {str(e)}")
        return {"error": "Failed to make POST request"}, 500


workflows_api = '/v1/workflows'


@api.route('%s/status/<int:id>' % workflows_api)
def get_workflows_status(id):
    api_hostname = current_app.config["WORKFLOWS_API_HOSTNAME"]
    url = f'{api_hostname}/api{workflows_api}/status/{id}'
    return requests.get(url, headers=get_workflows_headers())


@api.route('%s/status' % workflows_api)
def get_workflows_status_overview():
    limit = request.args.get('limit')
    api_hostname = current_app.config["WORKFLOWS_API_HOSTNAME"]
    url = f'{api_hostname}/api{workflows_api}/status'
    params = {'Limit': limit}
    return requests.get(url, headers=get_workflows_headers(), params=params)


@api.route('%s/report/{id}' % workflows_api)
def get_workflows_report(id):
    api_hostname = current_app.config["WORKFLOWS_API_HOSTNAME"]
    url = f'{api_hostname}/api{workflows_api}/report/{id}'
    return requests.get(url, headers=get_workflows_headers())
