from config.settings.base import *  # NOQA

from dotenv import load_dotenv

import os

load_dotenv()

SECRET_KEY = "django-insecure--ff1lm@x^6fcwvd6+ewwoeu%f*5$3y34qfg$-^*-q8e+99co9s"

DEBUG = True

ALLOWED_HOSTS = []  # NOQA

INSTALLED_APPS += [  # NOQA
    "crispy_forms",
    "crispy_bootstrap5",
]  # NOQA

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "0.0.0.0",
            "PORT": 5432,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT"),
            "TEST": {
                "NAME": "postgres",
            },
        }
    }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",  # NOQA
#     }
# }

STATIC_URL = "static/"
