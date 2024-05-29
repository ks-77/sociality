import os

from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure--ff1lm@x^6fcwvd6+ewwoeu%f*5$3y34qfg$-^*-q8e+99co9s"

DEBUG = True

ALLOWED_HOSTS = []  # NOQA

INSTALLED_APPS += [  # NOQA
    "crispy_forms",
    "crispy_bootstrap5",
]  # NOQA

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", ""),
        "USER": os.getenv("POSTGRES_USER", ""),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
        "HOST": os.getenv("POSTGRES_HOST", ""),
        "PORT": os.getenv("POSTGRES_PORT", ""),
    },
    "default_sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    },
}

STATIC_URL = "static/"
