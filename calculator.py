import os 
import subprocess
import time
print("***********************")
print("Basic Calculator")
print("***********************")

print("Addition: + ",
      "Subtraction: - ",
      "Multiplication: * ",
      "Division: / ")

operator = ""

command = 'cls' if os.name == 'nt' else 'clear'

while True:
    try:
        operator = input("Pick an operator  (+, -, *, /) or 'q' to quit:  ")

        if operator.lower() == 'q':
            print("Goodbye.")
            break
        
        if operator not in ["+", "-", "*", "/"]:
            raise ValueError("Invalid operator")
        
        num_1 = int(input("Enter 1st number: "))    
        num_2 = int(input("Enter 2nd number: "))

        if operator == "+":
            result = num_1 + num_2
            print(f"The sum of {num_1} and {num_2} is {result}")
            time.sleep(1)
            subprocess.run(command, shell=True)

        elif operator == "-":
            result = num_1 - num_2
            print(f"The difference of {num_1} and {num_2} is {result}")
            time.sleep(1)
            subprocess.run(command, shell=True)
            
        elif operator == "*":
            result = num_1 * num_2
            print(f"The product of {num_1} and {num_2} is {result}")
            time.sleep(1)
            subprocess.run(command, shell=True)
            
        elif operator == "/":
            if num_2 == 0:
                raise ZeroDivisionError("Cannot Divide by Zero")
            else:
                result = num_1 / num_2
                print(f"The quotient of {num_1} and {num_2} is {result}")
                time.sleep(1)
                subprocess.run(command, shell=True)
                
    except ValueError as ve:
        print(f"Error: {ve}")
        time.sleep(1)
        subprocess.run(command, shell=True)
    
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        time.sleep(1)
        subprocess.run(command, shell=True)
    
    except Exception as e:
        print(f"Unexpected Error: {e}")
        time.sleep(1)
        subprocess.run(command, shell=True)
