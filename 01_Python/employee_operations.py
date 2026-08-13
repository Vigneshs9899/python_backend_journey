from utils import get_integer_input

def find_employee(employees, search_id):
    
    for emp in employees:
        if emp["id"] == search_id:
            return emp        
    return None


def add_emp(emp_id):
    emp_name = input("Enter employee_name: ")
    emp_salary = get_integer_input("Enter employee_salary: ")
    emp_department = input("Enter employee_department: ")
    employee = {"id": emp_id, "name": emp_name, "salary": emp_salary, "department": emp_department}
    print("Employee added successfully")
    return employee

def view_emp(employee):
    print("Employee ID: ", employee["id"])
    print("Employee Name: ", employee["name"])
    print("Employee Salary: ", employee["salary"])
    print("Employee Department: ", employee["department"])
    print("-" * 30)



def update_employee(emp):
    update_salary = get_integer_input("Enter the updated salary: ")
    emp["salary"] = update_salary
    print("Employee Data updated successfully")
    view_emp(emp)

def delete_employee(emp, employees):
    employees.remove(emp)
    print("Employee data deleted successfully")