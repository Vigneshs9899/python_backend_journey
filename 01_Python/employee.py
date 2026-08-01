

employee = None

print("Employee Management System")
print("--------------------------")
print("1. Add Employee")
print("2. View Employee")
print("3. Exit")

def add_emp():
    emp_name = input("Enter employee_name: ")
    emp_salary = int(input("Enter employee_salary: "))
    employee = [emp_name, emp_salary]
    return employee

def view_emp(employee):
    print("Employee Name: ", employee[0])
    print("Employee Salary: ", employee[1])

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
            exit()



