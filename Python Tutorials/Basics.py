# Writb=Noneogram that inputs two numbers.
# num1, num2 = input("Enter two numbers: ").split()

# Convert the two numbers from strings to integers
# num1 = int(num1)
# num2 = int(num2)

# Add the two numbers
# Sum = num1 + num2

# Subtract the two numbers
# difference = num1 - num2

# Product of the two numbers
# product = num1 * num2

# Quotient of the two numbers
# division = num1 / num2

# Print the results
# print("{} + {} = {}".format(num1, num2, Sum))
# print("{} - {} = {}".format(num1, num2, difference))
# print("{} * {} = {}".format(num1, num2, product))
# print("{} / {} = {}".format(num1, num2, division))

# Tutorial 2
# mile = input("What miles have you covered: ")
# mile = int(mile)
# kilometers = mile*1.60934

# print("{} miles equals {} kilometers".format(mile, kilometers))


# TUTORIAL 3 EXERCISE
# Feed the age of the person
# age = eval(input("What is your age? "))

# if age < 5:
# print("Too young for School")
# elif age == 5:
# print("Go to Kindergarten")
# elif (age > 5) and (age <= 17):
# grade = age - 5
# print("Should be in grade {}".format(grade))
# else:
# print("Go to college")

# def my_function():
# print("In my function")
# my_function()

# def my_function(counter=89):
# print("Counter: {}".format(counter))

# my_function(12)

# def my_function(counter):
# print("Counter: {}".format(counter))

# my_function(12)

# def make_negative(number):
# return -abs(number)

# print("Number: {}".format(number))
# make_negative (45)

# def my_function(counter=89):
# print("Counter: {}".format(counter))

# my_function()

# print("My name is Gabriel and I come from Lira", sep='....')

# for i in [1, 2, 3, 4]:
# print(i, end=" ")

# a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
# print(a.get('projects')[3])

# for i in [1, 3, 4, 2]:
# print(i, end=" ")

# a = { 'id': 89, 'name': "John" }
# print(a['id'])

# for i in range(0, 3):
# print(i, end=" ")

# a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
# print(a.get('projects'))

# a = { 'id': 89, 'name': "John" }
# print(a.get('age'))


#num1, num2 = int(input("Enter the two numbers: ")).split()
#num1 = int(num1)
#num2 = int(num2)
#if num1 > num2:
#larger_number = num1
#else:
#larger_number = num2

# Print the result
#print("The larger number is:", larger_number)

def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s
print (list_sum([5,4,3]))