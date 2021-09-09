#!/usr/bin/env python
# coding: utf-8

# # Motion of an Object under Gravity
# ## One-dimensional Case
# Newton's law of gravitation determines the force acting on a mass due to the gravitational attraction of a second mass:
# 
# $$F = \frac{Gm_1m_2}{r^2}$$
# 
# Where $G$ is the universal gravitational constant, $m_1$ and $m_2$ are the two masses in kilograms and $r$ is the distance between them in metres.
# 
# Consider a projectile of mass $m_\mathrm{p}$ fired vertically from the surface of The Earth. The force acting on the projectile is
# 
# $$F = -\frac{Gm_\mathrm{p}m_\mathrm{e}}{x^2}$$
# 
# where $x$ is the distance of the projectile from the centre of The Earth. Combining with Newton's second law of motion $F = m_\mathrm{p}\ddot{x}$ gives an equation relating acceleration $\ddot{x}$ to position $x$:
# 
# $$\ddot{x} = -\frac{Gm_\mathrm{e}}{x^2}$$
# 
# Finally, introducing the velocity $v = \dot{x}$ gives a coupled system of ordinary differential equations:
# 
# $$\begin{align*}
# \frac{dx}{dt} &= v\\
# \frac{dv}{dt} &= -\frac{Gm_\mathrm{e}}{x^2}
# \end{align*}$$
# 
# (Note that the mass of the projectile does not appear in this equation! Is this what you would expect?)
# 
# ## Two-dimensional Case
# An object is floating at position $(x_1, x_2)$ relative to the earth which is assumed to remain stationory at position $(0, 0)$.
# 
# Let $\mathbf{x}$ be the position vector of the object and $\mathbf{F}$ the force vector:
# 
# $$\mathbf{x} = \begin{bmatrix}
#            x_{1} \\
#            x_{2}
#          \end{bmatrix}$$
#          
# $$\mathbf{F} = \begin{bmatrix}
#            F_{1} \\
#            F_{2}
#          \end{bmatrix}$$
# 
# $$$$
# 
# Newton's law of gravitation states that the force has magnitude:
# 
# $$F = \frac{Gm_\mathrm{e}m_\mathrm{p}}{r^2}$$
# 
# where $r = \sqrt{x_1^2 + x_2^2}$ is the distance between Earth and the object.
# 
# The direction of the force vector is a unit vector in the opposite direction to $(x_1, x_2)$ 
# 
# $$-\frac{\mathbf{x}}{r} $$
# 
# The force vector is then:
# 
# $$\mathbf{F} = -\frac{Gm_\mathrm{e}m_\mathrm{p}}{r^2}\frac{\mathbf{x}}{r} =  -\frac{Gm_\mathrm{e}m_\mathrm{p}}{r^3}\mathbf{x}$$
# 
# Introducing the velocity vector $\mathbf{v} = \ddot{\mathbf{x}}$ and using Newton's second law $\mathbf{F} = m_\mathrm{p}\ddot{\mathbf{x}}$:
# 
# $$\begin{align*}
# \frac{d\mathbf{x}}{dt} &= \mathbf{v}\\
# \frac{d\mathbf{v}}{dt} &= -\frac{Gm_\mathrm{e}}{r^3}\mathbf{x}
# \end{align*}$$
# 
# Defining a timestep $\Delta t$, then the position vector $\mathbf{x}_{i+1}$ and velocity vector $\mathbf{v}_{i+1}$ at timepoint $i+1$ can be calculated from the position and velocity vectors $\mathbf{x}_{i}$ and $\mathbf{v}_{i}$ at time point $i$:
# 
# $$ \begin{align*}
# \mathbf{x}_{i+1} &= \mathbf{x}_i + \mathbf{v}_i\Delta t\\
# \mathbf{v}_{i+1} &= \mathbf{v}_i -\frac{Gm_\mathrm{e}}{r^3}\mathbf{x_i}\Delta t
# \end{align*}$$
# 
# 

# In[ ]:




