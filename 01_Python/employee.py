employees = []


print("Employee Management System")
print("--------------------------")
print("1. Add Employee")
print("2. View Employee")
print("3. Search Employee by ID")
print("4. Update Employee")
print("5. Delete Employee")
print("6. Exit")

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

def get_integer_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid. Please enter a number.")


        

ch = 0
while (ch != 6):

    ch = get_integer_input("Enter your choice: ")
    
    
    match ch:
        case 1:
            emp_id = get_integer_input("Enter employee id: ")        
            found = False
            for emp in employees:
                if emp["id"] == emp_id:
                    found = True
                    print("Employee already exists")
                    break
            if not found:
                employee = add_emp(emp_id)
                employees.append(employee)
                
            
        case 2:
            if not employees:
                print("No employee added") 
            else:
                for emp in employees:
                    view_emp(emp)
        case 3:
            search_id = get_integer_input("Enter employee_id to search: ")
            found = False
            for emp in employees:
                if emp["id"] == search_id:
                    view_emp(emp)
                    found = True
                    break
            if not found:
                print("Employee not found")

        case 4:
            update_id = get_integer_input("Enter employee id to update: ")
            found = False
            for emp in employees:
                if emp["id"] == update_id:
                    update_employee(emp)
                    found = True
                    break
            if not found:
              print("Employee not found")

        case 5:
            delete_id = get_integer_input("Enter employee id to delete: ")
            found = False
            for emp in employees:
                if emp["id"] == delete_id:
                    delete_employee(emp, employees)
                    found = True
                    break
            if not found:
                print("Employee not found")
        case 6:
            print("Thank you for using Employee Management System.")
            break

        case _:
            print("Invalid choice, please try again")






