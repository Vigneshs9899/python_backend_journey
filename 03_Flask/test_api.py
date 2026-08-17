import requests

response = requests.post(
    "http://127.0.0.1:5000/employees",
    json={
        "id": 1,
        "name": "Vignesh",
        "salary": 50000,
        "department": "IT"

    }

    )

print(response.status_code)
print(response.json())