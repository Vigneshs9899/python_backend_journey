employees = []

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
    print("-" * 30)

ch = 0
while (ch != 3):

    ch = int(input("Enter your choice: "))
    
    match ch:
        case 1:
            while True:
                employee = add_emp()
                employees.append(employee)
                ch1 = input("Do you want to add another employee? (y/n): ")
                if ch1.lower() != 'y':
                    break
        case 2:
            if not employees:
                print("No employee added") 
            else:
                for emp in employees:
                    view_emp(emp)
        case 3:
            print("Thank you for using Employee Management System.")
            break

        case _:
            print("Invalid choice, please try again")



