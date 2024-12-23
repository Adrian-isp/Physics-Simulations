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

class Projectile:
    #constants:
    gravity = 9.81

    def __init__(self, launch_velocity: int, launch_angle: int):
        self.launch_velocity = launch_velocity

        """Convert angle to radians"""
        self.angle_radians = launch_angle / 180 * np.pi

        """Compute x velocity at launch"""
        self.v_x_launch = np.round(self.launch_velocity * np.cos(self.angle_radians), 3)
        """Compute y velocity at launch"""
        self.v_y_launch = np.round(self.launch_velocity * np.sin(self.angle_radians), 3)

        """Compute flight time with quadratic ecuation:
        y=0 => g/2 * t^2 + v_y0 * t = 0
        => t = 0 or t = 2 * v_y0 / g"""
        self.flight_time = np.round(2 * self.v_y_launch / self.gravity, 3)
    
    def get_x_position(self, time_spot: float):
        """Compute x position at t time:    x(t) = v_x0 * t"""

        if np.any(time_spot) > self.flight_time or np.any(time_spot) < 0:
            raise ValueError(f"Invalid time: {time_spot}, value must be between 0 and {self.flight_time} seconds")

        x = self.v_x_launch * time_spot
        return np.round(x, 3)

    def get_y_position(self, time_spot: float):
        """Compute y position at t time:    y(t) = v_y0 * t - g*(t^2)/2"""

        if np.any(time_spot) > self.flight_time or np.any(time_spot) < 0:
            raise ValueError(f"Invalid time: {time_spot}, value must be between 0 and {self.flight_time} seconds")

        y = self.v_y_launch * time_spot - self.gravity * np.pow(time_spot, 2) / 2
        return np.round(y, 3)

    def get_v_y(self, time_spot: float):
        """Compute vertical velocity at t time: v_y(t) = v_y0 - g*t"""

        if np.any(time_spot) > self.flight_time or np.any(time_spot) < 0:
            raise ValueError(f"Invalid time: {time_spot}, value must be between 0 and {self.flight_time} seconds")

        v_y = self.v_y_launch - self.gravity * time_spot
        return np.round(v_y, 3)

    def max_altitude(self):
        """Max altitude => v_y = 0 => v_y0 = gt => t = v_y0 / g
        Plug in the max altitude time into the height formula 
        y = v_y0 * t + g/2 * t^2"""

        time_to_max_altitude = self.v_y_launch / self.gravity
        return self.get_y_position(time_to_max_altitude)

    def range(self):
        """Compute the range of the projectile:
        x max = v_x_0 * flight_time"""
        return np.round(self.v_x_launch * self.flight_time, 3)

def main():
    launch_velocity = int(input("Type the launch velocity (m/s): "))
    launch_angle = int(input("Type the launch angle (degrees): "))
    projectile = Projectile(launch_velocity, launch_angle)

    print(f"max altitude: {projectile.max_altitude()} m")
    print(f"flight time: {projectile.flight_time} s")
    print(f"range: {projectile.range()} m")

if __name__ == "__main__":
    main()