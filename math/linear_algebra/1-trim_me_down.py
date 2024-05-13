#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []  # Initialize the_middle list
for row in matrix:  # Iterate through each row in matrix
    the_middle.append([row[2], row[3]])  # Append the 3rd and 4th 
print("The middle columns of the matrix are: {}".format(the_middle)) 
