## Gistified

#### Flask app where code snippets can be created with syntax highlight and language recognition.


### Dependencies

- Python 3.6.1
- PostgreSQL 9.6.5

### Setup

Run the following commands:

```
sudo apt-get update
sudo apt-get install postgres libpq-dev

pyenv install 3.6.1
pyenv virtualenv 3.6.1 gistified
```

### Development

Run the following commands:

```
pip install -r requirements.txt
/bin/bash ./config_db.sh
export FLASK_APP=run.py
FLASK_DEBUG=True flask run
```

### Tests

Tests are run with pytest and tox.

To execute either of them, run the following commands:

```
pytest
tox
```

