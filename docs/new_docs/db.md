[Back to Menu](main.md)
# Commands for database init

- [Dev](#dev)
- [General commands](#general-commands)
  - [Create user](#create-user)
  - [Create user token](#create-user-token)
  - [Set default location](#set-default-location-1)
  - [Create community](#create-community)
  - [Add user to community](#add-user-to-community)
- [Chris's deployment](#chris-deployment)
- [Catalog prod](#catalog-prod)
- [Reindex](#reindex)


## Dev
``` bash
invenio users create -a -c admin@elter.com --password testtest $$ invenio users create -a -c admin@elter.com --password testtest && invenio oarepo communities create elter ELTER && invenio oarepo communities members add elter admin@elter.com "owner" && invenio tokens create -n admin_token -u admin@elter.com -i
```

## General commands

### Create user
```
invenio users create -a -c <user_email> --password <password>
```
### Create user token
```
invenio tokens create -n <token_name> -u <user_email> -i
```
### Set default location
```
invenio files location create default s3://<bucket_name> --default
```
### Create community
```
invenio oarepo communities create <tag> <name>
```
### Add user to community
```
invenio oarepo communities members add <community_tag> <user_email> <community_role>
```



## Chris deployment

## Catalog prod - change values of variables
### Set default location
```
invenio files location create default s3://<bucket_name> --default
```
### Create communities
```
invenio oarepo communities create b2share B2SHARE && invenio oarepo communities members add b2share admin@elter.com "owner" && invenio oarepo communities create b2share_juelich B2SHARE_Juelich && invenio oarepo communities members add b2share_juelich admin@elter.com "owner" && invenio oarepo communities create zenodo ZENODO && invenio oarepo communities members add zenodo admin@elter.com "owner" && invenio oarepo communities create elter eLTER && invenio oarepo communities members add elter admin@elter.com "owner"
```

## Reindex
```
invenio db drop --yes-i-know && invenio db init && invenio db create && invenio index destroy --yes-i-know && invenio index init && invenio index queue init purge && invenio oarepo cf init && invenio oarepo index reindex && invenio oarepo index reindex 
```

[Back to Menu](main.md)