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