#!/usr/bin/env python
# coding: utf-8

# # Strings
# 
# ```{admonition} What you'll learn
# :class: tip
#  - How to store a sequence of character data in a string
#  - How to extract substrings by slicing
#  - How to use string methods
# ```
# 
# ## Example: RNA Sequences
# 
# In biology, an RNA sequence consists of a chain of the nucleotides Adenine, Uracil, Cytosine and Guanine in a specific order. We can represent an RNA sequence using the four letters `A`, `U`, `C` and `G`.
# 
# ```{figure} rna.png
# ---
# name: RNA sequence
# ---
# An RNA sequence represented by the string `AUGAGACUCUGAGAC`. The sequence is composed of three-character subsequences called codons, each of which identifies a specific amino acid. 
# ```
# 
# ```{sidebar} Amino Acid Translation Table
# 
# |Amino Acid| | codons |
# |---|---|---|
# |Leucine|L|UUA, UUG, CUU, CUC, CUA, CUG|
# |Methionine|M|AUG|
# |Arginine|R|AGA, AGG, CGA, CGU, CGG, CGC|
# |Aspartic Acid|D|GAU, GAC|
# |(stop)|.|UGA|
# ```

# In the body, the RNA sequence is used to produce a protein in a process called translation. The sequence is first divided into three character subsequences termed 'codons'. For example, the 15 character RNA sequence `AUGAGACUCUGAGAC` is divided into the codons `AUG`, `AGA`, `CUC`, `UGA`, and `GAC`.
# 
# Each of the codons identifies a specific amino acid, as shown in the partial amino acid translation table on the right. The RNA sequence `AUGAGACUCUGAGAC` would therefore be translated by the body into the amino acid sequence `methionine`, `arginine`, `leucine`, `(stop)`, `aspartic acid`. Using the abbreviated one-letter characters, this could be written as `MRL.D`.
# 
# Finally, the body chains together these amino acids into a protein. The stop codon represents the end of the chain, so the RNA sequence would be translated into a protein comprising a chain of three amino acids `methionine-arginine-leucine`.
# 
# :::{admonition} RNA Translation
# 1. RNA sequence: `AUGAGACUCUGAGAC`
# 1. Codons:  `AUG` `AGA` `CUC` `UGA` `GAC`
# 1. Amino Acids: `MRL.D`
# 1. Protein sequence: `MRL`
# :::

# 
# ```{admonition} Bioinformatics
# :class: tip
# Bioinformatics is the application of tools of computation and analysis to the capture and interpretation of biological data. One of the main applications of bioinformatics is the analysis of genome sequence data, such as that undertaken by the Human Genome Project.
# ```
# 
# we'll now see how we can implement this procedure programmatically. In Python, a sequence of character data is termed a **string**.

# In[1]:


rna_seq = "AUGAGACUCUGAGAC"
print("RNA sequence:", rna_seq)


# First, let's write a function `translate` which takes a three letter string and returns a single letter representing the corresponding amino acid. 

# In[2]:


def translate(codon):
    codon_list = ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG", "AUG", "AGA", "AGG", "CGA", "CGU", "CGG", "CGC", "GAU", "GAC", "UAA", "UAG", "UGA"]
    amino_acids = ["L", "L", "L", "L", "L", "L", "M", "R", "R", "R", "R", "R", "R", "D", "D", ".",  ".",  "."]
    
    i = codon_list.index(codon)
    aa = amino_acids[i]
    return aa


# Test the function using the CGG codon
codon = "CGG"
aa = translate("CGG")
print("Codon:", codon)
print("Amino acid:", aa)
   


# The list `codon_list` contains the three letter codons, and the list `amino_acids` contains the correspdonding single-letter amino acid abbreviations. Translating from codon to amino acid is simply a case of finding the index position of the codon in `codon_list` and identifying the character in the same position in `amino_acids`:
# 
# ```
# i = codon_list.index(codon)
# aa = amino_acids[i]
# ```
# 
# `i` is an integer represnting the index of the string `codon` in `codon_list`.
# 
# 
# ```{admonition} Finding items in a list
# :class: seealso
# See the previous section **Lists and Plotting** for how to find items in a list.
# ```
# 
# Next, we would like to split the string `rna_seq` into three-character codons, then use our function to determine the amino acid for each.

# In[3]:


n = len(rna_seq)
for i in range(0, n, 3):
    codon = rna_seq[i:i+3]
    print(translate(codon))


# First we use the `len` function to determine the number of characters in the string `rna_seq`. Next we generate a loop from `0` to `n` in steps of `3`:
# 
# ```
# for i in range(0, n, 3):
# ```
# 
# The expression `rna_seq[i:i+3]` extracts the a 3-character substring from `rna_seq` begining at the character at index `i`.
# 
# Finally, what if we'd like to stop processing the sequence once we reach the 'stop' codon? Python has a useful keyword `break` which allows us to do exactly that:

# In[4]:


n = len(rna_seq)
for i in range(0, n, 3):
    codon = rna_seq[i:i+3]
    if codon == "UGA":
        break
    print(translate(codon))


# As soon as the `break` keyword is reached, the enclosing `for` loop is exited, even if this means aborting the loop early.

# 
# ## String Variables
# A string is data type representing character data. In Python, string literals are surrounded either by double quote `"` or single quote `'` characters.

# In[5]:


greeting_start = "Season's"
greeting_end = 'greetings'

print(greeting_start, greeting_end)


# ## String Concatenation
# Use the `+` symbol to **concatentate** strings

# In[6]:


greeting = greeting_start + " " + greeting_end
print(greeting)


# But it is not possible to concatentate a string and a number:

# In[7]:


id = greeting + 55


# ## Converting between strings and numbers
# 
# Functions `str`, `int` and `float` are available to convert between strings and other data types.

# In[14]:


# convert from integer to string
id = 1729
new_id = str(id) + "_NEW"
print(new_id)


# In[15]:


# convert from string to floating-point number
price = "12.99"
total_price = float(price) * 1.2
print(total_price)


# ## String Methods
# A string is an **object**, which is a data type with **methods** directly attached with it which can be called similarly to calling a function. The `upper` method converts a string to upper case, and `lower` to lowercase:

# In[19]:


name = "Jeremy Bentham"
name_uppercase = name.upper()
print(name_uppercase)
name_lowercase = name.lower()
print(name_lowercase)


# Other useful methods are `split`, `join` and `trim`. `split` splits the string into individual words and returns them as a list:

# In[17]:


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


# :::{note}
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
# :::

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
    


# :::{note}  
# - String comparison is **case-sensitive** so `"S" == "s"` is `False`.
# - Remember to use a double equals to check for equality.
# :::

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
# String literals can span multiple lines, using triple-quotes: `"""`...`"""` or `'''`...`'''`.

# In[1]:


long_string = """Twas the night before Christmas,
when all through the house
Not a creature was stirring,
not even a mouse."""
print(long_string)

