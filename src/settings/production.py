from .base import Base
import djcelery


djcelery.setup_loader()


class Production(Base):
    DEBUG = False

    MEDIA_ROOT = '/media'
    STATIC_ROOT = '/static'
    ALLOWED_HOSTS = '*'
    DEFAULT_HOST = 'http://alterprice.staging.corp.createdigital.me'
