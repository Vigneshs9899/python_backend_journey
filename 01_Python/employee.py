employee = None

print("Employee Management System")
print("--------------------------")
print("1. Add Employee")
print("2. View Employee")
print("3. Exit")

def add_emp():
    emp_id = int(input("Enter employee_id: "))
    emp_name = input("Enter employee_name: ")
    emp_salary = int(input("Enter employee_salary: "))
    emp_department = input("Enter employee_department: ")
    employee = {"id": emp_id, "name": emp_name, "salary": emp_salary, "department": emp_department}
    print("Employee added successfully")
    return employee

def view_emp(employee):
    print("Employee ID: ", employee["id"])
    print("Employee Name: ", employee["name"])
    print("Employee Salary: ", employee["salary"])
    print("Employee Department: ", employee["department"])

ch = 0
while (ch != 3):

    ch = int(input("Enter your choice: "))
    
    match ch:
        case 1:
            employee = add_emp()
        case 2:
            if employee is None:
                print("No employee added") 
            else:
                view_emp(employee)
        case 3:
            print("Thank you for using Employee Management System.")
            break

        case default:
            print("Invalid choice, please try again")



