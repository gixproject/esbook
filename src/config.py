import os
from logging.config import dictConfig

logging_config = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
            "level": os.environ.get("LOG_LEVEL", "INFO"),
        }
    },
    "loggers": {
        "": {
            "level": os.environ.get("LOG_LEVEL", "INFO"),
            "propagate": True,
            "handlers": ["console"],
        },
    },
    "disable_existing_loggers": False,
}


class Config:
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = "top-secret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # silence the deprecation warning
    RESTPLUS_VALIDATE = True
    dictConfig(logging_config)

    # Swagger
    SWAGGER_UI_DOC_EXPANSION = "list"
    SWAGGER_UI_OPERATION_ID = True

    # Elastic
    ELASTICSEARCH_URI = os.environ.get("ELASTICSEARCH_URI", "elasticsearch:9200")
    ELASTIC_BOOKS_INDEX = "books"
    ELASTIC_AUTHORS_INDEX = "authors"

    # Database settings
    DB_USER = os.environ.get("DB_USER", "postgres")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
    DB_HOST = os.environ.get("DB_HOST", "postgres")
    DB_NAME = os.environ.get("DB_NAME", "postgres")
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
    )


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    SWAGGER_UI_REQUEST_DURATION = True


class TestConfig(Config):
    TESTING = True
    CSRF_ENABLED = False
    DB_NAME = f"{Config.DB_NAME}_test"
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
        Config.DB_USER, Config.DB_PASSWORD, Config.DB_HOST, DB_NAME
    )


config = {
    "development": DevelopmentConfig,
    "testing": TestConfig,
    "production": ProductionConfig,
}
