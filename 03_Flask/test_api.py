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

# response = requests.put(
#     "http://127.0.0.1:5000/employees/1",
#     json={
#         "salary": 80000
#     }
# )

# print(response.status_code)
# print(response.json())



# response = requests.delete(
#     "http://127.0.0.1:5000/employees/1"
# )

# print(response.status_code)
# print(response.json())




# response = requests.delete(
#     "http://127.0.0.1:5000/employees/99"
# )

# print(response.status_code)
# print(response.json())