#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Functions and Loops
# 
# ```{admonition} What you'll learn
#  - How to split up a problem into smaller parts using functions
#  - How to define and call functions
#  - How to test functions
#  - How to repeat code using `while` and `for` loops
#  - Relational operators
#  - Boolean variables
# ```
# 
# ## Functions
# 
# A function is a group of related statements that performs a specific task. With the help of functions, we can break our program into smaller and modular chunks. So, as we start to write larger programs, functions help us to make it more organized and manageable.
# 
# Furthermore, with the help of function, we can avoid repetition and make our code reusable. Let's start with a very simple example.
# 
# The following code sets the variable `name1` then prints a simple greeting message:

# In[1]:


name1 = "Prof Thomas"
print("Hello",  name1)
print("Nice to meet you.")


# Suppose we would like to print similar greeting messages for each of the variables `name1`, `name2` and `name3`. It is of course possible to do this by simply repeating the code three times:

# In[2]:


name1 = "Prof Thomas"
name2 = "Mr Bentham"
name3 = "Prof Lonsdale"

print("Hello",  name1)
print("Nice to meet you.")
print("Hello",  name2)
print("Nice to meet you.")
print("Hello",  name3)
print("Nice to meet you.")


# However, instead of repeating the identical code three times, we can write a Python **function**, a named sequence of instructions. In the code below, we define a function called `greet`. We then call the function three times, passing in each of our three variables `name1`, `name2` and `name3`.

# In[3]:


def greet(name):
    print("Hello ", name)
    print("Nice to meet you.")
    
greet("Prof Thomas")
greet("Mr Bentham")
greet("Prof Lonsdale")


# Let's examine what the Python interpreter does when it executes the above code.
# 
# - First, it reads the line `def greet(name):`. When Python reaches this line, it doesn't actually execute any of the code within this block. Instead, it skips to the next line of code below the function, in this case the line `greet("Prof Thomas")`.
# 
# - At this point, it recognises that `greet` is a previously defined function. Execution now moves to first line of the `greet` function, with the parameter variable `name` set to `"Prof Thomas"`.
# 
# - Python executes each line of code in the function in order.
# 
# - Once the interpreter reaches the final line of code in the function, execution returns to the main body of code and the line `greet("Mr Bentham")` is executed. Execution moves to the `greet` function with `name = "Mr Bentham"`, and execution continues as described above.

# ## Defining Functions
# 
# In this section, we will implement a function with a given specification, and call it with some test inputs.  
# 
# Suppose we want to define a function which computes the perimeter of a rectangle with given length and width. We need to do the following:
# 
# 1. Choose a name for the function (`calculate_perimeter`)
# 2. Define a variable for each argument (`length` and `width`). These are called **parameter variables**
# 3. Put these together with the keyword `def` and a colon (`:`)
# 
# ```
# def calculate_perimeter(length, width):
# ```
# 4. Specify the **body** of the function, which consists of statements which will run when the function is called. The perimeter of a rectangle is twice the length plus the width.
# 5. Finally we use the `return` statement to return the result of the function.
# 
# ```
# def calculate_perimeter(length, width):
#     perimeter = 2 * (length + width)
#     return perimeter
# ```
# 
# :::{note}
# - The body of the function is indented by 4 spaces
# - Nothing appears to happen when we run this code on its own - because we haven't called the function yet
# - The `perimeter` variable, defined inside the function, is not accessible outside the function
# - The `return` keyword is optional
# :::

# ## Calling Functions
# 
# If you run the preceding code nothing happens. In order to test the function, we need to write some statements that call the function and print the result.

# In[4]:


def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter
    

x1 = calculate_perimeter(2, 4)
x2 = calculate_perimeter(10, 10)

print("Rectangle 1 perimeter:", x1)
print("Rectangle 2 perimeter:", x2)


# Because the `calculate perimeter` function returns a number, we can use the function call in place of a numeric variable. For example, to print the total perimeter of two rectangles:

# In[5]:


print("Total perimeter of rectangles:", calculate_perimeter(2, 4) +  calculate_perimeter(10, 10))


# In[ ]:





# :::{note}
# The function definition must precede any statements which call it
# :::
# 
# :::{warning}
# The following function contains a common error: trying to modify an argument.
# ```
# def add_four(x):
#     x = x + 4 # Has no effect outside the function.
#     return x
# 
# x = 10
# add_four(x)  # Does not modify x.
# x = add_four(x)
# print(x)
# ```
# :::

# ## Example: Splitting a problem into parts
# 
# Consider following problem:
# 
# Given a number `n` between 1 and 365, print the day of the week, given 1st January is a Monday.  
# 
# We can split this into two problems:  
# 1. Given `n` from 1 to 365, calculate a number between 0 and 6 identifying the day of the week
# 2. Given a number between 0 and 6, determine the day of the week in text form (Monday, Tuesday, etc.)
# 
# We can write two functions each of which performs one of these steps, then chain them together.  
# 
# The first function, `get_number_of_day`, returns a number between 0 and 6 given a number `n` from 1 to 365:

