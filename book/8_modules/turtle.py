import matplotlib.pyplot as plt
import numpy as np

# function definitions

def start():
    state[0] = 0
    state[1] = 0
    state[2] = 0
    
    plt.figure(figsize=(5,5))
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    
def draw_forward(dis):
    x = state[0]
    y = state[1]
    angle = state[2]
    state[0] = x + dis * np.cos(angle)
    state[1] = y + dis * np.sin(angle)
    plt.plot([x, state[0]], [y, state[1]], color="black", linewidth=2)
    
def rotate_left(theta):
    state[2] = state[2] + theta * np.pi / 180
    
state = [0, 0, 0]
