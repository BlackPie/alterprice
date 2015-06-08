from .base import Base


class Staging(Base):
    DEBUG = False
    DEFAULT_HOST = 'http://alterprice.staging.corp.createdigital.me'
    MEDIA_ROOT = '/media'
    STATIC_ROOT = '/static'
