# Monitoring Views Workshop

* if you want a easy installation use **pipenv\*** else use **requirements.txt**

**pipenv:** can be installed wih:

```bash
pip install pipenv
```

dont forget to check if you have the right python version: 3.8

* Executing with pipenv 
```bash
pipenv run python {command}
```
Example:
```bash
pipenv run python manage.py makemigrations 
```

GET {{host}}:{{port}}{{api_path}}/measurements/?id=1
RESPONSE:
[
    {
        "model": "measurements.measurement",
        "pk": 1,
        "fields": {
            "variable": 4,
            "value": 2.0,
            "unit": "kg",
            "place": "Wakanda",
            "dateTime": "2022-02-14T03:59:25.149Z"
        }
    }
]

GET {{host}}:{{port}}{{api_path}}/measurements
RESPONSE:
[
    {
        "model": "measurements.measurement",
        "pk": 1,
        "fields": {
            "variable": 4,
            "value": 2.0,
            "unit": "kg",
            "place": "Wakanda",
            "dateTime": "2022-02-14T03:59:25.149Z"
        }
    },
    {
        "model": "measurements.measurement",
        "pk": 2,
        "fields": {
            "variable": 3,
            "value": -2.0,
            "unit": "lb",
            "place": "Banania",
            "dateTime": "2022-02-14T04:13:08.410Z"
        }
    }
]

DELETE {{host}}:{{port}}{{api_path}}/measurements/1
RESPONSE: No response. GET -> No aparece la borrada. Borrado exitoso.