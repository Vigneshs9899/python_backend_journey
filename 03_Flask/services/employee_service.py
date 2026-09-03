def create_employee(employee, employees):
    employees.append(employee)
    return employee

def find_employee(employee_id, employees):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return None

def update_employee_salary(employee_id, new_salary, employees):
    employee = find_employee(employee_id, employees)

    if employee:
        employee["salary"] = new_salary
        return employee

    return None

def delete_employee(employee_id, employees):
    employee = find_employee(employee_id, employees)

    if employee:
        employees.remove(employee)
        return employee

    return None