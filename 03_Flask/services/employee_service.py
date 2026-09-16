from db import get_connection
from psycopg.errors import UniqueViolation




def update_employee_salary(employee_id, salary):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            UPDATE employees
            SET salary = %s
            WHERE id = %s
            """,
            (salary, employee_id)
        )


        updated = cursor.rowcount

        if updated == 0:
            connection.rollback()
            return None

        connection.commit()

        cursor.execute(
            """
            SELECT id, name, salary, department
            FROM employees
            WHERE id = %s
            """,
            (employee_id,)
        )

        row = cursor.fetchone()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "salary": row[2],
            "department": row[3]
        }

    return None

def delete_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM employees
            WHERE id = %s
            """,
            (employee_id,)
        )

        connection.commit()
    
        deleted = cursor.rowcount

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    return deleted > 0


def get_all_employees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    employees = []

    for row in rows:
        employee = {
            "id": row[0],
            "name": row[1],
            "salary": row[2],
            "department": row[3]
        }

        employees.append(employee)

    cursor.close()
    connection.close()

    return employees
    
    

def get_employee_by_id(employee_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, salary, department
        FROM employees
        WHERE id = %s
        """,
        (employee_id,)
    )

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "salary": row[2],
            "department": row[3]
        }

    return None


def create_employee(employee):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO employees (id, name, salary, department)
            VALUES (%s, %s, %s, %s)
            """,
            (
                employee["id"],
                employee["name"],
                employee["salary"],
                employee["department"]
            )
        )
    

        connection.commit()
        return employee

    except UniqueViolation:
        connection.rollback()
        return None

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()      
        connection.close()
