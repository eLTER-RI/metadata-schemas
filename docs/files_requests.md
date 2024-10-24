# Files / requests demo

This demo shows how to create a file processor class and a custom request.

## File processor

Source code is in shared/services/files package

## Request

Source code is in shared/requests package

## Usage

### Command-line

Install the nrp-cmd commandline tool:

Clone https://github.com/nrp-cz/nrp-invenio-client,
switch to non-generic branch and build:

```bash
git clone https://github.com/nrp-cz/nrp-invenio-client
git switch non-generic
python3.12 -m venv .venv
.venv/bin/pip install -U setuptools pip wheel
.venv/bin/pip install -e .
alias nrp-cmd=$PWD/.venv/bin/nrp-cmd
```

Some documentation is at https://nrp-cz.github.io/docs/userguide/commandline

Note: to show communication, invoke the client as:

```bash
nrp-cmd --show-communication <command> <args>
```

## Register your repository

```bash
nrp-cmd add repository https://127.0.0.1:5000 --no-tls-verify elter
```

## Create record

```bash
nrp-cmd create record --repository elter --community a '{}' @rec
```

## Upload file

```bash
nrp-cmd upload file @rec /tmp/test.mf
```

## List files

```bash
nrp-cmd list files @rec
```

## Download file

```bash
nrp-cmd download file @rec test.mf -o /tmp
```

## Get record

```bash
nrp-cmd get record @rec
```

## List requests

```bash
nrp-cmd list requests @rec
```

## Create request

```bash
nrp-cmd create request run_external_workflow @rec  
```