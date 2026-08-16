from flask import Flask

app = Flask(__name__)

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
    return {
        "message": "Employee created successfully",
        "status": "success"
    }


if(__name__) == "__main__":
    app.run(debug=True)