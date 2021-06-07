# optional parameters :

def func(x=1):
    return x**2

call = func()
recall = func(5)
print(call);print(recall)






# statics and class methods :

class Person(object):
    population = 50
    def __init__(self,name , age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    @staticmethod
    def display(self):
        print(self.name,"is",self.age,"years old")

print(Person.getPopulation())
t = Person("javad",19)
print(Person.getPopulation())






# lambda function :

def func2(x):
    return x+5

print(func2(2))

func3 = lambda x : x+5
print(func3(2))

func4 = lambda x,y=4 : x+y
print(func4(3))






# collections and counter :
import collections
from collections import Counter

c = Counter("gallad")
print(c)
c = Counter(["a","b","c","c","c"])
print(c)
c = Counter({"a":1,"b":2})
print(c)
c = Counter(cats = 4 , dogs = 5)
print(c)
print(c["dogs"])

print(list(c.elements()))

c = Counter(a=4,b=5,c=6,d=7)
d = ["a","b","b","c"]
c.subtract(d)
print(c)
c.clear()
print(c)

# c+d sum counters
# c-d counters
# c & d min of each others
# c | d max of each others





# namedtuple() :
from collections import namedtuple

point = namedtuple("point","x y z")
p1 = point(3,4,5)
print(p1)
print(p1.x , p1.y , p1.z)
print(p1[2])
print(p1._asdict())
print(p1._fields)

p1 = p1._replace(y=6)
print(p1)




# deque :
from collections import deque

d = deque("hello")
print(d)

d.append("4")
d.append(5)
print(d)
d.appendleft(5)
print(d)
d.pop()
d.popleft()
print(d)
d.clear()
print(d)

d.extend("123123")
d.extendleft("hellowwowo")
print(d)
d.rotate(2)
print(d)
