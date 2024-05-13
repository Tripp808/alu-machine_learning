#!/usr/bin/env python3
matrix=[[1,3,9,4,5,8],[2,4,7,3,4,0],[0,3,4,6,1,5]]
the_middle=[]#Initializethe_middlelist
for row in matrix:#Iteratethrougheachrowinmatrix
the_middle.append([row[2],row[3]])#Appendthe3rdand4th
print("Themiddlecolumnsofthematrixare:{}".format(the_middle))
