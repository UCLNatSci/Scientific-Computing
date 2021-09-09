#!/usr/bin/env python
# coding: utf-8

# # Tutorial 4: Lists and Plotting
# ## Lists
# A **list** is a Python data type that stores a sequence of values. For example, suppose we have the following data representing five years' population data for a species:

# In[1]:


populations = [12, 25, 54, 102, 206]
print(populations)


# Each element in a list has an **index** which identifies its position. We can access a list element by following the variable name with square brackets and the index:

# In[2]:


initial_pop = populations[0]
year_3_pop = populations[3]

print("Initial population:", initial_pop)
print("Population in year 3:", year_3_pop)


# Likewise, we can update individual list elements. Suppose we would like to change the value of the 3rd element:

# In[3]:


populations[3] = 100 # Assign the value 100 to element at index 3
print(populations)


# Any data type can be stored in a list, including strings:

# In[4]:


cities = ["Manchester", "Liverpool", "Sheffield", "Stoke-on-Trent"]
x = cities[2]
print(x)


# ---
# **NOTES**  
# - Lists are indexed starting from `0`. If a list has `n` elements, then the last element is at index `n - 1`.
# - Square brackets are used for two distinct purposes: for list creation: `x = [1, 2, 4]`, and list element access: `x[2]`.
# ---

# ## Traversing Lists
# There are two ways of accessing all elements of a list. The first way is to use a `for` loop to loop over all index values. We use the Python function `len` to determine the number of elements in the list.

# In[5]:


n = len(populations) # get the number of elements in the list
for i in range(n): # loop over index values 0 to n - 1
    pop = populations[i] # Access element at index i
    print("Year", i, "population:", pop)


# If you don't need index values, you can loop over the individual elements of the list:

# In[6]:


for pop in populations: # loop over all elements of the list
    print("Population:", pop)


# ## Appending Elements to a List
# After a list is created, we can add items to it using the `append` method. Suppose that we have recorded the species population for the next year as `420`:

# In[7]:


populations.append(420)
print(populations)


# A common pattern for list creation is to start with an empty list, then use a loop to append one element at a time. The following example creates a list of the first 10 square numbers.

# In[8]:


values = []
for i in range(10):
    values.append(i**2)
print(values)


# ## Finding a List Element
# If you want to know the index of an element in a list, use the `index` method. `string.index(s)` returns the first element equal to argument `s`:

# In[9]:


values = ["ABC", "DEF", "GHI", "JKL"]
i = values.index("GHI") # Find the index of the first element equal to "GHI"
print(i)


# ## Plotting using Matplotlib
# 
# Python does not include any in-built graph plotting capability. In order to plot graphs, we have to **import** a Python **package** called `matplotlib`. A package is a library of code which we can use to extend the capabilities of core Python, and is composed of individual code files called **modules**. Use the `import` statement to import the module `matplotlib.pyplot`:

# In[10]:


import matplotlib.pyplot as plt


# ---
# **NOTES**
# - The Python statement `import a` causes the Python package (or module) `a` to be imported. Any function defined in `a` is then available by typing '`a.`' followed by the function name.
# - `import a as b` gives `a` an alias (nickname) `b`, so that functions are available by typing '`b.`' followed by the function name. This is useful when `a` has a long name (such as `matplotlib.pyplot`).
# - Python includes built-in modules such as `sys` (system functions) and `os` (operating system functions) which can be imported in the same way.
# - Other packages are not part of Python itself but are pre-installed as part of a Python distribution (such as Anaconda or Cocalc). In this course we will use `matplotlib` and `numpy`.
# - There are many third-party modules available, which typically need to be downloaded and installed. Examples include `biopython` (for bioinformatics) and `pandas` (for data analysis).
# ---
# 
# Suppose we have collected the following data which we would like to plot on a line graph.
# 
# | Time (s)     | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 |
# |--------------|-----|-----|-----|-----|-----|-----|-----|
# | Distance (m) | 2.5 | 2.6 | 3.4 | 4.1 | 4.5 | 5.1 | 5.2 |
# 
# First, we create lists to store the data for each of the x-axis and y-axis:
# 

# In[11]:


time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
dis = [2.5, 2.6, 3.4, 4.1, 4.5, 5.1, 5.2]


# Then:
# - create a figure using the function `plt.figure`, passing in the dimensions in inches.
# - plot a line graph using `plt.plot`, passing in the two lists
# - add axis labels and a title using `plt.xlabel`, `plt.ylabel` and `plt.title`

# In[12]:


plt.figure(figsize=(4,4)) # create figure of size 4 by 4 inches
plt.plot(x, y) # plot a line graph
plt.xlabel("Time (s)") # add an x-axis label
plt.ylabel("Distance (m)") # add a y-axis label
plt.title("Particle Position") # add a figure title

