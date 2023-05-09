# Revision

## HTTP Verbs

- GET - Retrieve a record or a collection of records.
- POST - Create a new record.
- PUT - Update an existing record by replacing the whole record.
- PATCH - Update an existing record by partially modifying the 
record.
- DELETE - Delete record(s). 

## What is the main purpose of APIs?

An API (Application Programming Interface) is a software-to-software 
interface that allows two applications to exchange data between each 
other.

### REST APIs

REST is a set of architectural constraints for an API to support high-performing and reliable communication at scale.

- Representational data flow (Uniform Interface)
- Messages
- Unique URI's/naming
- Statelessness
- Caching

## Requests Library

### How to make a get request in Python

```python
import requests

req = requests.get(url, params=params, auth=("user", "pass"))

req.status_code
req.headers
req.content
req.json()
```

### How to make JSON returned from API into a python dictionary

```python
import json
import urllib.request

python_dict = json.loads(open("file.json").read())
python_dict = json.load(open("file.json"))

with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
     data = json.load(url)
```

### How to make a POST request

```python
    import requests

    json_body = json.dumps({"key": "value"})
    headers = {"Content-Type": "application/json"}

    var_request = requests.post("url", headers=headers, data=json_body)
```
