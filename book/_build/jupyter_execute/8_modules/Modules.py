#!/usr/bin/env python
# coding: utf-8

# # Modules
# 
# A **module** is a file with a `.py` extension which contains Python code. The code can be **imported** from the module using the Python `import` statement.
# 
# First, create a new file called `turtle.py` and paste in the following code:
# 
# ```
# import matplotlib.pyplot as plt
# import numpy as np
# 
# # function definitions
# 
# def start():
#     state[0] = 0
#     state[1] = 0
#     state[2] = 0
#     
#     plt.figure(figsize=(5,5))
#     plt.xlim(-2, 2)
#     plt.ylim(-2, 2)
#     
# def draw_forward(dis):
#     x = state[0]
#     y = state[1]
#     angle = state[2]
#     state[0] = x + dis * np.cos(angle)
#     state[1] = y + dis * np.sin(angle)
#     plt.plot([x, state[0]], [y, state[1]], color="black", linewidth=2)
#     
# def rotate_left(theta):
#     state[2] = state[2] + theta * np.pi / 180
#     
# state = [0, 0, 0]
# ```
# 
# This defines a module called `turtle`.
# 
# Next, create a notebook (with `.ipynb` extension) and enter the following code. The `py` file and the `ipynb` files must be in the same folder.

# In[1]:


import turtle


# This statement imports the module `turtle` which is defined in the file `turtle.py` contained in the same folder as the notebook. When the Python interpreter executes this statement, it reads and executes the code contained in the file.
# 
# Any functions or variables defined in the module `turtle` can now be accessed from this notebook using the prefix `turtle.`. For example, the function `start()` defined in `turtle.py` can be called using `turtle.start()`:

# In[2]:


turtle.start() # call start function defined in turtle.py
turtle.draw_forward(1) # call draw_forward function defined in turtle.py


# ## Modularising Code
# 
# Modules are useful for breaking a large program into smaller parts. For example, the `.ipynb` file could contain only code suitable for presentation, with other code relegated to functions defined in `.py` files.
# 
# Because functions must be imported before being used, it is common practice to gather together all `import` statements at the top of the notebook file.
# 
# ```
# import numpy as np
# import turtle
# 
# # rest of code goes here...
# ```
# 
