import psycopg2
import pytest
from decouple import config
from dj_database_url import parse


@pytest.fixture
def database_connection():
    database = config("DATABASE_URL", cast=parse)

    connection = psycopg2.connect(
        host=database.get("HOST"),
        port=database.get("PORT"),
        user=database.get("USER"),
        password=database.get("PASSWORD"),
        dbname=database.get("NAME"),
    )

    yield connection

    connection.close()


@pytest.mark.django_db
def tests_for_connection_to_a_postgres_database(database_connection):
    cursor = database_connection.cursor()

    cursor.execute("SELECT 1")
    result = cursor.fetchone()

    assert result[0] == 1
