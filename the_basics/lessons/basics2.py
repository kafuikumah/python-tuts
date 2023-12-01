# FOR LOOPS - HOW AND WHY
monday_temperatures = [9.1, 8.8, 7.5 ] 

for temperature in monday_temperatures:
    print(round(temperature))
print('Temperatures Done')

for letter in 'hello':
    print(letter)
    print(letter.upper())
    print(letter.title())

# LOOPING THROUGH A DICTIONARY
student_grades = {"Mary": 9.1, "Sam": 8.8, "Jon": 7.5}

for grades in student_grades.items(): #Prints out the whole dictionary
    print(grades)

for grades in student_grades.keys(): #Prints out ONLY the keys
    print(grades)

for grades in student_grades.values(): #Prints out ONLY the values
    print(grades)



# WHILE LOOPS - HOW AND WHY
a = 3

while a > 0:
    print(1)
    print(2)
#While a>0, it will continue to print 1 or 2 because a is a value which is greater than 1. that value is 3.
# if the varible a were dynamic, 1 and 2 will keep printing untill the value of a changes.

