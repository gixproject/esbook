import psycopg2
import pytest
from invoke import task
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import config as _config
from manage import app


@task
def tests(ctx, path=None):
    """
    Invokes test PostgreSQL database creating and runs tests.
    :param object ctx: CLI context.
    :param str path: A test file path.
    """
    app.config.from_object(_config["testing"])
    config = app.config
    db_name = config["DB_NAME"]

    # Get connect with PostgreSQL
    connection = psycopg2.connect(
        "user={} password='{}' host={}".format(
            config["DB_USER"],
            config["DB_PASSWORD"],
            config["DB_HOST"],
        )
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Drops existing test database and creates new
    cursor = connection.cursor()
    cursor.execute(f"drop database if exists {db_name}")
    cursor.execute(f"create database {db_name}")

    # Runs tests
    test_path = f"../tests/{path}"
    pytest.main([test_path])
