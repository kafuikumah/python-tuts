# Open the file
myfile = open("/files/fruits.txt")
# Read the file and save content
content = myfile.read()
# Close the file
myfile.close() 
#you cannot read a file after closing it. you need to open again before you close it
print(content)


# HOWEVER, THERE IS A BETTER WAY (using "with" keyword)

with open("./files/fruits.txt") as myfile:
    content = myfile.read()
    # Closing the file is not necessary because the with keyword closes it automatically

print(content)


# WRITING TEXT TO A FILE "w" - Overwrites
with open("./files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nCarrot\n")
    myfile.write("Lettuce\nOnion")

# APPENDING TEXT TO A FILE "a" - Appends
with open("the_basics/files/vegetables.txt", "a") as myfile:
    myfile.write("\nOkra")


# APPEND AND READ AT THE SAME TIME "a+"
with open("the_basics/files/vegetables.txt", "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()

print(content)