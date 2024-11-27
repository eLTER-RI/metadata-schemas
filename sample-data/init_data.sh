#!/bin/bash

set -e

BP="$(dirname "$BASH_SOURCE[0]")/.."

source "$BP/.venv/bin/activate"

create_record() {
  local file="$1"
  local community="$2"
  local output_path="$3"
  local -n output_id="$4"
  local api_url="$5"
  api_url=${api_url:-"https://127.0.0.1:5000/api"}
  api_url="${api_url}/communities/$community/lter"

  echo "Uploading record from $file to $api_url"

  curl -k \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    --data-binary "@$file" \
    $api_url >"$output_path"

  export output_id=$(jq -r '.id' $output_path)
  if [[ "$output_id" == "null" ]]; then
    echo "Failed to upload record"
    cat $output_path | jq
    return 1
  fi
  echo "Record uploaded with id: $output_id, see $output_path for details"

  cat $output_path
}

run_external_workflow() {
  local draft_id="$1"
  local output_path="$2"
  local -n output_wf_id="$3"
  local api_url="$4"
  api_url=${api_url:-"https://127.0.0.1:5000/api"}
  api_url="${api_url}/communities/$community/lter"
  api_url=${api_url:-"https://127.0.0.1:5000/api"}
  api_url="${api_url}/lter/$draft_id/draft/requests/run_external_workflow"

  echo "Starting external workflow for draft_id: $draft_id"

  curl -k \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    $api_url >"$output_path"

  export output_wf_id=$(jq -r '.id' "$output_path")
}

external_wf_action() {
  local wf_id="$1"
  local action="$2"
  local api_url="$3"

  api_submit_url=${api_url:-"https://127.0.0.1:5000/api"}
  api_submit_url="${api_url}/requests/$wf_id/actions/$action"

  curl -k \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    $api_submit_url
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  export TOKEN="H2uYI83bmadSDK00pLQZ1Nuo6bTjoHAWCaOvgio4IK992uudSWj4MRzsCwwW"

  create_record 001.json elter /tmp/rec.json REC_ID
  run_external_workflow "$REC_ID" /tmp/rec.json WF_ID
  external_wf_action "$WF_ID" "submit"

#  run_external_workflow "$REC_ID" ../tmp/rec.json WF_ID
#  external_wf_action "$WF_ID" "submit"
fi
