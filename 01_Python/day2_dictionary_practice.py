employee = {
    "name": "Vignesh",
    "salary": 50000
}

employee["name"] = "Vijay"

print(employee["name"])



employee = {
    "name": "Vignesh",
    "salary": 50000
}

#pop()
x = employee.pop("name")
print(x)


#del
employee = {
    "name": "rajini",
    "salary": 50000
}
del employee["salary"]
print(employee)


#clear
actor = {
    "name": "kamal",
}

actor.clear()

print(actor)



cars = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(cars.get("brand"))

print(cars.get("color", "Value not found"))

print(cars.keys())

print(cars.values())

print(cars.items())