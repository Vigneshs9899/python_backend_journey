import requests

# response = requests.post(
#     "http://127.0.0.1:5000/employees",
#     json={
#         "id": 1,
#         "name": "Vignesh",
#         "salary": 50000,
#         "department": "IT"

#     }

#     )

# print(response.status_code)
# print(response.json())
# response = requests.get(
#     "http://127.0.0.1:5000/employees/1"
# )

# print(response.status_code)
# print(response.json())

# response = requests.post(
#     "http://127.0.0.1:5000/employees",
#     json={
#          "id": 5,
#         "name": "Raj",
#         "salary": 60000,
#         "department": "Marketing"

#     }

#     )

# print(response.status_code)
# print(response.json())

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


# response = requests.put(
#     "http://127.0.0.1:5000/employees/1",
#     json={
#         "salary": 80000
#     }
# )

# print(response.status_code)
# print(response.json())


# response = requests.delete(
#     "http://127.0.0.1:5000/employees/3"
# )

# print(response.status_code)
# print(response.json())

# response = requests.post(
#     "http://127.0.0.1:5000/employees",
#     json={
#         "id": 2,
#         "name": "Vijay",
#         "salary": 10000,
#         "department": "IT"

#     }

#     )

# print(response.status_code)
# print(response.json())


# response = requests.post(
#     "http://127.0.0.1:5000/employees",
#     json={
#         "id": 3,
#         "name": "Ajith",
#         "salary": 90000,
#         "department": "IT"

#     }

#     )

# print(response.status_code)
# print(response.json())

# response = requests.put(
#     "http://127.0.0.1:5000/employees/2",
#     json={
#         "salary": 20000 
#     }
# )

# print(response.status_code)
# print(response.json())


# response = requests.delete(
#     'http://127.0.0.1:5000/employees/44',
# )

# print(response.status_code)
# print(response.json())


# response = requests.post(
#     "http://127.0.0.1:5000/employees",
#     json={}

#     )

# print(response.status_code)
# print(response.json())


# response = requests.post(
#     "http://127.0.0.1:5000/employees",
#     json={
#         "id": 6,
#         "name": "",
#         "salary": 50000,
#         "department": "IT"
#     }
# )

# print(response.status_code)
# print(response.json())


# response = requests.post(
#     "http://127.0.0.1:5000/employees",
#     json={
#         "id": 0,
#         "name": "Arun",
#         "salary": 50000,
#         "department": "IT"
#     }
# )

# print(response.status_code)
# print(response.json())


response = requests.put(
    "http://127.0.0.1:5000/employees/1",
    json={
        "salary": 600000
    }
)

print(response.status_code)
print(response.json())