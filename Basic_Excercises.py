"""the following set of exercises to practice this beautiful language
and make some experiments to learn the process
"""
##Conditions: skills

"""
even_number = int(input("Plase, enter a even number \n"))
odd_number = int(input("Plase, enter a odd number  \n"))
if even_number > odd_number:
    print(even_number ," is greater than ", odd_number)
elif even_number == odd_number:
    print( even_number, " and ", odd_number , "are equals")
else:
    print(even_number , " is less than  ",odd_number)
"""

""" Collections:

List: is a collection which is ordered and changeable. Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
Set: is a collection which is unordered and unindexed. No duplicate members.
Dictionary: is a collection which is unordered, changeable and indexed. No duplicate members.

"""
fruits = ["Apple", "Orange", "Banana", "Coconus"]
print(fruits)
fruits.append(1);
fruits.append("Watermelon");
fruits.insert(2,"Coconus");
fruits.pop(0);

##Print Each value from the List
for x in fruits:
    print(x)


print("Size of List with Len", len(fruits))
print("Size of List with count (Cococnus in list)", fruits.count("Coconus"))

fruits.clear();

print("Size of List after remove it", len(fruits))

#Dictionaries:

dictionary = {
    "age": 29,
    "name": "Diego Babativa",
    "employee": "Software Engineer"
    }

print("Printing Dictionary: " , dictionary)
print("Getting ítem by key: " , dictionary.get("name"))

print("Printing all values: ", )
for x in dictionary.values():
    print(x)


#Mutiple else statements on the samen line

a = 12; b = 2;
print("A") if a > b else print("=") if a==b else print("B")

#And & or conditionals:
print("Even number less than 10") if a%2==0 and a<10 else print("Don´t passed")


#while Loops

i=0;
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    if i > 3:
        break
    

#For loop
print("Printing the For loop *****************")
for x in range(0,10,3):
    print(x)


#Functions
print("Functions:")

def squareThisNumber(number):
    return number^2


print(squareThisNumber(2))


#Recursion functions:
#--------------------
def tri_recursion(k):
    if(k)>0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
       result=0
    return result
        
#--------------------
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#++++++++++++++++++++
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return n *factorial(n-1)
    

print("Calling Python recursion : tri_recursion function(6)...")
tri_recursion(6)

print("Calling Python recursion : fibonacci function(6)...")
print(fibonacci(6))

print("Calling Python recursion : factorial  function(5)...")
print(factorial(5))



#LAMBDA FUNCITONS

x = lambda a, b, c : a*b*c

print("Printing Lambda...", x(2,3,4))


##Classes and Objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is" , self.name, " and I am " , self.age, "years old")

p1= Person("Diego", 29)
p1.myfunc()











