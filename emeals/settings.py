import os

import environ
env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# reading .env file
env_file = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(env_file)

SECRET_KEY = env(
    'SECRET_KEY',
    default='qolcmidak1veo136fjuyne0xr$t_3zi*^y@xy(jy!vdn_b4_c*'
)

DEBUG = env.bool('DJANGO_DEBUG', False)

ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]

# Apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'dishes',
    'menus',
    'reservations',
    'users'
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'emeals.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'emeals.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = env('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join('static'),
)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = LOGIN_URL


# Time for closing reservations
RESERVE_CLOSING = env('RESERVE_CLOSING', default='11')
SLACK_CHANEL = env('SLACK_CHANEL')
SITE_DOMINE = env('SITE_DOMINE')

# For RabbitMQ
BROKER_URL = env('BROKER_URL')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND')

# Celery Data Format
CELERY_ACCEPT_CONTENT = [env('CELERY_ACCEPT_CONTENT')]
CELERY_TASK_SERIALIZER = env('CELERY_TASK_SERIALIZER')
CELERY_RESULT_SERIALIZER = env('CELERY_RESULT_SERIALIZER')
CELERY_TIMEZONE = env('TIME_ZONE')

# Crontab
CRONTAB_MINUTE = env('CRONTAB_MINUTE')
CRONTAB_HOUR = env('CRONTAB_HOUR')
CRONTAB_DAY_OF_WEEK = env('CRONTAB_DAY_OF_WEEK')
