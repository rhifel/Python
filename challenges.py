#Hackerrank Challenges
'''
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints
1 <= n <= 100
Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

'''

#Problem 1
n = int(input().strip())
if not n % 2 == 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5: 
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

'''
Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Example
a = 3
b = 5
Print the following:
8
-2
15
Input Format
The first line contains the first integer, .
The second line contains the second integer, .
Constraints
1 <= a <= 10^10
1 <= b <= 10^10
Output Format
Print the three lines as explained above.
'''
#Problem 2
a = int(input())
b = int(input())
sums = a + b
diff = a - b
product = a * b
    
print(sums)
print(diff)
print(product)

'''
Add logic to print two lines. The first line should contain the result of integer division, a//b. 
The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.
'''
#Problem 3
a = int(input())
b = int(input())
div = a / b
div1 = a // b
print(div1) 
print(div)

'''
Task
The provided code stub reads an integer, , from STDIN. 
For all non-negative integers , print i^2 .
Example
n = 3
The list of non-negative integers that are less than n = 3 is [0,1,2]. 
Print the square of each number on a separate line.
'''
#Problem 4
n = int(input())
for i in range(n):
    print(i * i)

'''
Given a year, determine whether it is a leap year. 
If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. 
It is only necessary to complete the is_leap function.
'''
#Problem 5
def is_leap(year):
    leap = False
    if year % 4 == 0:
         if year % 100 != 0 or year % 400 == 0 :
            leap = True
    return leap

year = int(input())
print(is_leap(year))

'''
The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
Note that "" represents the consecutive values in between.
'''
#Problem 6
n = int(input())
for i in range(1, n+1):
    print(i, end="")

'''
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
Hello firstname lastname! You just delved into python.
Function Description
Complete the print_full_name function in the editor below.
print_full_name has the following parameters:
string first: the first name
string last: the last name
'''
#Problem 7
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    print_full_name()
'''
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns:
string: the resulting string
'''
def split_and_join(line):
    # write your code here
    
    a = line.split(" ")
    #print(a)
    
    b = "-".join(a)
    #print(b)
    
if __name__ == '__main__':

    #split_and_join("this is a string")
    line = input()
    result = split_and_join(line)
    print()
    
    
