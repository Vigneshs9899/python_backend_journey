import psycopg
import os

connection = psycopg.connect(
    dbname="employee_management",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD"),
    host="localhost"
)

print("Database connected successfully")


cursor = connection.cursor()

# cursor.execute(
#     """
#     INSERT INTO employees (id, name, salary, department)
#     VALUES (%s, %s, %s, %s)
#     """,
#     (2,"Arun",45000,"HR")
# )
 
# connection.commit()

# cursor.execute(
#     """
#     UPDATE employees 
#     SET salary = %s
#     WHERE id = %s 
#     """,
#     (55000,2)
# )

# connection.commit()

cursor.execute(
    """
    DELETE FROM employees
    WHERE id = %s

    """,
    (2,)
)

connection.commit()

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

print(rows)

cursor.close()

connection.close()