import pandas as pd
import numpy as np
import urllib
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression

#%%
### Exercise 1: 
# Given the following dataframe:
data = np.random.rand(4, 5)

# Write a function and use it to calculate the mean of every colum of the dataframe
# If you have time try doing it with and without a for loop (You can either use the function inside your fo loop or put a for loop inside your function)
def mean_columns(array):
    calc_mean = np.mean(data, axis = 0)
    return(calc_mean)

mean_columns(data)

def average_columns(array):
    ncol = array.shape[1]
    col_mean = np.zeros(5)
    for i in range(ncol):
        col_mean[i] = np.mean(array[:, i])
    return(col_mean)

average_columns(data)

def take_mean(some_numbers):
    mean_number = np.mean(some_numbers)
    return(mean_number)

mean_columns = np.zeros(5)

for i in range(data.shape[1]):
    mean_columns[i] = take_mean(data[:, i])


#%% Exercise two: regression analysis
# For this exercise we will work with the
# iris dataset which is a classic and very easy
# multi-class classification dataset. 
# This dataset comes with the sklearn pacakge so we can just load it in directly. 
# It describes measurements of sepal & petal width/length for three different species of iris
d = datasets.load_iris()
iris_df = pd.DataFrame(d['data'], columns=d['feature_names'])
iris_df.index = pd.Series(
    pd.Categorical.from_codes(d.target, d.target_names),
    name='species'
)
iris_df.head()

# %%
# 1. How do you view the "unique" species in the `iris_df` index?
#hint: use the function np.unique() and apply it to the index of the dataframe
unique = np.unique(iris_df.index)

# %%
# 2. How do you "locate" only rows for the `versicolor` species?
#hint: use .loc to the rows that have the name 'versicolor'
versicolor_only = iris_df.loc['versicolor', :]

# %%
# 3. Calculate the mean for every column of the dataframe grouped by species. 
#hint: use groupby.mean(), look back at our pandas examples
mean_species = iris_df.groupby(iris_df.index).mean()

# %%
# 4. Make a scatter plot of the `sepal length (cm)` versus the `petal length (cm)` for the `versicolor`` species?
#hint: first grab out just the rows you want to plot
#then use the scatter function to plot those columns (in plotting notes if needed)
plt.scatter(versicolor_only['sepal length (cm)'], versicolor_only['petal length (cm)'])
plt.title('Versicolor Sepal Length vs Petal Length')
plt.ylabel('Petal length (cm)')
plt.xlabel('Sepal length (cm)')


# 5.  Do the same plot for `setosa` and `virginica` all on the same figure. Color them 'tomato', 'darkcyan', and 'darkviolet', respectively. (BONUS: Try to write the code so you only need to type each iris name one time)
#repeat what you did in 4 three more times
plt.scatter(versicolor_only['sepal length (cm)'], versicolor_only['petal length (cm)'], color = 'tomato')
plt.scatter((iris_df.loc['setosa', 'sepal length (cm)']), iris_df.loc['setosa', 'petal length (cm)'], color = 'darkcyan')
plt.scatter((iris_df.loc['virginica', 'sepal length (cm)']), iris_df.loc['virginica', 'petal length (cm)'], color = 'darkviolet')
plt.title('Species Sepal Length vs Petal Length')
plt.ylabel('Petal length (cm)')
plt.xlabel('Sepal length (cm)')


# 6. Write a function that will do 'ax.scatter' for a given iris type and desired color of points and use this to function to modify the code you make in 5
#hint: no for loop needed, function should have two arguments and you will call it 3 times
#copy code from 5 down here and replace your ax.scatter calls with your function





