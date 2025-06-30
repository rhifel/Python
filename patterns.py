

'''
# Triangle
rows = int(input("Enter Number of Rows: "))

for i in range(1, rows,):
    print(" " * (rows - i) + "* " * i)
'''
    
'''
# Diamond
rows = int(input("Enter Number of Rows: "))

for i in range(1, rows): # upper part 
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
'''
# 6 x 7 matrix heart shape
for row in range(6):
		for col in range(7):
			if (row == 0 and (col%3 != 0)) or (row == 1 and (col%3 ==0)) or ((row - col == 2)) or ((row + col == 8)):
				print("*",end="")
			else:
				print(" ",end="")
		print()	
'''

# trying to create another solution for the heart pattern
rows = int(input("Enter Number of Rows: "))

for i in range(2, rows + 1):
    
    left_t = (" " * (rows - i) + "* " * i)
    
    right_t = (" " * ((rows - i) * 2) + "* " * i)
    
    print("" + left_t + "" + right_t)
    
rows_dbl = 2 * rows 

for i in range(rows_dbl, 0, -1):
    
    print(" " * (rows_dbl - i) + "* " * i)