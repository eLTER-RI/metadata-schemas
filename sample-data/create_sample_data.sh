#!/bin/bash

# set -e

BP="$(dirname "$BASH_SOURCE[0]")/.."

source "$BP/.venv/bin/activate"

create_community() {
  local community_slug="$1"
  local community_title="$2"
  local community_owner_email="$3"

  invenio oarepo communities create "$community_slug" "$community_title"
  invenio oarepo communities members add "$community_slug" "$community_owner_email" "owner"
}

add_community_member() {
  local community_slug="$1"
  local member_email="$2"
  local role="$3"

  invenio oarepo communities members add "$community_slug" "$member_email" "$role"
}

create_user() {
  local email="$1"
  local password="$2"

  invenio users create -a -c "$email" --password "$password"
}

generate_token() {
  local email="$1"
  local name="$2"
  local -n varname="$3"

  varname=$(invenio tokens create -n "$name" -u "$email")
}

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

publish_record() {
  local record_id="$1"
  local api_url="$2"

  api_url=${api_url:-"https://127.0.0.1:5000/api"}
  api_url="${api_url}/lter/${record_id}/draft/requests/publish_draft"

  echo "Publishing record with id $record_id to $api_url"

  curl -k \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    --data-binary "{}" \
    $api_url | tee /tmp/publish.json

  submit_link=$(cat /tmp/publish.json | jq -r '.links.actions.submit')
  echo "Submitting request $submit_link"

  curl -k \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    --data-binary "{}" \
    $submit_link | tee /tmp/submit.json
}

upload_file() {
  local record_id="$1"
  local file="$2"
  local api_url="$3"

  api_url=${api_url:-"https://127.0.0.1:5000/api"}

  files_url="${api_url}/lter/${record_id}/draft/files"

  echo "Starting file upload $file to $api_url"
  fn=$(basename $file)

  curl -k \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    --data-binary "[{\"key\": \"$fn\"}]" \
    $files_url | tee /tmp/upload-initiate.json

    curl -k \
    -X PUT \
    -H "Content-Type: application/octet-stream" \
    -H "Authorization: Bearer $TOKEN" \
    --data-binary "@$file" \
    "${files_url}/${fn}/content" | tee /tmp/upload-content.json

    curl -k \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    --data-binary "{}" \
    "${files_url}/${fn}/commit" | tee /tmp/upload-commit.json
}

# if the file is sourced, stop here
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then

  create_user "harvester@lter.com" "testtest"
  create_user "admin@lter.com" "testtest"

  create_community "b2share" "B2SHARE" "admin@lter.com"
  create_community "zenodo" "ZENODO" "admin@lter.com"

  add_community_member "b2share" "harvester@lter.com" "submitter"
  add_community_member "zenodo" "harvester@lter.com" "submitter"

  generate_token "harvester@lter.com" upload-token HARVESTER_UPLOAD_TOKEN

  # export the token for subsequent commands
  export TOKEN=$HARVESTER_UPLOAD_TOKEN

  create_record sample-data/001.json b2share /tmp/rec.json REC_ID
  echo "Record id: $REC_ID"
  publish_record $REC_ID

  create_record sample-data/001_with_files.json b2share /tmp/rec.json REC_ID
  echo "Record id: $REC_ID"
  upload_file $REC_ID invenio.cfg
  publish_record $REC_ID

fi
