import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation, writers
from matplotlib import style

"""
law of velocity
v(t) = v0 + a * t

t - time (s)
v - velocity (m/s)
v0 - initial velocity
a - acceleration (m/s^2)
"""
# constants:
velocity_initial = 10
acceleration = 1

def velocity(time):
    return velocity_initial + acceleration * time

def max_velocity(t0: float, t1: float):
    maxv = velocity(t0)
    for t in np.linspace(t0, t1, 100):
        v = velocity(t)

        if v > maxv:
            maxv = v

    return maxv

# time interval in seconds (s)
time_0 = 0
time_1 = 10

# time and velocity data
time = np.linspace(time_0, time_1, 100)
velocity_values = velocity(time)

"""
PLOTTING:

- graph for velocity according to time v(t)
- dark background, orange line for velocity
- invisible line for formatting
- animated the change from zero to max
- animation goes at 2x the speed

"""
style.use('dark_background')

# set up figure and data

fig, ax = plt.subplots(dpi = 200)

ax.set_title("Linear motion graph", fontdict= {'fontsize' : 15})
ax.set_xlabel("Time (s)")
ax.set_ylabel("Velocity (m/s)")

ax.set_xticks(np.arange(time_0, time_1 + 2))
ax.set_yticks(np.arange(0, max_velocity(time_0, time_1) + 2, 2))

ax.grid(alpha = 0.1)
# The legend shouldn't be here!

# invisible line for formatting
ax.plot(time, velocity_values, alpha = 0)

# FIRST LINE
line, = ax.plot([], [], label = 'v(t)', color = 'orange', linewidth = 4)
ax.legend(loc = 'upper left')

# initialisation function
def init():
    ax.set_ylim(time_0-1, time_1+1)
    ax.set_ylim(0-2, max_velocity(time_0, time_1)+2)
    line.set_data([], [])
    return line,

# update frame functions
def update(frame):
    x_data = time[:frame]
    y_data = velocity_values[:frame]
    line.set_data(x_data, y_data)
    return line,

# Define the animation
ani1 = FuncAnimation(fig, 
                     func = update, 
                     frames = len(time)+10, 
                     init_func = init, 
                     blit = True, 
                     interval = 25, 
                     repeat = False)

plt.show()
plt.close(fig)

fig, ax = plt.subplots(dpi = 200)

ax.set_title("Linear motion graph", fontdict= {'fontsize' : 15})
ax.set_xlabel("Time (s)")
ax.set_ylabel("Velocity (m/s)")

ax.set_xticks(np.arange(time_0, time_1 + 2))
ax.set_yticks(np.arange(0, max_velocity(time_0, time_1) + 2, 2))

ax.grid(alpha = 0.1)

# Add the fill and the line
ax.plot(time, velocity_values, label = 'v(t)', color = 'orange', linewidth = 4)

x_values = []
y_values = []

fill = ax.fill_between(x_values, y_values, np.zeros_like(y_values),
                color = "orange", alpha = 0.5, label = '$\Delta$d')
ax.legend(loc = 'upper left')


ax.set_ylim(time_0-1, time_1+1)
ax.set_ylim(0-2, max_velocity(time_0, time_1)+2)

def update_fill(frame):
    x_values = time[:frame]
    y_values = velocity_values[:frame]
    fill.set_data(x_values, y_values, np.zeros_like(y_values))
    return fill

ani2 = FuncAnimation(fig, 
                     func = update_fill, 
                     frames = 110,
                     interval = 20,
                     repeat = False)

plt.show()
plt.close(fig)

# Save the animations:

#ani1.save("LinearMotion/Velocity_time.gif")
#ani2.save("LinearMotion/Distance_area.gif")
