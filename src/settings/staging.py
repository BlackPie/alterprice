from .base import Base


class Staging(Base):
    DEBUG = False

    MEDIA_ROOT = '/media'
    STATIC_ROOT = '/static'
    ALLOWED_HOSTS = '*'
