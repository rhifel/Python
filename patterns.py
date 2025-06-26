

'''
# Triangle
rows = int(input("Enter Number of Rows: "))

for i in range(1, rows, +1):
    print(" " * (rows - i) + "* " * i)
'''
    
'''
# Diamond
rows = int(input("Enter Number of Rows: "))

for i in range(1, rows, +1): # upper part 
    print(" " * (rows - i) + "# " * i)

for j in range(rows, 0, -1): # lower part
    print(" " * (rows - j) + "# " * j)
'''

'''
# Checkerboard
rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter Number of Columns: "))

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
'''
for i in range(3):
    for j in range(3):
        print(i, j)
        