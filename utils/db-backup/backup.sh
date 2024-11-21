#!/usr/bin/env bash
set -euo pipefail

# Set environment variables
DB_NAME=${DB_NAME}
DB_USER=${DB_USER}
DB_PASSWORD=${DB_PASSWORD}
DB_HOST=${DB_HOST}
DB_PORT=${DB_PORT}

S3_ACCESS_KEY=${S3_ACCESS_KEY}
S3_SECRET_KEY=${S3_SECRET_KEY}

S3_URL=${S3_URL}
S3_BUCKET=${S3_BUCKET}
BACKUP_FILE="backup_$(date +%Y%m%d%H%M%S).sql.gz"

# Export password to avoid password prompt
export PGPASSWORD=${DB_PASSWORD}

# Create a backup using pg_dump
pg_dump -h "${DB_HOST}" -p "${DB_PORT}" -U "${DB_USER}" -d "${DB_NAME}" -b -v | gzip > "${BACKUP_FILE}"

# Prepare s3 credentials

JSON_CREDENTIALS=$(jq -n \
  --arg access_key_id "${S3_ACCESS_KEY}" \
  --arg secret_access_key "${S3_SECRET_KEY}" \
  --arg url "${S3_URL}" \
  '{accessKey: $access_key_id, secretKey: $secret_access_key, url: $url, api: "s3v4", path: "auto"}'
);

# Configure mc
export PATH=$PATH:$HOME/minio-binaries/
echo -n "${JSON_CREDENTIALS}" | mc alias import s3

# Upload the backup to S3
mc put "${BACKUP_FILE}" "s3/${S3_BUCKET}/${BACKUP_FILE}"