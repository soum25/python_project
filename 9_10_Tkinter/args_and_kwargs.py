def add(*args):
    print(args[5])
    a = 0
    for n in args:
        a += n
    return a


print(add(14, 45, 74, 4, 5, 7))


def calculate(n,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
    n *= kwargs["a"]
    n += kwargs["b"]
    print(n)


calculate(2,a=3, b=5)

class Car():
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


bmw = Car(make="toyota",model="Gt-r")
print(bmw.make)
print(bmw.model)
