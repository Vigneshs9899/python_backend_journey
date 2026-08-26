from flask import Flask, request

app = Flask(__name__)

employees = []

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "This is my Flask backend"


@app.route("/api")
def api():
    return {
        "message": "Welcome to my API",
        "status": "success"
    }

@app.route("/employees", methods=["POST"])
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
    employees.append(employee)   
    return {
               "message": "Employee recieved successfully",
               "employee": employee
           }, 201


@app.route("/employees", methods=["GET"])
def get_employees():
      return {
            "message": "Employee data recieved",
            "employee": employees
      }, 200


@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
      for employee in employees:
        if employee["id"] == employee_id:
            return {
                "message": "Employee recieved",
                "employee": employee
            
            },200
      return {
                  "message": "Employee id not found"
            }, 400


@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            update_data = request.get_json()
            employee["salary"] = update_data["salary"]
            return{
                "message": "Employee Data updated",
                "employee": employee
            }, 200
          
    return {
          
    "message": "Employee id not found"
          
    }, 404

@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
     for employee in employees:
          if employee["id"] == employee_id:
            employees.remove(employee)
            return{
                 "message": "Employee data deleted successfully"
            }, 200
     return{
        "message": "Employee id not found"
        }, 404
      

if(__name__) == "__main__":
    app.run(debug=True)