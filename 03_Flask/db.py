import os
import psycopg

def get_connection():
    connection = psycopg.connect(
        dbname="employee_management",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD"),
        host="localhost"
    )

    return connection


if __name__ == "__main__":
    connection = get_connection()
    print("Flask database connection successful!")
    connection.close()