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



if(__name__) == "__main__":
    app.run(debug=True)