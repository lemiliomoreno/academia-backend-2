import os


def get_db_credentials():
    return {
        "db_user": os.getenv("POSTGRES_USER"),
        "db_password": os.getenv("POSTGRES_PASSWORD"),
        "db_host": os.getenv("POSTGRES_HOST"),
    }
