
def area(a, b):
    return a * b

print(area(4, 5))
print(area(a=4, b=5))
print(area(b=4, a=5))


def area(a, b=7):
    return a * b

print(area(4)) #passed parameter is for a
print(area(a=4, b=5)) # b=5 overwrites b=7

