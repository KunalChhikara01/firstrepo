#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Name - Kunal Chhikara, Student id - 201526146 
# Program to find an inverse of a random permutation matrix using a nested loop.


A = [[0,1,0,0,0],
     [0,0,1,0,0],
     [0,0,0,1,0],
     [0,0,0,0,1],
     [1,0,0,0,0]]


Result = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]


# Iterate through rows

for i in range(len(A)):
   
   for j in range(len(X[0])):         # iterate through columns
       Result[j][i] = A[i][j]

for r in Result:
   print(r)