# In[6]:


def get_number_of_day(n):
    d = n % 7
    return n


# The second function, `get_day_of_week`, returns a string given a number between 0 and 6:

# In[7]:


def get_day_of_week(n):
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return week_days[n]


# Finally, we write a function `get_day_of_week_from_number_of_year` which takes a number between 1 and 365 and prints the day of the week:

# In[8]:


def get_day_of_week_from_number_of_year(n):
    d = get_number_of_day(n)
    s = get_day_of_week(d)
    return s


# Now we can test it:

# In[9]:


day = get_day_of_week_from_number_of_year(1)
print(day)


# Wait! It didn't work: the answer should be `Monday`. Let's investigate. First, let's check the function `get_day_of_week`. Given the value 0, it should return `Monday`:

# In[10]:


get_day_of_week(0)


# So that's working OK. Let's test `get_number_of_day`. Since the 1st day of the year is a Monday, `get_number_of_day(1)` should return 0:

# In[11]:


get_number_of_day(1)


# Aha! We forgot to subtract 1 to change from 1-based indexing to 0-based indexing. In one of the practice exercises, you will fix the error.
# 
# ## Testing Functions
# 
# By splitting the problem into small functions, we were able to test each part separately, and easily identify where the error was. This is one of the key benefits of using functions.
# 
# A common techniques is called test-first development, where the tests are written *before* writing the function. 
# 
# ```
# def highest_common_factor(a, b):
#     # replace this line with the function contents
#     pass
#     
# # should print 3
# print(highest_common_factor(6, 3))
# 
# # should print 5
# print(highest_common_factor(5, 5))
# ```
# 

# ## Loops
# 
# A **loop** is a sequence of instructions which is executed repeatedly until a goal is reached. We've already seen the `while` loop which repeats a code block while a condition is true.
# 
# ## `while` Loops
# 
# In Python we use a `while` statement to repeat a sequence of statements while a specific condition is satisfied.

# In[12]:


pop = 10 # initial population
year = 0 # initial year
while pop < 1000: # repeat the following statements while pop is less than 1000
    year = year + 1 # update the year 
    pop = pop * 2 # update the population
print("Number of years:", year)


# :::{note}
# - The `while` statement is terminated by a colon (`:`)
# - The `while` condition is `pop < 1000`
# - The indented lines below the `while` statement are executed repeatedly while the condition is true  
# :::
# 
# ## Relational Operators
# The less-than operator `<` is a **relational operator**. It compares two expressions and evaluates to `true` if the expression on the left is less than the expression on the right. Other relational operators include the equality operator `==` which evaluates to `true` if the expression on the left is equal to the expression on the right. Relational operators can be used in `if` statements or `while` loops.
# 
# |Symbol|Operator|
# |---|---|
# |<|less than|
# |<=|less than or equal|
# |>|greater than|
# |>=|greater than or equal|
# |==|equals|
# |!=|does not equal|
# 
# :::{warning}
# It is very easy to make a mistake by choosing the wrong operator. For example, if we replaced `pop < 1000` with `pop > 1000` in the above code, the `while` loop is never entered since the condition is false on the first iteration.
# :::
# 
# ## Boolean Variables
# 
# We can assign the result of a relational operation to a variable. Such a variable has the value `True` or `False` and is called a **Boolean Variable**.
# 

# In[13]:


x = 5
y = 6
z = x > y
print(x, "is greater than", y, ":",  z)


# ## `for` Loops
# 
# A `for` loop is used to iterate over a sequence of elements. The simplest form of the `for` statement is to iterate over a range of integer values. For example, the following code will execute the indented statements once for each integer from 5 to 9:
# 

# In[14]:


for i in range(5, 10):
    print("i =", i)


# The `range` function specifies the sequence of integer values that the loop variable will take. `range(a, b)` generates a sequence starting at `a` and ending at `b - 1`.  
# To generate a sequence with a different step size, pass a third argument to the `range` function:

# In[15]:


for i in range(1, 10, 2):
    print("i =", i)


# You can use the range function with a single argument, in which case the range of values starts at zero:

# In[16]:


for i in range(5):
    print("i =", i)


# :::{note}
# - The loop variable `i` is updated each loop iteration
# - The for statement is terminated by a colon (`:`)
# - The indented lines below the `for` statement are executed once for each integer specified by the `range` function
# - The range function *includes* the lower limit but *excludes* the upper limit
# :::

# ### Nested Loops
# For loops may be **nested** by placing one inside another. The following example repeats in the inner loop 4 times for each of the out loop, resulting in a total of 20 iterations,.

# In[17]:


for i in range(5):
    for j in range(4):
        print(i, j, end="")
    print()


# :::{note}
# By default, the `print` function adds a newline character, which means that consecutive calls to `print` results in output on separate lines.
# 
# To avoid this, and use `print("text", end="")`.
# :::
