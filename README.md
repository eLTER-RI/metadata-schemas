# eLTER Metadata schemas

## Description
This repository contains the eLTER metadata schemas for the eLTER network. The schemas are used to describe datasets, data products, and other related information.

## Info
Files suffixed with `_monolith` contain all `$ref`erenced subschemas inline.

## Viewer

A human readable representation of the schema is available using the Atlassian Json-Schema-Viewer App using the following link:

[https://json-schema.app/view/%23/%23%2Fproperties%2Fmetadata?url=https%3A%2F%2Fraw.githubusercontent.com%2FeLTER-RI%2Fmetadata-schemas%2Frefs%2Fheads%2Fmain%2FeLTERMetadataSchemaDatasets_monolith.json](https://json-schema.app/view/%23/%23%2Fproperties%2Fmetadata?url=https%3A%2F%2Fraw.githubusercontent.com%2FeLTER-RI%2Fmetadata-schemas%2Frefs%2Fheads%2Fmain%2FeLTERMetadataSchemaDatasets_monolith.json)

## Converting between monoliths and subschemas
### Bake a monolith

Monoliths (*dereferenced* main schemas with inlined subschema content rather than mere `$ref`erences) are created whenever an update is 
pushed as or to a) `/subschemas`, b) `eLTERMetadataSchemaDatasets.json` or c) `eLTERMetadataSchemaExternalDatasets.json`

These artifacts can be retrieved like so:
1. go to [Actions](https://github.com/eLTER-RI/metadata-schemas/actions) (top menu)
2. go to workflow [`make monolith`](https://github.com/eLTER-RI/metadata-schemas/actions/workflows/make-monolith.yml) (left sidebar)
3. in the main panel, select "Run workflow" from the "Run workflow" dropdown on the right (branch: main)
4. wait a couple of seconds until the workflow starts, and another 10-15 s until done
5. click the workflow title
6. scroll down to the "artifacts" card and download desired monolith(s) as zip-archive

The names of the main schemas getting dereferenced are hardcoded in `make-monolith.js` (which does the work) and [`make-monolith.yml`](https://github.com/eLTER-RI/metadata-schemas/blob/main/.github/workflows/make-monolith.yml) which configures the automated workflow.

ℹ️ This action *does not automatically update the repository*. If desired, download the output (click the action's title, scroll down and download the output from the "artifacts" card) and commit. 

### Extract subschemas from monolith(s)
If, conversely, you want to extract subschemas from an updated monolith, trigger the workflow [`create subschemas from monolith`](https://github.com/eLTER-RI/metadata-schemas/actions/workflows/subschemas-from-monolith.yml). Remember to download the artifacts and commit them to update the repo (see above).

