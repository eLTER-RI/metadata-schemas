[Back to Menu](main.md)
# Commands for database init

- [Dev](#dev)
- [General command](#general-command)
- [Chris's deployment](#chris-deployment)
- [Catalog prod](#catalog-prod)
- [Reindex](#reindex)


## Dev

## General command

## Chris deployment

## Catalog prod - change values of variables
### Set default location
```
invenio files location create default s3://<bucket_name> --default
```
### Create communities
```
invenio oarepo communities create b2share B2SHARE && invenio oarepo communities members add b2share && invenio oarepo communities create b2share_juelich B2SHARE_Juelich && invenio oarepo communities members add b2share_juelich admin@elter.com "owner" && invenio oarepo communities create zenodo ZENODO && invenio oarepo communities members add zenodo admin@elter.com "owner" && invenio oarepo communities create elter eLTER && invenio oarepo communities members add elter admin@elter.com "owner"
```

## Reindex
```
invenio db drop --yes-i-know && invenio db init && invenio db create && invenio index destroy --yes-i-know && invenio index init && invenio index queue init purge && invenio oarepo cf init && invenio oarepo index reindex && invenio oarepo index reindex 
```

[Back to Menu](main.md)