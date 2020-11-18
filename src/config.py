import os


class Config:
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = "top-secret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # silence the deprecation warning
    RESTPLUS_VALIDATE = True

    # Database settings
    DB_USER = os.environ.get("DB_USER", "postgres")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
    DB_HOST = os.environ.get("DB_HOST", "postgres")
    DB_NAME = os.environ.get("DB_NAME", "postgres")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestConfig,
    "production": ProductionConfig
}
