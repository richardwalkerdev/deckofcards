## Commands

### Run local server

`python manage.py runserver`

### Run tests

`python manage.py test`

### Run pylint

```
pylint --load-plugins pylint_django main/
pylint --load-plugins pylint_django decofcards/
```

### Use curl

`curl -X GET http://127.0.0.1:8000/deck/`