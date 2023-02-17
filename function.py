# def my_function(first_name):
#     print(first_name+ "hello")

# my_function("John")

#Exercise 1
# input("Enter your name")
# def my_function(name):
#     print(name+ "hello")
# my_function("John")

#Exercise 2
# value1 = int(input("Enter first_value"))
# value2 = int(input("Enter second_value"))
# value = value1 + value2
# def my_function(value):
#     print(value)
# my_function(value)

# value = value1 / value2
# def my_function(value):
#     print(value)
# my_function(value)


# value = value1 + value2
# print(value)
# value = value1 / value2
# print(value)

# def add_nums():
#     print("My_function")
# add_nums()
# add_nums()
# add_nums()

# def add_nums(a, b):
#     result = a + b
#     print(result)
# add_nums(2, 3)
# #or
# add_nums(a=2, b=3)

# def add_nums(a, b):
#     sales = a + b
#     print(sales)
# add_nums(20, 30)

#Exercise
# username1 = input("Enter first name:")
# username2 = input("Enter second name:")
# username = username1 + username2

# def add_names(username):

#     print("Hello there", username1, username2)
# add_names(username)

#Scoping - don't use a code outside its function
av = 56

def average(a, b):
    av = (a + b) /2
    return av

print(av)