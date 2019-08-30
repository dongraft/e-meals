# E-Meals Nora

Basic management system to coordinate the meal delivery for Cornershop employees. (Backend Challenge)

Clone the repo:
```
$ git clone https://github.com/aroldolanderos/e-meals.git
```

```
$ cd e-meals
```


Create a virtual env with python3
```
$ virtualenv myprojectenv  (python3)
```

```
$ virtualenv source myprojectenv/bin/activate
```

Install dependences

```
$ pip install -r requirements.txt
```



### Define environment variables
```
SECRET_KEY=<my_secret_key>
DJANGO_DEBUG=True

# DB
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<db_name>
DB_USER=<db_user>
DB_PASSWORD=<db_pass>
DB_HOST=localhost
DB_PORT=5432

TIME_ZONE='America/Santiago'
RESERVE_CLOSING='11'
ALLOWED_HOSTS=*

#'https://hooks.slack.com/services/xxxx/yyyy'
SLACK_CHANEL='<slack_chanel_url>'

# ip or domine
SITE_DOMINE='http://127.0.0.1:8000'
BROKER_URL='amqp://127.0.0.1'

# Celery config
CELERY_ACCEPT_CONTENT='application/json'
CELERY_RESULT_BACKEND='amqp://127.0.0.1'
CELERY_TASK_SERIALIZER='json'
CELERY_RESULT_SERIALIZER='json'
CRONTAB_MINUTE=30
CRONTAB_HOUR='8,9' #AM
CRONTAB_DAY_OF_WEEK='mon-fri'
```

#### Generate Secret Key for environment
```
$ touch generador_django.py
```

```
$ vim generador_django.py
```

Paste into generador_django.py
```
"""
Pseudo-random django secret key generator.
- Does print SECRET key to terminal which can be seen as unsafe.
"""

import string
import random

# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')

SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

print(SECRET_KEY)
``` 

``` 
$ python3 generador_django.py
``` 

If you have openssl, you can run
```
$ openssl rand -base64 32
```

[Sample source of how to generate secret key](https://programadorwebvalencia.com/como-generar-un-secret-key-en-django)

### Django initial commands

Apply migrations
```
$ python manage.py migrate
```

Generate statics files
```
$ python manage.py collectstatic
```

#### To test locally

Run Celery
```
$ celery -A emeals worker -l info -B
```

And in a different tab

```
$ python manage.py runserver
```