def mean(*args):
    return sum(args) / len(args)


print(mean(1,2,3,4,6,7))

def mean(**kwargs):
    return kwargs


print(mean(a=1,b=2,c=3,d=4,e=6))