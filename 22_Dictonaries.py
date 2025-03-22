#we use curly brackets to define a dictionary
#Dictionaries in python are used to store keys values pairs
customer = {
    "name" : "Yash Kumar",
    "age" : 20,
    "is_verified" : True
}

#We also update the keys values
customer["age"] = 21
print(customer["age"])
print(customer["name"])
print(customer.get("City" , "Jaipur"))

#We also add new keys values
customer["City"] = "Jhunjhunu"
print(customer["City"])