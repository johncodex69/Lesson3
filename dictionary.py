# cars = {
# "model": "jeep",
# "year" :2021,
# "type" :"trackhawk"
# }
# print(cars["type"])

#Nested dictionary
# cars = {
#     "car1": {"type": "bentley"},
#     "cars2": {"type": "ferrari"}} 
# print(cars["cars2"])


# car = {
#     "model" : "ford",
#     "year" : 1998,
#     "color" : "red",
#     "country" : "States"
# }

# #Accessing dictionary items
# print(car["year"])

# person = {
#     "name" : "Kathy",
#     "age" : 27,
#     "pets" : ["dog", "cat"]
# }
# # Accessing dictionary

# # print(person["pets"])

# person["pets"][0]
# print(person["pets"][0])

# person = {
#     "name" : "Kathy",
#     "age" : 27,
#     "pets" : {
#         "dog" : "x",
#         "cat" : "y"
#     }
# }
# print(person["pets"])
# print(person["pets"]["cat"])

# #Integer keys
# teams = {
#     23 : "a",
#     56.67 : [34, 453, 87]

# }
# print(teams[56.67])

# profile = {}
# profile["username"] = "user123"
# profile["age"] = 26
# profile["email"] = "123prosporous@gmail.com"

# print(profile)

# profile = {}

# def sign_up():
# #Ask for username
#     username = input("Enter username:")
# #Ask for email
#     email = input("Enter email:")
# #Ask for password
#     password = input("Enter password:")

# #Store in dictionary
#     profile["username"] = username
#     profile["email"] = email
#     profile["passsword"] = password

# sign_up()

# def get_profile():
#     print(profile)

# def change_username():
#     new_username = input("Enter new_username:")
#     profile["username"] = new_username

# sign_up()
# get_profile()

# change_username()
# get_profile()

months = {"January" : 31,
           "February" : 29,
           "March" : 31,
           "April" : 30,
           "May" : 31,
           "June" : 30,
           "July" : 31,
           "August" : 31,
           "September" : 30,
           "October" : 31,
           "November" : 30,
           "December" : 31  
}

# days_of_month = input("Enter month:")
# print(months[days_of_month])

