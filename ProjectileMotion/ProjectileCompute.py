import numpy as np

"""
Projectile motion simulation
input:  launch velocity, ex: 100 m/s;
        launch angle ex: 60

output: projectile position (x,y)
        at each time spot

distance - meters
time - seconds
"""

#constants:
gravity = 9.81

def get_v_x_launch(launch_velocity: int, launch_angle: int):
    """Compute x velocity at launch, convert angle to radians"""
    angle_radians = launch_angle / 180.0 * np.pi
    v_x = launch_velocity * np.cos(angle_radians)
    return np.round(v_x, 2)

def get_v_y_launch(launch_velocity: int, launch_angle: int):
    """Compute y velocity at launch, convert angle to radians"""
    angle_radians = launch_angle / 180.0 * np.pi
    v_y = launch_velocity * np.sin(angle_radians)
    return np.round(v_y, 2)
    
def get_x_position(time_spot: float, v_x_launch: float):
    """Compute x position at t time:    x(t) = v_x0 * t"""
    x = v_x_launch * time_spot
    return np.round(x, 2)

def get_y_position(time_spot: float, v_y_launch: float):
    """Compute y position at t time:    y(t) = v_y0 * t - g*(t^2)/2"""
    y = v_y_launch * time_spot - gravity * np.pow(time_spot, 2) / 2
    return np.round(y, 2)

def v_y(time_spot: float, v_y_launch: float):
    """Compute vertical velocity at t time: v_y(t) = v_y0 - g*t"""
    v_y = v_y_launch - gravity * time_spot
    return np.round(v_y, 2)

def max_altitude_time(v_y_launch: float):
    """Max altitude => v_y = 0 => v_y0 = gt => t = v_y0 / g"""
    return np.round(v_y_launch / gravity, 3)

def max_altitude(v_y_launch: float):
    """Plug in the max altitude time into the height formula 
    y = v_y0 * t + g/2 * t^2"""
    return get_y_position(max_altitude_time(v_y_launch), v_y_launch)

def flight_time(v_y_launch: float):
    """Compute flight time with quadratic ecuation:
    y=0 => g/2 * t^2 + v_y0 * t = 0
    => t = 0 or t = 2 * v_y0 / g"""
    return np.round(2 * v_y_launch / gravity, 3)

def range(v_x_launch: float, v_y_launch: float):
    """Compute the range of the projectile"""
    return np.round(v_x_launch * flight_time(v_y_launch), 2)

#example:
launch_velocity = 100
launch_angle = 60

v_x_launch = get_v_x_launch(launch_velocity, launch_angle)
v_y_launch = get_v_y_launch(launch_velocity, launch_angle)

print(f"max altitude: {max_altitude(v_y_launch)} m at {max_altitude_time(v_y_launch)} s")
print(f"projectile range: {range(v_x_launch, v_y_launch)} m")
print(f"flight time: {flight_time(v_y_launch)} s")
