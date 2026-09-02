from flask import Flask, request
from routes.employee_routes import employee_bp

app = Flask(__name__)
app.register_blueprint(employee_bp)



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








      

if(__name__) == "__main__":
    app.run(debug=True)