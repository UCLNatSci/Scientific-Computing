#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python
# 
# ## Printing
# 
# In this section, we introduce the first Python function in detail.

# In[1]:


# My first program
print("My name is Pete :-)")


# The first line
# ```
# # My first program
# ```  
# is a comment. It begins with the `#` character and will be ignored by the Python interpreter.  
# 
# The second line
# ```
# print("My name is Pete :-)")
# ```
# instructs Python to display a line of text. We call the function `print` and pass it the text to be displayed.  
# 
# A sequence of characters enclosed in quotation marks  
# ```
# "My name is Pete :-)"
# ```
# is called a **string**.
# 
# The print statement can also print numbers. The following example evaluates `3 + 4` and prints the result:

# In[2]:


print(3 + 4)


# The print statement can print multiple values. Separate each value by a comma:

# In[3]:


print("3 + 4 =", 3 + 4, ":-)")


# Notice that Python inserts a space between each value.
# 
# The `print` function starts a new line after each statement. If no arguments are passed to the function, it prints a blank line. 

# In[4]:


print("***")
print()
print("***")


# ## Errors
# 
# Python expects code to have a very specific format. For example, every open bracket '`(`' must have a matching closing bracket '`)`'. If there is an error in the code, python will generate an **error message**.

# In[5]:


print("***"


# The error message tells us that the error is on `line 1` and that the type of error is `SyntaxError`.
# 
# This information can be very useful, especially in longer programs.

# In[13]:


print("This")
print("code")
print("works)
print("perfectly!")


# The error is on `line 3`. To view line numbers change to command mode (press `Esc`) then press the `l` key. Now we can see that the error is on line 3 and we can fix it by putting in the missing quote symbol `"`.

# ### Example
# 
# A car is travelling at 15 metres per second. Is it exceeding the speed limit of 30 miles per hour?
# 
# To solve this problem, first we define variables to store the speed of car in m/s and the speed limit in mph:

# In[4]:


car_speed_ms = 15
speed_limit_mph = 30


# Next, we need to convert the car speed into mph and store it in a new variable. We multiply by 3600 (seconds in an hour) then divide by 1609.34 (metres in a mile).

# In[5]:


car_speed_mph = car_speed_ms * 3600 / 1609.34
print(car_speed_mph)


# By printing the result, we can see that the car is exceeding the speed limit. But let's get Python to do the check, and print 'Slow down, Nigel!' if the car is driving too fast.

# In[6]:


message = "Slow down, Nigel!"
if car_speed_mph > speed_limit_mph:
    print(message)


# ---
# **Exercise**  
# Check if a car travelling at 13 m/s is exceeding the speed limit by changing the value of `car_speed_ms` and re-running the code.
# 
# ---

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

# ---
# **VARIABLE NAMING RULES**  
# - A variable name can only contain alpha-numeric characters and underscores (`A-Z`, `a-z`, `0-9`, and `_`)
# - A variable name cannot start with a number
# - Variable names are case-sensitive (`age`, `Age` and `AGE` are three different variables)
# ---
# 
# ---
# **BEWARE!**  
# 
# Beware of accidentally renaming Python keywords. The following is correct Python but a very bad idea because it renames the `print` function, which will result in some very weird errors!
# 
# ```
# # DON'T DO THIS!
# print = 5
# ```
# 
# ---
# 

# ## Strings
# 
# A **string** is a sequence of characters. Use single or double quote characters to delimit a string.

# In[8]:


message = "Don't do it!"
print(message)


# ## Number Types
# 
# Every Python variable has a **data type** as well as a value. The type determines what operations can be performed on the variable and how it is stored in the computer's memory. Python supports a number of primitive data types including numbers, strings, lists and files and in particular there are two number types: **integers** and **floating point numbers**. When we specify a number in code it is important to understand which type we are creating:
# 
# **NUMBER TYPES**
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

# In[8]:


3 + 4 / 2


# In order to compute $\frac{3 + 4}{2}$, use brackets:

# In[9]:


(3 + 4) / 2


# In order to calculate powers, use the `**` operator. For example, the following calculates the $8^3$:

# In[10]:


8 ** 3


# ## Modulo Arithmetic
# 
# Using the `/` operator results in a float-point value:

# In[11]:


9 / 4


# On the other hand, the `//` operator performs **floor division**, computing the quotient and discarding the fractional part:

# In[12]:


9 // 4


# To calculate the remainder after floor division, use the **modulus** operator `%`:

# In[13]:


9 % 4


# ### Example
# The `%` operator is useful to determine if a variable is divisible by a number. For example, if a number is even its remainder after dividing by 2 is zero; if it is odd its remainder after dividing by 2 is 1:

# In[14]:


x = 5
print(x % 2)
x = 6
print(x % 2)


# ### Example
# Suppose we have 1234 pennies in the piggy-bank. How much do we have in pounds and pence? First we divide by 100 to get the while number of pounds:

# In[15]:


num_pennies = 1234
pounds = num_pennies // 100
print("Pounds:", pounds)


# Next we use the `%` operator to find the number of pence:

# In[16]:


pence = num_pennies % 100
print("Pence:", pence)


# ---
# **OPERATOR LIST**  
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
# 
# ---

# ## Decisions
# The specific heat capacity of water depends on whether it is in a solid, liquid or gaseous state.
# 
# |State|Specific heat capacity (kJ/kgK)|
# |---|---|
# |Solid|2.108|
# |Liquid|4.187|
# |Gas|1.996|
# 
# Let's write code which, given the temperature of a water sample, sets the value of the variable `shc` to the appropriate value (of course, we need to know the melting and boiling points of water!)

# In[17]:


temp = 90 # temperature of water sample

if temp > 100:
    shc = 1.996
elif temp > 0:
    shc = 4.187
else:
    shc = 2.108
    
print("Specific heat capacity:", shc, "kJ/kgK")


# The `if` statement evaluates the expression `temp > 100` and if it is true, executes the indented code directly underneath, then skips to the next statement after the `if-else` block. If it is not true, execution moves to the `elif` statement. If the expression `temp > 0` is true, the indented code beneath it is executed  and execution skips to the next statement after the `if-else` block. Finally, if neither expression is true, the indent code block below the `else` statement is executed.

# ---
# **NOTES**  
# 
# - Exactly one of the indented code blocks will be executed.
# - Use the `tab` key to indent code by exactly four spaces.
# - The `if`, `elif` and `else` statements must be followed by a colon (`:`).
# - Note the unusual keyword `elif` (rather than `elseif`).
# - The `elif` and `else` statements are optional.
# 
# ---

# ### Example
# 
# The following example checks if the number `x` is divisible by 2, and prints an appropriate message.
# 
# Note that we use the operator `==` to check for equality.

# In[18]:


x = 53783

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")

