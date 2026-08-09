try:
    salary = int(input("Enter salary: "))
    print("Salary:", salary)
except ValueError:
    print("Invalid salary")