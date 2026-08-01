# This function takes two numbers as input and returns the maximum of the two using the built-in max() function. The result is then printed to the console.
def maximum(a,b):
    return max(a,b)

result = maximum(10, 25)

print("The maximum value is:", result)


# This function takes a number as input and returns whether the number is even or odd. The result is then printed to the console.
def even_or_odd(num):
    if num % 2 ==0:
        return "Even"
    else:
        return "Odd"
num=6

result = even_or_odd(num)

print("The number",num,"is", result)


# This function takes a number as input and returns its factorial using the math.factorial() function. The result is then printed to the console.
from math import factorial as fact

def factorial(num):
    return fact(num)

result = factorial(5)

print("The factorial of 5 is:", result)


# This function takes a list of numbers as input and returns the sum and average of the numbers. The results are then printed to the console.
def simple(a):

    sum=0

    for i in a:

        sum = sum + i

        avg = sum / len(a)

    print("The sum is:", sum)
    print("The average is:", avg)

a=[10,20,30]

result = simple(a)



# This function takes an employee's name and salary as input and returns them as a tuple. The results are then printed to the console.
def employee(name, salary):

    return name, salary

result = employee("Vignesh",45000)

print("Employee Name:", result[0])
print("Employee Salary:", result[1])