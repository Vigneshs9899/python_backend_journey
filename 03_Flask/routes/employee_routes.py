from flask import Blueprint, request
from services.employee_service import (find_employee, update_employee_salary, delete_employee, create_employee)

employee_bp = Blueprint("employee", __name__)

employees = []

@employee_bp.route("/employees", methods=["POST"])
def add_employee():
    employee = request.get_json()

    required_fields = ["id", "name", "salary", "department"]
    for fields in required_fields:
       
        if fields not in employee:
           return{
                       "message": f"Employee {fields} is required"
                   }, 400
        
        if not isinstance(employee["id"], int):
                    return{
                        "message": "ID must be an integer"
                    }, 400
        
        if not isinstance(employee["name"], str):
                    return{
                        "message": "Name must be string"
                    }, 400

        if not isinstance(employee["department"], str):
                    return{
                        "message": "Department must be string"
                    }, 400
        
        if not isinstance(employee["salary"], int):
            return{
                "message": "Salary must be an integer"
            }, 400
    employee = create_employee(employee, employees)  
    return {
               "message": "Employee recieved successfully",
               "employee": employee
           }, 201

@employee_bp.route("/employees", methods=["GET"])
def get_employees():
      return {
            "message": "Employee data recieved",
            "employee": employees
      }, 200


@employee_bp.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = find_employee(employee_id, employees)

    if employee:
        return employee,200
    
    return {
                  "message": "Employee id not found"
            }, 400


@employee_bp.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    update_data = request.get_json()
    employee = update_employee_salary(
          employee_id,
          update_data["salary"],
          employees
    )
    
    if employee:
        return{
            "message": "Employee Data updated",
            "employee": employee
        }, 200
          
    return {
          
    "message": "Employee id not found"
          
    }, 404

@employee_bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee_route(employee_id):
    employee = delete_employee(employee_id, employees)
    if employee:
        return{
            "message": "Employee data deleted successfully"
         } , 200
    return{
        "message": "Employee id not found"
        }, 404