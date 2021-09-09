#!/usr/bin/env python
# coding: utf-8

# # Strings
# ## String Variables
# A string is data type representing character data. In Python, string literals are surrounded either by double quote `"` or single quote `'` characters.

# In[1]:


greeting_start = "Season's"
greeting_end = 'greetings'

print(greeting_start, greeting_end)


# ## String Concatenation
# Use the `+` symbol to **concatentate** strings

# In[2]:


greeting = greeting_start + " " + greeting_end
print(greeting)


# But it is not possible to concatentate a string and a number:

# In[3]:


id = last_name + 55


# ## Converting between strings and numbers
# 
# Functions `str`, `int` and `float` are available to convert between strings and other data types.

# In[12]:


# convert from integer to string
id = 1729
new_id = str(id) + "_NEW"
print(new_id)


# In[14]:


# convert from string to floating-point number
price = "12.99"
total_price = float(price) * 1.2
print(total_price)


# ## String Methods
# A string is an **object**, which is a data type with **methods** directly attached with it which can be called similarly to calling a function. The  `upper` method returns a new string in upper case:

# In[19]:


name = "Ian Botham"
name_uppercase = name.upper()
print(name_uppercase)


# Other useful methods are `split`, `join` and `trim`. `split` splits the string into individual words and returns them as a list:

# In[2]:


text = "The time has come"
word_list = text.split()
print(word_list)


# `join` does the reverse, combining a list of strings into a single string. `s1.join(word_list)` joins the strings in ``

# In[3]:


", ".join(word_list)


# `strip` removes any white space characters (spaces, tabs or newlines) at the start or end of the string:

# In[21]:


text = "  too much space!   "
text2 = text.strip()
print(text2)


# ## Strings and Characters
# A string is composed of a sequence of characters, and most of the operations that can be performed on lists can also be performed on strings. For example, individual characters can be accessed using square brackets enclosing the index position.

# In[34]:


text = "Natural Sciences"
# first character is at index 0
first_initial = text[0]
# last character is at index -1
final_character = text[-1]
print(first_initial, final_character)


# Use the `len` function to find the length of a string.

# In[11]:


s = "Mighty"
x = len(s)
print(x)


# ---
# **NOTE**
# 
# An important difference between lists and strings: whereas it is possible to change the value of an an individual list item, it is **not** possible to change an indivdual string character. We say that strings are **immutable**.
# ```
# x = [4, 5, 6]
# x[0] = 10 # this is OK
# s = "ABC"
# s[0] = "X" # this will result in an error
# ```
# Likewise, it is not possible to append a character to a string. Instead, use string concatenation.
# ```
# s.append("D") # Error
# s = s + "D" # This is OK
# ```
# ---

# ## Slicing Lists and Strings
# 
# Given a list or string, we can access a single element using square brackets:
# 

# In[26]:


x = [4, 5, 6, 7, 8, 9]
y = x[0]
print(y)


# If we want to access a sublist, we can use array **slicing**. Given integers `a` and `b`, `x[a:b]` returns a new list which contains the elements of `x` from index `a` to `b - 1` (i.e. including element `a` but excluding element `b`).

# In[27]:


z = x[0:3]
print(z)


# `x[a:b:c]` returns a list containing items `a` to `b - 1` with a step size of `c` (this is very similar to the `range` function),

# In[30]:


w = x[0:9:2]
print(w)


# ## Example
# Natural Sciences modules are identified by a 8 character code consisting of `NSCI` followed by a four digit number. The following paragraph of text contains Natural Sciences module codes mixed up with other data. We will write Python code to extract a list of Module codes from the text.

# In[32]:


text = "Surrounded NSCI0007 me occasional pianoforte NSCI0011 alteration unaffected impossible ye. For saw half than cold.  arrived adapted. Numerous ladyship so raillery humoured goodness received an. So NSCI0004 formal length my highly NSCI0005 afford oh. Tall neat he make or at dull ye."

n = len(text) # determine the number of characters in the text
module_list = [] # create an empty list
for i in range(n): # i loops of all index positions in text
    if text[i:i + 4] == "NSCI": # exctact a 4 character substring and check if it is equal to "NSCI"
        module_list.append(text[i:i + 8]) # add 8 characters to the list
print(module_list)
    


# ---
# **NOTES**  
# - String comparison is **case-sensitive** so "S" == "s" is *not* true.
# - Remember to use a double equals to check for equality.
# ---

# ## Escape Sequences
# 
# If you want to include special characters in a string, use an **escape sequence**. Precede the character you want to want to escape by a backslash character `\`.

# In[13]:


quote = '"The time has come", the Walrus said.'
print(quote)


# In[14]:


quote = "\"The time has come\", the Walrus said."
print(quote)


# This can also be used to include a backslash character in the string.

# In[20]:


quote = "A\\B"
print(quote)


# A very useful excape sequence is `\n`, which denotes a **newline** character.

# In[21]:


print("A\nAB\nABC")


# ## Multi-line Strings
# String literals can span multiple lines, using triple-quotes: """...""" or '''...'''.

# In[1]:


long_string = """Twas the night before Christmas,
when all through the house
Not a creature was stirring,
not even a mouse."""
print(long_string)

