## Gistified

#### Flask app where code snippets can be created with syntax highlight and language recognition.

- Syntax highlight is done with [Prettify](https://github.com/google/code-prettify)

- Language recognition is achieved with [Pygments](http://pygments.org/)


Right now, all code snippets are highlighted, however, this does not mean their language is recognized. With that, language recognition is limited to file extentions, this means that a code snippet will only have its language found if the file extension is right. For example, `blabla.py` will match `Python`, `blabla.rb` to `Ruby` and on.


### Dependencies

- Python 3.6.1
- PostgreSQL 9.6.5

### Setup

Run the following commands:

```
sudo apt-get update
sudo apt-get install postgresql libpq-dev

pyenv install 3.6.1
pyenv virtualenv 3.6.1 gistified
```

### Development

Run the following commands:

Setup db and install libs

```
pip install -r requirements.txt
/bin/bash ./config_db.sh
```

Apply migrations and run app

```
export FLASK_APP=run.py
flask db upgrade
FLASK_DEBUG=True flask run
```

### Tests

Tests are run with pytest and tox.

To execute either of them, run the following commands:

```
pytest
tox
```

