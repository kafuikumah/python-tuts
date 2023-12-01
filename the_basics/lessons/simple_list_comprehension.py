# FOR LOOPS CONTINUATION - LIST COMPREHENSIONS

# Companies have techniques to save data. one is to remove decimals from values if the values are a set of temperatures
# So what we will do is to divide the values in the list by 10, so that we can get the actual value, instead of the stored value



temps = [221, 234, 340, 230]

new_temps = []

for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)


# THAT IS GREAT, BUT THERE IS A NEATER WAY TO DO THIS IN PYTHON

actual_temp = [temp / 10 for temp in temps]

print(actual_temp)