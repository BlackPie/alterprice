from .base import Base
import djcelery


djcelery.setup_loader()

class Staging(Base):
    DEBUG = False

    MEDIA_ROOT = '/media'
    STATIC_ROOT = '/static'
    ALLOWED_HOSTS = '*'
