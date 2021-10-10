#!/usr/bin/env python
# coding: utf-8

# # Python Fundamentals
# 
# Programming is all about breaking down a problem into simple steps that the computer can understand. In this case, the 'simple steps' are instructions, written in the Python programming language, which perform simple operations such as performing arithmetic calculations or setting the value of variables. These instructions are usually performed one at a time in sequence, although some instructions might cause the program to branch to a different section of code or to repeat a section of code. In this section we will introduce some of the most common Python constructs and some techniques to solve simple computational problems.
# 
# ```{admonition} What you'll learn
#  - How to create variables
#  - How to perform arithmetic calcuations
#  - Displaying output using `print`
#  - Branching using the `if` statement
#  - Looping using the `while` statement
#  - Using pseudocode to construct the solution to a problem
# ```
# ## Example
# 
# We'll start with a simple example of a Python program which simulates the growth in population of a colony of bacteria. Suppose we start with 100 cells and the population doubles every hour. How many hours will it take to reach a population of 10000 cells?

# In[1]:


pop = 100

while pop < 10000:
    # double the population
    pop = pop * 2
    print(pop)


# Let's examine each line in turn. First, we define a **variable** `pop` and set its value to 100:
# 
# ```
# pop = 100
# ```
# 
# Then we define a `while` loop. A `while` loop repeats a section of code while the specified condition is true:
# 
# ```
# while pop < 10000:
# ```
# 
# The code in the indented block below this line is then executed repeatedly. The line `# double the population` is a comment and is ignored by the Python interpreter. Next, multiply `pop` by 2:
# 
# ```
#     pop = pop * 2
# ```
# 
# Then `print` the value of `pop`:
# 
# ```
#    print(pop)
# ```
# 
# Execution terminates once the condition `pop < 1000` becomes false.
# 
# When we run the code, we can see that it prints 7 values, so it must take 7 hours for the population to exceed 10000. But let's adapt the code so that it prints this number. We'll need to introduce a second variable to keep track of the number of hours:

# In[2]:


pop = 100
i = 0
while pop < 10000:
    pop = pop * 2
    i = i + 1
    print(pop)
    
print("Number of hours:", i)


# The value of `i` is initialised to zero, and then increased by 1 during each iteration of the loop. Notice that the value of `pop` is printed 7 times, whereas the Number of hours `i` is only printed once after the loop terminates since it is outside the indented block.
# 
# Finally, suppose the the population growth rate is 1.02 rather than 2. If we print the population in every iteration of the loop, we're going to have an enormous list of numbers. So let's print it only once every 24 hours instead:

# In[3]:


pop = 100
i = 0
while pop < 10000:
    pop = pop * 1.02
    i = i + 1
    if i % 24 == 0:
        print(pop)
    
print("Number of hours:", i)


# We have introduced the following line `if i % 24 == 0:`. There are two separate constructs here: an `if` statement and the `%` operator. The indented code `print(pop)` will only be executed if the condition `i % 24 == 0` is true. `i % 24` means 'remainder after dividing `i` by 24', which is only equal to zero when `i` is a multiple of 24. We'll look at this in more detail later.

# This may be a simple example, but there is already some significant complexity hidden in here. We'll now cover in more detail the various language constructs used here, and introduce a few more.
# 
# ## Variables
# 
# A **variable** is a named storage location in the computer's memory. We store a value in a variable so that we can use it later in our computations.
# 
# We use **assignment** to set the value of a variable:

# In[4]:


speed = 35 # assign the value 35 to a variable called speed
print(speed)


# We can assign a new value to an existing variable:

# In[5]:


speed = 40 # The new value replaces the old value
print(speed)


# Assignment is not the same as equality. We can have the same variable on both sides of the equals sign:

# In[6]:


speed = speed + 2 # Calculcate speed + 2 then assign the result to variable 'speed'
print(speed)


# This is a legal statement because Python first evaluates the expression on the right of the equals sign (`speed + 2`) and *then* places the result into the variable on the left.

# ```{note}
# **VARIABLE NAMING RULES**  
# - A variable name can only contain alpha-numeric characters and underscores (`A-Z`, `a-z`, `0-9`, and `_`)
# - A variable name cannot start with a number
# - Variable names are case-sensitive (`age`, `Age` and `AGE` are three different variables)
# ```
# :::{warning}
# Beware of accidentally renaming Python keywords. The following is correct Python but a Very Bad Idea because it renames the `print` function, which will result in some very weird errors!
# 
# ```
# print = 5
# 
# print(print) # this won't work.
# ```
# :::
# 

# ## Printing
# 
# The `print` function is used to display values to the screen.

# In[7]:


print("Good morning :-)")


# ```
# print("Good morning :-)")
# ```
# instructs Python to display a line of text. We call the function `print` and pass it the text to be displayed.  
# 
# A sequence of characters enclosed in quotation marks  
# ```
# "Good morning :-)"
# ```
# is called a **string**.
# 
# The print statement can also print numbers. The following example evaluates `3 + 4` and prints the result:

# In[8]:


print(3 + 4)


# The print statement can print multiple values. Separate each value by a comma:

# In[9]:


print("3 + 4 =", 3 + 4, ":-)")


# Notice that Python inserts a space between each value.
# 
# The `print` function starts a new line after each statement. If no arguments are passed to the function, it prints a blank line. 

# In[10]:


print("***")
print()
print("***")


# :::{note}
# `print` is the first of many Python in-built functions that we will study.
# 
# You can find out more about Python functions by using the **`help()`** function. For example, we can see change the default seperator using `sep`
# :::

# In[11]:


help(print)


# In[12]:


print("1", "2", "3", sep="-")


