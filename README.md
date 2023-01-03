# Flask example

Using Flask to build a Restful API Server.


## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
|──────meters-api/
| |────template/base.html
| |────template/index.html
|──────app.py
|──────init_db.py
|──────schema.sql
|──────db.sqlite3
```


## Flask Configuration

#### Example

```
app = Flask(__name__) 
```

#### Builtin Configuration Values

SERVER_NAME: the name and port number of the server. 

JSON_SORT_KEYS : By default Flask will serialize JSON objects in a way that the keys are ordered.

- [reference¶](http://flask.pocoo.org/docs/0.12/config/)


## Run Flask
### Run flask for develop
```
$ python meters-api/init_db.py   #for adding default data in sqlight file
$ python meters-api/app.py
```
In flask, Default port is `8000`

Web page:  `http://127.0.0.1:8000/meters/`

## Reference

Offical Website

- [Flask](http://flask.pocoo.org/)
- [Flask Extension](http://flask.pocoo.org/extensions/)


## Changelog

- Version 0.1 : add master api