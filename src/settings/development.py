import os
from .base import Base
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Development(Base):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    MEDIA_ROOT = os.path.join(BASE_DIR, "assets", "media")
    STATIC_ROOT = ''

    AP_ADMIN_EMAIL = 'koles.web@gmail.com'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False

            }
        }
    }
    ROBOKASSA_TEST = False