# :::{admonition} Pseudocode
# Pseudocode is a way to represent the solution to a programming problem in 'plain English', without worring about correct programming syntax. For example, suppose we have the following problem:
# 
# > The value of a loan increases by 1.3% every month, except in December when it is reduced by 100 pounds. How many months will it take for a 1000 pound loan to reach 2000 pounds?
# 
# We might write this in pseudo code as follows:
# 
# ```none
# set loan to 1000  
# set counter to 0  
# repeat until loan is greater than 2000:
#   if counter is divisble by 12:
#     decrease loan by 100
#   otherwise
#     multiply loan by 1.013
#   increase counter by 1
# display value of counter
# ```
# 
# By writing the pseudocode, we can establish the correct algorithm for the solution, before turning it into syntatically-correct Python code. There exist several 'standard' versions of pseudocode, although in this course I encourage you to write it in any way which makes sense to you!
# :::

# ## Number Types
# 
# Every Python variable has a **data type** as well as a value. The type determines what operations can be performed on the variable and how it is stored in the computer's memory. Python supports a number of primitive data types including numbers, strings, lists and files and in particular there are two number types: **integers** and **floating point numbers**. When we specify a number in code it is important to understand which type we are creating:
# 
# |Number|Type|Description|
# |---|---|---|
# |`5`|`int`|A whole number|
# |`-5`|`int`|A negative integer|
# |`0.5`|`float`|A number with decimal part|
# |`5.0`|`float`|Including a decimal point always results in type `float`|
# |`5e6`|`float`|$5\times10^6$|
# |`2.34e-5`|`float`|$2.34\times10^{-5}$|

# ## Arithmetic Operators
# Python supports basic arithmetic operations addition, subtraction, multiplication and division using the symbols `+`, `-`, `*` and `/`. Brackets are used to indicate the order in which the parts of an expression are computed. For example, in the following expression, the division is performed first and then the addition.

# In[13]:


3 + 4 / 2


# In order to compute $\frac{3 + 4}{2}$, use brackets:

# In[14]:


(3 + 4) / 2


# In order to calculate powers, use the `**` operator. For example, the following calculates the $8^3$:

# In[15]:


8 ** 3


# ## Modulo Arithmetic
# 
# Using the `/` operator results in a float-point value:

# In[16]:


9 / 4


# On the other hand, the `//` operator performs **floor division**, computing the quotient and discarding the fractional part:

# In[17]:


9 // 4


# To calculate the remainder after floor division, use the **modulus** operator `%`:

# In[18]:


9 % 4


# ### Example 1
# The `%` operator is useful to determine if a variable is divisible by a number. For example, if a number is even its remainder after dividing by 2 is zero; if it is odd its remainder after dividing by 2 is 1:

# In[19]:


x = 5
print(x % 2)
x = 6
print(x % 2)


# ### Example 2
# Suppose we have 1234 pennies in the piggy-bank. How much do we have in pounds and pence? First we divide by 100 to get the while number of pounds:

# In[20]:


num_pennies = 1234
pounds = num_pennies // 100
print("Pounds:", pounds)


# Next we use the `%` operator to find the number of pence:

# In[21]:


pence = num_pennies % 100
print("Pence:", pence)


# ## Python Operators
# 
# | Operator | Symbol |
# |---|---|
# | Addition | `+` |
# | Subtraction | `-` |
# | Multiplication | `*` |
# | Division | `/` |
# | Power | `**` |
# | Modulo | `%` |
# | Floor division | ``//`` |

# ## `If` statement
# The specific heat capacity of water depends on whether it is in a solid, liquid or gaseous state.
# 
# |State|Specific heat capacity (kJ/kgK)|
# |---|---|
# |Solid|2.108|
# |Liquid|4.187|
# |Gas|1.996|
# 
# Let's write code which, given the temperature of a water sample, sets the value of the variable `shc` to the appropriate value (of course, we need to know the melting and boiling points of water!)

# In[22]:


temp = 90 # temperature of water sample

if temp > 100:
    shc = 1.996
elif temp > 0:
    shc = 4.187
else:
    shc = 2.108
    
print("Specific heat capacity:", shc, "kJ/kgK")


# The `if` statement evaluates the expression `temp > 100` and if it is true, executes the indented code directly underneath, then skips to the next statement after the `if-else` block. If it is not true, execution moves to the `elif` statement. If the expression `temp > 0` is true, the indented code beneath it is executed  and execution skips to the next statement after the `if-else` block. Finally, if neither expression is true, the indent code block below the `else` statement is executed.
# 
# :::{note}
# **`If` statement**
# - Exactly one of the indented code blocks will be executed.
# - Use the `tab` key to indent code by exactly four spaces.
# - The `if`, `elif` and `else` statements must be followed by a colon (`:`).
# - Note the unusual keyword `elif` (rather than `elseif`).
# - The `elif` and `else` statements are optional.
# :::
# 
# :::{warning}
# **Assignment vs Equality**  
# 
# `=` is the **assignment** operator. It assigns the value on the right to the variable on the left:
# ```
# x = 6 + 7 # sets x to the value 13
# ```
# 
# `==` is the **equality** operator. It evaluates to `True` if the expression on the left is equal to the expression on the right.
# ```
# x == 13 # returns `True`
# ```
# 
# The condition in an `if` statement should always use `==`. This is a common mistake:
# 
# ```
# if x = 13: # this is a mistake. Be careful!
#     print("yes")
# ```
# :::

# ### Example
# 
# The following example checks if the number `x` is divisible by 2, and prints an appropriate message.
# 
# Note that we use the operator `==` to check for equality.

# In[23]:


x = 53783

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")

