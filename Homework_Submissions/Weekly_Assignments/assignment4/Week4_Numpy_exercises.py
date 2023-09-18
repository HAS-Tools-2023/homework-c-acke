#%%
# This script contains exercises on 
# manipulating arrays with numpy
import numpy as np


# %% Exercise 1: Working with a 1-D array:
x = np.arange(0, 3**3)

# 1.1 What is the length of x?
print(len(x))
#27

# Comprehension question is this an attribute or a method or a function of x? How do we know?
#This is an attribute of x because this describes the length of x, which is a characteristic
#%%
# 1.2 Get the first value out of x and print it: 
print(x[0])
#%%
# 1.3. Get the last value out of x and print it?
print(x[-1])
#%%
# 1.4. Get the first 5 values and last 5 values out of x and print them?
print(x[0:5])

print(x[22:27])

#%%
# %% Exercise 2: Working with a 2-D array:
# 2.1 Get the first 9 values of x, and reshape them to a
#    3x3 matrix. Assign this matrix to the variable `y`
y = None
print(y)

#BONUS show how you can do this with two lines of code and how you can do it with one line of code. 
y = np.arange(9).reshape(3, 3)

##Comprehension question: Is reshape a function, a method or an attribute of y?  How do we know? 
#Reshape is a function, this is something that python is asked to do in order to create a different output

#%%
# 2.2 Get the middle value out of y and print it?
y = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
])

print(y[1,1])
#%%
# 2.3. Get the first row out of y and print it?
print(y[0])
# %%
# 2.4 If you save the first row of y to a new variable w what type of object is w? 
w = y[0]
#This would be an array with 3 values
#%%
# 2.5 Get the first column out of y and print the lenght of this colum? (hint you will need to use the attribute 'size' to do this)
print(np.size(w))
# BONUS: Try doing this two different ways. First where you save the column as a new variable and then get its size (i.e. with two lines of code). And next where you combine thos commands into one line of code

#%% Exercise 3 Creating numpy arrays: 

# %%
# 3.1 use the np.arange function and the reshape method to create a numpy array with 3 rows and two columns that has values 0-9
print(np.arange(9).reshape(3,3))
# %%
# 3.2 use the np.ones function to create a 4 by 4 matrix with all ones 
print(np.ones((4,4)))
# %% 
# 3.3 Now modify the matrix you created in the last exercise to make the values all 4's   (Hint: you could do this with either addition or multiplication)
z2 = np.ones((4,4))
z1 = np.array([[3,3,3,3],[3,3,3,3],[3,3,3,3],[3,3,3,3],])
print(np.add(z2, z1))
#%% Exercise 4:  using the axis argument
z=np.arange(20).reshape((5,4))

# 4.1 Use 'sum' to print the total of z
print(sum(z))
#Comprehension question -- is 'sum' a function a method or an attribute?  
#Sum is a function because it's built in to Python 
#%%
# 4.2. Print the sum along the first dimension of z?
print(sum(z[0:1]))
print(np.shape(z))
## Comprehension question -- is the 'first dimension' the rows or the columns of z? 
#It is the first row of z

# %% 
# 4.3 How many elements does your answer to exercise 4.2 have? (i.e. how many numberd did you get back?)
#I got back 4 

# How does this compare to the shape of z? 
#This makes sense because there are four columns when referring to the shape, so it would read the first value of each column
