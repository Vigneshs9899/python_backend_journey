from flask import Blueprint, request
from services.employee_service import (update_employee_salary, delete_employee, create_employee, get_all_employees, get_employee_by_id)

employee_bp = Blueprint("employee", __name__)



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
    employee = create_employee(employee)  
    return {
               "message": "Employee recieved successfully",
               "employee": employee
           }, 201

@employee_bp.route("/employees", methods=["GET"])
def get_employees():

    employees = get_all_employees()
      
    return {
          "message": "Employee data recieved",
          "employee": employees
    }, 200


@employee_bp.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = get_employee_by_id(employee_id)

    if employee:
        return employee,200
    
    return {
                  "message": "Employee id not found"
            }, 404


@employee_bp.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    update_data = request.get_json()
    employee = update_employee_salary(
          employee_id,
          update_data["salary"]
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
    deleted = delete_employee(employee_id)
    if deleted:
        return{
            "message": "Employee data deleted successfully"
         } , 200
    return{
        "message": "Employee id not found"
        }, 404