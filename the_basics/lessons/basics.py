import datetime
#  VARIABLES
myntimenow = datetime.datetime.now()
print(myntimenow)


# SIMPLE TYPES, INTEGERS, STRINGS AND FLOATS
x = 10
y = '10'
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

# LIST TYPES - mutable, meaning you can add/append items
student_grades = [9.1, 8.8, 7.5 ]

mysum = sum(student_grades)
length = len(student_grades)

mean = mysum / length
print("The mean of student grades list is:", mean)


# DICTIONARIES
student_grades = {"Mary": 9.1, "Sam": 8.8, "Jon": 7.5}
student_names = student_grades.keys()
print(student_names)

mysum = sum(student_grades.values())
length = len(student_grades)

mean = mysum / length
print("The mean of student grades dictionary is:", mean)


# TUPLES - non-mutable meaning you cannot add/append new values
monday_temperatures = (1, 4, 5)
print(monday_temperatures)


# FUCNTIONS

def mean(mylist):
    print("Function Started")
    the_mean = sum(mylist) /len(mylist)
    return the_mean #if your function does not have a return statement, python always returns None

# fxn is ONLY executed when it is called somewhere else with its required parameters
mymean = mean([1, 4, 6])
print(mymean + 10)
print(type(mean), type(sum))



# CONDIDTIONALS : IF... instead of using lists, we're going to use dictionaries. this is because
# a dictionary has a key: value pairing so the function can specifically pick the values of the dictionary
# and then leave out the key.
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value.values())
    else:
        the_mean = sum(value) /len(value)

    return the_mean


student_grades = {"Mary": 9.1, "Sam": 8.8, "Jon": 7.5}
monday_temperatures = (1, 4, 5) 

print("Your Mean Calculation is:")
print(mean(student_grades))


# CONDITIONALS REQUIRING USER INPUT
def weather_conditions(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
    
user_input = float(input("Enter Temperature Today: "))

print(weather_conditions(user_input))
print(type(user_input), user_input)


# STRING FORMATTING
user_input = input("Enter your name:")
message1 = "Hello %s!" %user_input #old method. python 2 and 3
message = f"Hello {user_input}!" # new method. used for python 3.6 and above

print(message)

# STRING FORMATTING WITH MULTIPLE VARIABLES
firstname = input("Enter your First name:")
surname = input("Enter your Surname:")
when = "today"

message2 = "Hello %s %s!" %(firstname, surname) #old method. python 2 and 3
message3 = f"Hello {firstname} {surname}! What's up {when}?" # new method. used for python 3.6 and above

print(message2)
print(message3)


