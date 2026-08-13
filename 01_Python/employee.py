from utils import get_integer_input
from employee_operations import find_employee, add_emp, view_emp, delete_employee, update_employee


employees = []


print("Employee Management System")
print("--------------------------")
print("1. Add Employee")
print("2. View Employee")
print("3. Search Employee by ID")
print("4. Update Employee")
print("5. Delete Employee")
print("6. Exit")

        

ch = 0
while (ch != 6):

    ch = get_integer_input("Enter your choice: ")
    
    
    match ch:
        case 1:
            emp_id = get_integer_input("Enter employee id: ")        
            employee = find_employee(employees, emp_id)
            if employee is None:
                employee = add_emp(emp_id)
                employees.append(employee)                    
            else:
                print("Employee already exists")
                
            
        case 2:
            if not employees:
                print("No employee added") 
            else:
                for emp in employees:
                    view_emp(emp)
        case 3:
            search_id = get_integer_input("Enter employee_id to search: ")
            employee = find_employee(employees, search_id)

            if employee is None:
                print("Employee not found")
            else:
                view_emp(employee)
            

        case 4:
            update_id = get_integer_input("Enter employee id to update: ")
            employee = find_employee(employees, update_id)
            if employee is None:
                print("Employee not found")
            else:
                update_employee(employee)

        case 5:
            delete_id = get_integer_input("Enter employee id to delete: ")
            employee = find_employee(employees, delete_id)
            if employee is None:
                print("Employee not found")
            else:
                delete_employee(employee, employees)

        case 6:
            print("Thank you for using Employee Management System.")
            break

        case _:
            print("Invalid choice, please try again")






