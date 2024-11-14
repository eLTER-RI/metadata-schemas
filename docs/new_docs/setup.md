[Back to Menu](main.md)

# Setup
## Prerequisites

- Ideally any Linux distribution or MacOS. Can run on WSL,
however it is not supported and issues like not working hot-reload can occur
- Docker engine
- Node v21
- Python 3.12
- Python uv
- sudo apt install imagemagick

## Debug configuration
- Create following configuration:
  - Executing script = debug_repository.py (in the root repo)
  - Script params = run --cert ./docker/development.crt --key ./docker/development.key
  - Working dir = elter_dar root dir
  - ENV vars = PYTHONUNBUFFERED=1;FLASK_DEBUG=1 - you
can define any Env vars you need
  - Python 3.12

[Back to Menu](main.md)