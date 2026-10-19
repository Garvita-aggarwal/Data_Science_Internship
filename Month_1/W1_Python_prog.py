#Theory: Study Python variables, data types, operators, input/output, conditional statements (if-else), loops (for, while).
## Week 1: Introduction to Python Programming

# Variables (Used to store values)

name = "Yashu" 
age  =  22
weight = 62.0 


# Datatypes

name = "Yashu" #String
age  =  22     # Int = Only whole nummbers
weight = 62.0  # Boolean = whole no + decimals

# operators
print(5*2)  # Multiply
print(5/2)  # Divide
print(5//2) # Floor
print(5%2)  # Modulus     (Arithmetic)

a = "4"
b = 4
if a == b:               # Comparison check
    print("Ok") 
else:
     print ("Inalid")

a = "Heema"
print(a)                 # Assigmment Operator


a = 22
print(a<30 and a>18)      # Logical operator (and = Both condition must be true)

a = 22
print(a<30 or a>18)      #  (OR = Either of the condition must be true)

a = 22
if a<30 or a>18:
    print(not True)


#5. Identity Operators ( Used to check whether two variables refer to the same object.)

a =[10,11,12]
b = a
print(a is b)  # a== b  -Value object  # a is b -same Object 

#7. Bitwise Operators (These work at the binary/bit level.)
# & , |, XOR , NOT , Left shift  5<<1 , Right Shift 5>>1 


# Input/output
name = input("Enter name : ");

print("Name :",name);

#conditional statements (if-else)

a = input("Enter a:")
b = input("Enter b:")
if(a > b):
    print(a)
else:
    print(b)


#  loops (for, while).
# To print "Ganpati Bappa Moriyaa"
n = 5
for i in range(5):
    print("Ganpati Bappa Moriyaa")

i=0
while i<5:
    print("Ganpati Bappa Moriyaa 2")
    i = i + 1



# Temp Calculator

temp = float(input("Enter temperature: "))
unit = input("Enter Unit(C/F):").upper()

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print("Fahrenheit: ",fahrenheit)

elif unit =="F":
    celsius = (temp - 32) * 5/9
    print("Celsius :",celsius)

else:
    print("Invalid unit")


