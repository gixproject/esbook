import os
from logging.config import dictConfig


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(16))
    RESTPLUS_VALIDATE = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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
    SESSION_COOKIE_SECURE = True


class DevelopmentConfig(Config):
    DEBUG = True
    SWAGGER_UI_REQUEST_DURATION = True


class TestConfig(Config):
    TESTING = True
    DB_NAME = f"{Config.DB_NAME}_test"
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
        Config.DB_USER, Config.DB_PASSWORD, Config.DB_HOST, DB_NAME
    )


dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in "
                "%(pathname)s:%(lineno)d %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "level": os.environ.get("LOG_LEVEL", "INFO"),
            },
            "file": {
                "class": "logging.FileHandler",
                "level": os.environ.get("LOG_LEVEL", "WARNING"),
                "formatter": "default",
                "filename": os.environ.get("LOG_PATH", "esbook.log"),
                "mode": "a",
            },
        },
        "root": {
            "level": os.environ.get("LOG_LEVEL", "WARNING"),
            "handlers": ["console", "file"],
        },
        "disable_existing_loggers": False,
    }
)

config = {
    "development": DevelopmentConfig,
    "testing": TestConfig,
    "production": ProductionConfig,
}
