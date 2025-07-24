# eLTER Metadata schemas

## Description
This repository contains the eLTER metadata schemas for the eLTER network. The schemas are used to describe datasets, data products, and other related information.

## Info
Files suffixed with `_monolith` contain all `$ref`erenced subschemas inline.

## Viewer

A human readable representation of the schema is available using the Atlassian Json-Schema-Viewer App using the following link:

[https://json-schema.app/view/%23/%23%2Fproperties%2Fmetadata?url=https%3A%2F%2Fraw.githubusercontent.com%2FeLTER-RI%2Fmetadata-schemas%2Frefs%2Fheads%2Fmain%2FeLTERMetadataSchemaDatasets_monolith.json](https://json-schema.app/view/%23/%23%2Fproperties%2Fmetadata?url=https%3A%2F%2Fraw.githubusercontent.com%2FeLTER-RI%2Fmetadata-schemas%2Frefs%2Fheads%2Fmain%2FeLTERMetadataSchemaDatasets_monolith.json)

## Get a monolith

Monoliths (*dereferenced* main schemas with inlined subschemas content rather than mere `$ref`erences) are created whenever an update is 
pushed as or to a) `/subschemas`, b) `eLTERMetadataSchemaDatasets.json` or c) `eLTERMetadataSchemaExternalDatasets.json`

These artifacts can be retrieved like so:
1. select "Actions" from the top menu
2. select workflow "make monolith" from the left sidebar
3. in the main panel, select "Run workflow" from the "Run workflow" dropdown on the right (branch: main)
4. wait a couple of seconds until the workflow starts, and another 10-15 s until done
5. click the workflow title
6. scroll down to the "artifacts" card and download desired monolith(s) as zip-archive
