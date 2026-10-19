#Theory: Study Python lists, tuples, dictionaries, sets, functions, lambda functions, recursion, and list comprehension.

# List -->    List is mutable which means can be changed.It can perform function like Append(),Insert(),Remove

# 1.Creating and accessing list (All list store multiple value in on variable)
a = [2,4,6,8,10]
print(a)       #created

fruits =["Apple","Mango","Papaya","Watermelon"]
print(fruits[0])         #Accessing
print(fruits[1])
print(fruits[2])

#2. Indexing and Slicing
a = [2,4,6,8,10]                               #Indexing - Means getting one specific item
print(a[0])
print(a[3]) 

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])                            #Slicing - Means getting multiple items
print(numbers[ :4])                            #End is not included
print(numbers[-4:-1])                          #-1 start from last



#  3. append(), insert(), remove(), pop()

a = [2,4,6,8,10]
a.append(12)            # append
print(a)
print(type(a))

fruits =["Apple","Mango","Papaya","Watermelon"]
fruits.insert(1,"Melon") 
print(fruits)             #insert


fruits =["Apple","Mango","Papaya","Watermelon"]
fruits.remove("Mango") 
print(fruits)             #remove - Remove item by its value

fruits =["Apple","Mango","Papaya","Watermelon"]
fruits.pop(3)
print(fruits)             #pop - removes item by its index 


#Sort and Reverse
#sort- Sort numbers from smallest to largest

numbers =[50,10,40,20,30]
numbers.sort()
print(numbers)

numbers =[50,10,40,20,30]
numbers.sort(reverse=True)
print(numbers)

#Sorting strings
name = ["Jiya","Laiba","Bhavya","Samiksha"]
name.sort()

print(name)
#Tuple - Immutable means cannot change 

#1. Creating a Tuple

fruits =("apple","banana","citrus orange","guava")
print(fruits)

#2. Accessing a tuple
fruits =("apple","banana","citrus orange","guava")
print(fruits[0])
print(fruits[2])

#3. Slicing 

a = (10,20,30,40)
print(a[1:3])
print(a[:3])

#4.Immutable
a = (10,20,30,40)
#a.append(50)         #Not changable

#5. Tuple Methods (Tuples have fewer methods because you can't modify them)

#Count
a = (10,20,10,30,40,10)
print(a.count(10))

#index
a = (10,20,10,30,40,10)
print(a[2])

#6. Tuple Unpacking

student = ("Garvi",21,"Data Ethusiast")

name,age,career = student
print(name)
print(age)
print(student)


#Dictionary : Dictories store data as Key value pair.
student = {
    "name" : "Shivam",
    "age"  : 17,
    "roll no" : 32
}
# Accessing the value
print(student["name"])  #print(student.get('name'))
print(student["age"])
print(student["roll no"])

#Add value
student["city"] = "Delhi"
print(student["city"])

#Updating value
student["roll no"] = 43
print(student["roll no"])

#Remove item
student.pop("age")

del student['city']

# clear() Removes everything
student.clear()

#Dict Methods
#keys()
student = {
    "name" : "G",
    "age"  : 12,
}
print(student.keys())

#values 
print(student.values())

#items
print(student.items())

#Looping through dict
#Only Keys
for key in student:
    print(key)

#only values
for value in student.values():
    print(value)

#key and values
for key,values in student.items():
    print(key,value)

#Sets (A set is a collection of unique values.)
number = {10,20,30,40,20}
print(numbers)

#Set do not have index
#Loop 
for nummber in numbers:
    print(number)

#Add
number = {10,20,30,40,20}
number.add(40)
print(number)
#Remove
number = {10,20,30,40,20}
number.remove(20)
print(number)  #Error if 20 does not exist

#Discard
number = {10,20,30,40,20}
number.discard(50)
print(number)

#Pop
number = {10,20,30,40,20}
number.pop()
print(number)

#Set Operations
#Union - Cobines two Sets
a = {1,2,3}
b = {3,4,5}
c = a|b
print(c)

#Intersection 
a = {1,2,3}
b = {3,4,5}
c = a & b
print(c)
#difference 
print(a-b)
#Symmetric Difference
print(a^b)


# Functions
#Defining it (A function is a reusable block of code designed to perform a specific task.)

def greet(name):
    return f"Hello,{name} !"
print(greet("AI"))



def greet(name):
    print("Hello",name, "! Welcome.")

name = input("Enter Name :")
greet(name)
#Part	Meaning
#def	      Keyword used to define a function
#greet	      Function name
#()	          Parameters go here
#:	          Starts the function body
#Indented code	Function body


#Multiple parameters

#Greeting with name and age
def greet(name,age):
    print("Hello",name,"!")
    print("You are",age,"years old.")
    
name = input("Enter name :")
age = int(input("Enter your age :"))

greet(name,age)

#Default arguments (A default parameter is a parameter that already has a value. If the user doesn't provide a value, Python uses the default value.)

def greet(name="User"):
    print("hello",name)  #Simple Argument

greet()

#multiple argument with a default
def greet(name,message="Welcome"):
    print(message,name)

greet("Bhavana")

#Real World Example
def calculate_bill(price,tax=18):
    total = price + (price * tax/100)
    print("Total :",total)
    
calculate_bill(1000)


#Local vs global variables
#*args
#**kwargs

#Lambda functions - It is a small anonymous function written in one line

#Syntax : lambda arguments: expression
double = lambda x: x*2  #one argument
print(double(10))

#add
add = lambda a,b: a+b
print(add(10,20))

#Multiple arguments
calculate = lambda a,b,c:a+b+c
print(calculate(10,20,30))

#Lambda with if-else
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(10))
print(check(7))

#2. Strings
#Indexing & slicing
names =('Riya','Priya','Shreya','Anu')
print(names[0])

#upper(), lower(), capitalize()
#strip()
#replace()
#split()
#join()
#find()
#count()
#startswith() / endswith()
#f-strings
#String formatting

#Recursion - Function calling itself
def hello():             #Example
    print('Hello')
hello()

#Printing no from 5 down to 1
def countdown(n):
    if n ==0:
        return
    print(n)
    countdown(n-1)
countdown(5)

#Factorial  n! =n*(n-1)!
def factorial(n):
    if n == 1:
        return 1

    return n*factorial(n-1)
print(factorial(5))

#Fibonacci

#List comprehension
numbers = [1, 2, 3, 4, 5]

squares = []

for n in numbers:
    squares.append(n * n)

print(squares)