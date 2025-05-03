import math
import time
# Exercise Rectangle Area Calculator 
'''
length = float(input("Enter the Length in cm: "))
width = float(input("Enter the Width in cm: "))

area = length * width

print(f"The Area of the Rectangle is {length} x {width} = {area}cm²")
'''
# Exercise Shopping Cart 
''' 
item = input("What would you like to buy? ")
quantity = int(input("How many are you buying? "))
price = float(input("What is the price? "))
total = quantity * price

print("\nPurchase Details")
print(item)
print(price)
print(f"x   {quantity}")
print("---------------")
print(f"Total Php {total}")
'''
# Madlibs
'''
print("MADLIBS!!")
person1 = input("\nEnter a Name: ")
animal = input("Enter an Animal: ")
verb = input("Enter a Verb: ")
adjective1 = input("Enter an Adjective: ")
adjective2 = input("Enter another Adjective: ")

print(f"\nI saw {person1} doing backflips")
print(f"Then a flying {animal} appeared")
print(f"He was {verb}ed by the {animal}")
print(f"It was {adjective1} and I was {adjective2}")
print("Great Story!!")'
'''
# Circumference of a Circle
'''
radius = float(input("Enter Radius: "))
circumference = 2 * math.pi * radius
print(f"circumference = 2 x {round(math.pi, 2)} x {radius}")
print(f"The Circumference is {round(circumference, 2)}")
'''
# Area of a Circle
'''
radius = float(input("Enter Radius: "))
area = math.pi * pow(radius, 2)
print(f"area = {round(math.pi, 2)} x {radius}²")
print(f"The Area is {round(area, 2)}")
'''
# Basic Calculator
'''
operator = input("Choose an Operator (+ - * / pow): ")
num1 = float(input("Enter 1st Number or Base Number(for pow): "))
num2 = float(input("Enter 2nd Number or Exponent (for pow): "))

if operator == "+":
    result = num1 + num2
    print(f"Result: {round(result, 2)}")
elif operator == "-":
    if num1 <= num2:
        result = num2- num1
        print(f"Result: {round(result, 2)}")
    else:
        result = num1 - num2
        print(f"Result: {round(result, 2)}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {round(result, 2)}")
elif operator == "/":
    result = num1 / num2
    print(f"Result: {round(result, 2)}")
elif operator == "pow":
    result = pow(num1,num2)
    print(f"Result: {round(result, 2)}")
else:
    print(f"{operator} is an Invalid Operator!!!")
'''
'''
name = input("Enter Name: ")
result = len(name)
find = name.find("l")

print(f"{name} \n{result}\n{find}")
'''
'''
grade = float(input("Enter Your Grade: "))

while grade < 0:  
    print("Enter a Grade")

grade = float(input("Enter Your Grade: "))
print(f"Your Grade is {grade}")

grade_status = "Passed" if grade >= 75 else "Failed"
print(grade_status)
'''
my_Time = int(input("Enter the Time in seconds: "))
              
for counter in range(my_Time, 0, -1):
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600) 
    print(f"Time Left: {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("⏲️⏲️Perdi Gyapon Si Jene👍⏲️⏲️")
