import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.animation import FuncAnimation

"""VISUALISING THE COMPUTED TRAJECTORY DATA
1. Graph the trajectory of the projectile
2. graph the velocity
"""

"""Add the simulation data:"""
from ProjectileCompute import Projectile
vel = 100
angle = 75
proj = Projectile(vel, angle)

# number of frames:
num_frames = 200

timespace = np.linspace(0, proj.flight_time, num_frames)

x_data = proj.get_x_position(timespace)
y_data = proj.get_y_position(timespace)
v_y_data = proj.get_v_y(timespace)
v_0_data = np.zeros_like(v_y_data)

"""Graph setup"""
style.use("dark_background")

fig, (ax_traj, ax_vel) = plt.subplots(2, 1, figsize = (8,12), dpi = 200)
fig.tight_layout(pad = 5)

ax_traj.set_title("Projectile Trajectory", fontdict={"fontsize":15})
ax_traj.set_xlabel("Horizontal Distance (m)", fontdict={"fontsize":11})
ax_traj.set_ylabel("Height (m)", fontdict={"fontsize":11})

ax_traj.grid(alpha = 0.1)
"""add the trajectory line"""
line, = ax_traj.plot([], [], color = "red", label = "trajectory", linewidth = 2)

"""Add the launch angle line"""
l_length = proj.max_altitude() * (1/np.sin(angle/180.0 * np.pi))
l_height = np.sin(angle/180 * np.pi) * l_length
l_length = np.cos(angle/180 * np.pi) * l_length
ax_traj.plot([0,l_length], [0,l_height], linestyle = "--", color = "white", label = "launch angle")
#this too:
ax_traj.plot([-l_length, proj.range() + l_length], [0, 0], linestyle = "--", color = "White", alpha = 0.2)

ax_traj.legend()

"""Add the velocity data"""

ax_vel.set_title("Velocity over time", fontdict={"fontsize":15})
ax_vel.set_xlabel("Time (s)", fontdict={"fontsize":11})
ax_vel.set_ylabel("Velocity (m/s)", fontdict={"fontsize":11})

ax_vel.grid(alpha = 0.1)

"""Add the velocity line and y=0"""
vel_color = "#89f336"
vel_line, =ax_vel.plot([], [], label = "v(t)", color = vel_color, linewidth = 3)
vel_0, = ax_vel.plot([], [], color = vel_color, linestyle = "--")
vel_fill = ax_vel.fill_between([], [], [], color = vel_color, alpha = 0.5, hatch = '/', label = "height travelled")

ax_vel.legend()

"""create the animation data"""
desired_limit = 100

def init():
    ax_traj.set_xlim(0, max(x_data) + desired_limit)
    ax_traj.set_ylim(0, max(y_data) + desired_limit)
    ax_vel.set_xlim(0, proj.flight_time)
    ax_vel.set_ylim(-1 * proj.v_y_launch, proj.v_y_launch)

    line.set_data([], [])
    vel_line.set_data([], [])
    vel_0.set_data([], [])
    vel_fill.set_data([], [], [])

    return (line, vel_line, vel_0, vel_fill)

def update(frame):
    x_values = x_data[:frame]
    y_values = y_data[:frame]
    line.set_data(x_values, y_values)

    vel_x_values = timespace[:frame]
    v_y_values = v_y_data[:frame]
    v_0_values = v_0_data[:frame]
    vel_line.set_data(vel_x_values, v_y_values)
    vel_0.set_data(vel_x_values, v_0_values)
    vel_fill.set_data(vel_x_values, v_y_values, v_0_values)

    # update limits to follow projectile
    x_current = x_data[frame]
    y_current = y_data[frame]
    ax_traj.set_xlim(x_current - desired_limit, x_current + desired_limit)
    ax_traj.set_ylim(y_current - desired_limit, y_current + desired_limit)

    return (line, vel_line, vel_0, vel_fill)

"""create the animation"""
ani1 = FuncAnimation(fig, func = update, frames = num_frames, init_func = init, interval = 30, blit = False)
#ani1.save("ProjectileMotion/Projectile_Animated.gif")

plt.show()
plt.close()

"""
Repeat for pictures
"""

fig, (ax_traj, ax_vel) = plt.subplots(2, 1, figsize = (8,12), dpi = 200)
fig.tight_layout(pad = 5)

ax_traj.set_title("Projectile Trajectory", fontdict={"fontsize":15})
ax_traj.set_xlabel("Horizontal Distance (m)", fontdict={"fontsize":11})
ax_traj.set_ylabel("Height (m)", fontdict={"fontsize":11})

ax_traj.set_xlim(-desired_limit, desired_limit)
ax_traj.set_ylim(-desired_limit, desired_limit)

ax_traj.grid(alpha = 0.1)
"""add the trajectory line"""
#line, = ax_traj.plot(x_data, y_data, color = "red", label = "trajectory", linewidth = 2)

"""Add the launch angle line"""
l_length = proj.max_altitude() * (1/np.sin(angle/180.0 * np.pi))
l_height = np.sin(angle/180 * np.pi) * l_length
l_length = np.cos(angle/180 * np.pi) * l_length
ax_traj.plot([0,l_length], [0,l_height], linestyle = "--", color = "white", label = "launch angle")
ax_traj.plot([-l_length, proj.range() + l_length], [0, 0], linestyle = "--", color = "White", alpha = 0.2)

ax_traj.legend()

"""Add the velocity data"""

ax_vel.set_title("Velocity over time", fontdict={"fontsize":15})
ax_vel.set_xlabel("Time (s)", fontdict={"fontsize":11})
ax_vel.set_ylabel("Velocity (m/s)", fontdict={"fontsize":11})

ax_vel.grid(alpha = 0.1)

"""Add the velocity line and y=0"""
vel_color = "#89f336"
vel_line, =ax_vel.plot(timespace, v_y_data, label = "v(t)", color = vel_color, linewidth = 3, visible = 0)
#vel_0, = ax_vel.plot(timespace, v_0_data, color = vel_color, linestyle = "--")
#vel_fill = ax_vel.fill_between(timespace, v_y_data, v_0_data, color = vel_color, alpha = 0.5, hatch = '/', label = "height travelled")

#ax_vel.legend()

fig.savefig("ProjectileMotion/Initial_Graph.png")

plt.show()
plt.close()