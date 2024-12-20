import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style

# velocity in meters per second (m/s)
velocity_initial = 5

# time in seconds (s)
time_inital = 0
time_final = 10

# law of velocity
def velocity(time):
    return time + velocity_initial

# PLOTTING
style.use('dark_background')

# time
time = np.linspace(0, 10, 100)

# set up figure and data
fig, ax = plt.subplots()

ax.set_title("Linear motion graph", fontdict= {'fontsize' : 15})
ax.set_xlabel("Time (s)")
ax.set_ylabel("Velocity (m/s)")

ax.set_xticks(np.arange(0, 11))
ax.set_yticks(np.arange(0, 16))

ax.grid()
ax.legend()

# Plot elements
line, = ax.plot([], [], label = 'v(t)', color = 'orange', linewidth = 4)

# initialisation function
def init():
    ax.set_ylim(0,10)
    ax.set_ylim(0,15)
    line.set_data([], [])
    return line,

# update frame function
def update(frame):
    x_data = time[:frame]
    y_data = velocity(x_data)
    line.set_data(x_data, y_data)
    return line,

# Define the animation
ani = FuncAnimation(fig, update, frames = len(time), init_func = init, blit = True, interval = 50)

# Show animation
plt.legend()
plt.show()