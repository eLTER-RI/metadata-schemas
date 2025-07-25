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

<img src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAADwAAAAyCAYAAAAA9rgCAAAACXBIWXMAAASgAAAEoAGuODdsAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABH9JREFUaIHdml1oHFUUx/9n57ppyWIsLdZobY02gVqktRbyoCgU3DbZbow+iG9KYWeTgEh9KCLayUooFQuKfZC9YwwKpUJQ0+gKpvUDQUtrrQWFioWEVkJjKUm1yabJfhwfssHQzmZ3w8mdxR8MzOy59/zv2bl75szdC2aGqQPd3U0m9bwOBbO0AThUSQet9UUA90oNICDlqEw2UU9PYyUdmDkIgKQO03cYyOUiAN4pt3kgEBjN5/O3S8mbDxiIooKAY7HYdklx01MaAB6ngwdX+aALAFBa618E/X1n2/beUpqYnd0F4Kigbkm01p8B2KAAbBX0eymVSq0C0Oll3BQKbTk/OYnGlStfSaVSDYK6xRiLRCIfFM4fBNCkAExIeWfm65FIZALAAS/77jNnHgDwyIV0esPu0dG32LYzUtqlIKJrzDxOzGxKE5RI9ALYUxjBDt6//1tj4gX8SFpzMEf9kFVa60+knDHz6Xg8/maZzaMAXpbSLoXruu8y890KwDNSTolIDQwM3KGUet7L3lRbu/mPqan5y42vHzlyoLmu7i8p/Zth5ivRaPRo4XwnCklLlPb29r+Hhobe97KNTE9vA9A8f31oeDh9rLnZs60EwWAwd/NnKhgMihUBlmVlAHA4HJ7ysmdOnswuvL6Rz+8Mh8M9UvqLoZTans1mA/5l6TlyAO5ix7lqagx+1NILsQC0AvioWAPXdV/I5/ObpQT9DhiYy9ZFA2bmp4moTUrMv+fwf+yiw4drTIlVwx0OYXz8CQBDXsZcLrfXsqyElFg1BAzMTWvPgDs7O4clhVQymeyQchYIBEZisdhXS+jaBuBFqXF44bruc8xcp4joPSmnzDzY39//fU1NzWNe9vpg8J7Ls7NepvWxvj47unr1iNRYAEAp9U9ra+upwtgSWI5KKxQK5bPZ7DUvWwaYKdbv1MTEurY1ayQXI5DJZG4pgBSAZ6UEiGi0paVlBsBPXvarZ88WLTB+Taf7otGo6B1eCDO/BCDkd6U1z2/sOA+ZGEO1ZOnBYgbXdbcy851SQtUS8OfFDIVk87+qtK4AOG1KrBrucIodJ1/MyMwfAvhRSsz/gImKTmcAiMfjn0rKqd7e3o1SzmZmZia7urrGKumCFStOSOkvhtZ6PYDbVC6XuyDlVCk1COCpCrp8w/v2XZfSL8FxAE3+Jq0S03k5UAC0oL9zFbW2rC8FtReFmT8morV+Vlrn2HEeNiZeQCUSCbFp7TgOAyj3GyxaXS0TBACqvr7+lrXbpaK1HrRtu9ykZfT3q7X+HT4mrcvo7v7ZD2EFQOw5yMzlJq1BNpk85viBiC4q27afNCzsy+PItu09gD8vD9NgNv6/8DxKay22ysDMx+PxuF2i2RA7TlpKs1ySyeTXRNSgANwn5ZSI1pba49FYW3splUq9KqVZDul0+m0iWgegQQGQXEcaK7HH4/7zk5OvHevoqOQFQwSt9Z8AlNGNnUgk4n5vLjWbtCzrC6N6HhitpZeC1voNZn5Uyp//Kx6l2UJEO6ScVcMinlH+BWJF4Hnxt/m4AAAAAElFTkSuQmCC" alt="to monolith" />


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

