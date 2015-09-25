# -*- coding: utf-8 -*-
import os
import sys
from configurations import Configuration, values
from kombu import Exchange, Queue

# base dir (parent of settings dir)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

APPS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, 'apps'))
if APPS_PATH not in sys.path:
    sys.path.append(APPS_PATH)


class Base(Configuration):
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    ADMINS = (
        ('Vladimir Shulyak', 'vs@createdigital.me'),
    )

    MANAGERS = ADMINS

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME':     os.environ.get('POSTGRESQL_NAME'),
            'USER':     os.environ.get('POSTGRESQL_USER'),
            'PASSWORD': os.environ.get('POSTGRESQL_PASS'),
            'HOST':     os.environ.get('DB_PORT_5432_TCP_ADDR'),
            'PORT':     os.environ.get('DB_PORT_5432_TCP_PORT'),
        }
    }

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # On Unix systems, a value of None will cause Django to use the same
    # timezone as the operating system.
    # If running in a Windows environment this must be set to the same as your
    # system time zone.

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html

    SITE_ID = 1

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale

    LANGUAGE_CODE = 'ru-ru'

    TIME_ZONE = 'Europe/Moscow'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = ''

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = '/media/'

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = ''

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'

    STATIC_LIBS_URL = '/static/libs/'

    # URL prefix for admin static files -- CSS, JavaScript and images.
    # Make sure to use a trailing slash.
    # Examples: "http://foo.com/static/admin/", "/static/admin/".
    ADMIN_MEDIA_PREFIX = '/static/admin/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(BASE_DIR, "assets"),
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = '+ulem!a0+!qaupyr7loo0ozcbtmyjo2ob2k3eo=_r8&_(y5&#%f'

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, "templates"),
    )

    TEMPLATE_CONTEXT_PROCESSORS = Configuration.TEMPLATE_CONTEXT_PROCESSORS + (
        'alterprice.processors.categories',
        'alterprice.processors.current_url',
        'alterprice.processors.cities',
        'alterprice.processors.current_city',
        'client.processors.shop_processor',
        'django.core.context_processors.request',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'client.middleware.ShopMiddleware',
        'alterprice.middleware.CityMiddleware'
    )

    ROOT_URLCONF = 'alterprice.urls'

    EXTERNAL_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.humanize',
        'rest_framework',
        'django_filters',
        'django_extensions',
        'django_ses',
        'djcelery',
        'template_email',
        'autoslug',
        'easy_thumbnails',
        'raven.contrib.django.raven_compat',
        'django_geoip',
    )

    INTERNAL_APPS = (
        'alterprice',
        'apuser',
        'catalog',
        'utils',
        'shop',
        'product',
        'brand',
        'client',
        'markup',  # TMP app
        'marketapi',
    )

    INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

    AUTH_USER_MODEL = 'apuser.AlterPriceUser'

    REST_FRAMEWORK = {
        'DEFAULT_FILTER_BACKENDS': (
            'rest_framework.filters.DjangoFilterBackend',
            'rest_framework.filters.SearchFilter'
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            # 'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
        # 'DEFAULT_PERMISSION_CLASSES': (
        #     'rest_framework.permissions.IsAuthenticated',
        # ),
        'PAGINATE_BY': 10,
        'PAGINATE_BY_PARAM': 'page_size',
        'MAX_PAGINATE_BY': 99999,  # TODO: fixme
        'DATETIME_FORMAT': "%d.%m.%Y"
    }

    # INternal apps settings
    MAX_FILE_UPLOAD_SIZE = 8*1024*1024

    DEFAULT_CLICK_PRICE = 3

    EMAIL_TOKEN_LENGHT = 32
    EMAIL_TOKEN_PATTERN = '[0-9a-z]{%d}' % EMAIL_TOKEN_LENGHT
    EMAIL_TOKEN_LIFE_DAYS = 1

    RECOVERY_TOKEN_LIFE_DAYS = 1
    RECOVERY_TOKEN_LENGHT = 32
    RECOVERY_TOKEN_PATTERN = '[0-9a-z]{%d}' % RECOVERY_TOKEN_LENGHT

    AWS_SES_REGION_NAME = 'eu-west-1'
    AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'

    AWS_ACCESS_KEY_ID = 'AKIAIF2XWI25JNNWOOPA'
    AWS_SECRET_ACCESS_KEY = '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'

    EMAIL_BACKEND = 'django_ses.SESBackend'
    DEFAULT_FROM_EMAIL = 'robot@createdigital.me'

    # Redis settings

    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')

    # rabbit
    RABBIT_HOSTNAME = os.environ.get('RABBIT_PORT_5672_TCP', 'localhost:5672')

    if RABBIT_HOSTNAME.startswith('tcp://'):
        RABBIT_HOSTNAME = RABBIT_HOSTNAME.split('//')[1]

    BROKER_URL = os.environ.get('BROKER_URL', '')
    if not BROKER_URL:
        BROKER_URL = 'amqp://{user}:{password}@{hostname}/{vhost}/'.format(
            user=os.environ.get('RABBIT_ENV_USER', 'admin'),
            password=os.environ.get('RABBIT_ENV_RABBITMQ_PASS', 'mypass'),
            hostname=RABBIT_HOSTNAME,
            vhost=os.environ.get('RABBIT_ENV_VHOST', ''))

    # We don't want to have dead connections stored on rabbitmq, so we have to negotiate using heartbeats
    BROKER_HEARTBEAT = '?heartbeat=30'
    if not BROKER_URL.endswith(BROKER_HEARTBEAT):
        BROKER_URL += BROKER_HEARTBEAT

    BROKER_POOL_LIMIT = 1
    BROKER_CONNECTION_TIMEOUT = 10

    # Celery settings
    CELERY_ENABLE_UTC = True
    CELERY_TIMEZONE = 'Europe/Moscow'

    # configure queues, currently we have only one
    CELERY_DEFAULT_QUEUE = 'default'
    CELERY_QUEUES = (
        Queue('default', Exchange('default'), routing_key='default'),
    )

    # Sensible settings for celery
    CELERY_ALWAYS_EAGER = False
    CELERY_ACKS_LATE = True
    CELERY_TASK_PUBLISH_RETRY = True
    CELERY_DISABLE_RATE_LIMITS = False
    # By default we will ignore result
    # If you want to see results and try out tasks interactively, change it to False
    # Or change this setting on tasks level
    CELERY_IGNORE_RESULT = True
    CELERY_SEND_TASK_ERROR_EMAILS = False
    CELERY_TASK_RESULT_EXPIRES = 600

    # Set redis as celery result backend
    # CELERY_RESULT_BACKEND = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)
    CELERY_RESULT_BACKEND = 'redis://%s:6379/0' % REDIS_HOST
    CELERY_REDIS_MAX_CONNECTIONS = 1

    # Don't use pickle as serializer, json is much safer
    CELERY_TASK_SERIALIZER = "json"
    CELERY_ACCEPT_CONTENT = ['application/json']

    CELERYD_HIJACK_ROOT_LOGGER = False
    CELERYD_PREFETCH_MULTIPLIER = 1
    CELERYD_MAX_TASKS_PER_CHILD = 1000

    CELERY_REDIRECT_STDOUTS_LEVEL = 'INFO'

    THUMBNAIL_ALIASES = {
        '': {
            'product_small': {'size': (200, 160), 'autocrop': False, 'crop': False},
            'product_big': {'size': (428, 320), 'autocrop': False, 'crop': False},
            'category': {'size': (200, 150), 'autocrop': False, 'crop': False},
        }
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
            'debug': {
                'format': "%(levelname)s [%(name)s:%(lineno)s] %(message)s",
            },
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'INFO',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'debug',
            },
            'null': {
                'class': 'logging.NullHandler',
            },
            'logfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': "/var/log/app/django.log",
                'maxBytes': 50000,
                'backupCount': 2,
                'formatter': 'standard',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
            },
            'werkzeug': {
                'handlers': ['console'],
            },
            'django.request': {
                'handlers': ['logfile'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.security': {
                'handlers': ['logfile'],
                'level': 'ERROR',
                'propagate': False,
            },
            'py.warnings': {
                'handlers': ['console'],
            },
            '': {
                'handlers': ['logfile'],
                'level': 'WARN',
            },
        }
    }

    ROBOKASSA_PASS1 = os.environ.get('ROBOKASSA_PASS1')
    ROBOKASSA_PASS2 = os.environ.get('ROBOKASSA_PASS2')
    ROBOKASSA_LOGIN = os.environ.get('ROBOKASSA_LOGIN')
    ROBOKASSA_TEST = True
    ROBOKASSA_TAX = 0.05

    MARKET_API_KEY = os.environ.get('MARKET_API_KEY')

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://redis:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
    RAVEN_CONFIG = {
        'dsn': os.environ.get('SENTRY_PRIVATE_DSN'),
    }
