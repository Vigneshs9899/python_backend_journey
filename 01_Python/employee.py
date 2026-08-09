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
    while True:
        try:
            emp_salary = int(input("Enter employee_salary: "))
            break
        except ValueError:
            print("Invalid salary. Please enter number.")
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
    update_salary = int(input("Enter the updated salary: "))
    emp["salary"] = update_salary
    print("Employee Data updated successfully")
    view_emp(emp)

def delete_employee(emp):
    employees.remove(emp)
    print("Employee data deleted successfully")


        

ch = 0
while (ch != 6):

    while True:
        try:
            ch = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Invalid choice. Please enter a number.")
    
    match ch:
        case 1:
            while True:
                try:
                    emp_id=int(input("Enter the employee id: "))
                    break
                except ValueError:
                    print("Invalid ID. Please enter a number.")
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
            search_id = int(input("Enter employee_id to search: "))
            found = False
            for emp in employees:
                if emp["id"] == search_id:
                    view_emp(emp)
                    found = True
                    break
            if not found:
                print("Employee not found")

        case 4:
            while True:
                try:
                    update_id = int(input("Enter employee id to update: "))
                    break
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            found = False
            for emp in employees:
                if emp["id"] == update_id:
                    update_employee(emp)
                    found = True
                    break
            if not found:
              print("Employee not found")

        case 5:
            while True:
                try:
                    delete_id = int(input("Enter employee id to delete: "))
                    break
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            found = False
            for emp in employees:
                if emp["id"] == delete_id:
                    delete_employee(emp)
                    found = True
                    break
            if not found:
                print("Employee not found")
        case 6:
            print("Thank you for using Employee Management System.")
            break

        case _:
            print("Invalid choice, please try again")






