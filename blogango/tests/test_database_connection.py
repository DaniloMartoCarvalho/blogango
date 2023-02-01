import psycopg2
from decouple import config
from dj_database_url import parse
from django.test import TestCase


class DatabaseTestCase(TestCase):
    def setUp(self) -> None:

        database = config("DATABASE_URL", cast=parse)

        self.connection = psycopg2.connect(
            host=database.get("HOST"),
            port=database.get("PORT"),
            user=database.get("USER"),
            password=database.get("PASSWORD"),
            dbname=database.get("NAME"),
        )

    def test_connection(self) -> None:
        cursor = self.connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        self.assertEqual(result[0], 1)

    def tearDown(self) -> None:
        self.connection.close()
