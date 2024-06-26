import time
import psycopg2
import subprocess
import os
from dotenv import load_dotenv


load_dotenv()


def check_db_connection(host, port, user, password, database):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        conn.close()
        return True
    except psycopg2.OperationalError:
        return False


def main():
    db_host = os.environ.get("POSTGRES_HOST")
    db_port = os.environ.get("POSTGRES_PORT")
    db_user = os.environ.get("POSTGRES_USER")
    db_password = os.environ.get("POSTGRES_PASSWORD")
    db_name = os.environ.get("POSTGRES_DB")

    max_retries = 10
    retries = 0
    while not check_db_connection(db_host, db_port, db_user, db_password, db_name):
        retries += 1
        if retries >= max_retries:
            print(f"Unable to connect to the database after {max_retries} attempts. Exiting.")
            return
        print(f"Trying to connect to the database. Trying attempt #{retries}")
        time.sleep(5)

    try:
        subprocess.run(["alembic", "upgrade", "head"])
        time.sleep(2)
    except subprocess.CalledProcessError as e:
        print("Error while performing database migration:", e)
        return

    print(f"{'***' * 20} Database is available! {'***' * 20}")


if __name__ == "__main__":
    main()
