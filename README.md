# restful_api_flask

### Actual file name
File name should be `app.py`. Here splitting 
into multiple file for ease of understanding


### Run Code
```python
python app.py
```


### Debug mode on
This Auto reload the updated code
```python
export FLASK_DEBUG=1
```

### Required libraries
```python
pip install flask
pip install flask-sqlalchemy # Database
pip install flask-marshmallow # serialization library
```

### Run db commands
Use `DB Browser for SQLite` for UI based tool
https://sqlitebrowser.org/dl/
```python
flask db_create
flask db_seed
flask drop_all
```

