# LIST COMPREHENSION WITH IF CONDITIONALS
# In this excercise, we want to make sure not to include or compute special values within lists so we use if conditionals

temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps) 