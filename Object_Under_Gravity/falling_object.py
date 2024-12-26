import numpy as np
import matplotlib.pyplot as plt

class FallingObject:
    """
    simulate iteratively an object with mass falling from a height
    using Euler's Method
    
    done: weight force implementation

    to do: visualisation
    """
    GRAVITY = 9.81 #m/s^2

    def __init__(self, mass: float, height: float, velocity = 0, velocity_angle = 90, shape = "cube", length = 1):
        """Initialise the simulation with the mass(kg), height(m), velocity(m/s) at an angle(degrees), object shape and length"""
        self.mass = mass
        # position is a vector r = [0, y]
        self.position = np.array([0.0, height])

        # calculate weight: G = m*g and turn into vector
        self.weight_force = np.array([0.0, -self.mass * self.GRAVITY])

        # turn velocity into a vector  v=[v_x, v_y], converting angles to radians
        self.velocity = np.array([velocity * np.cos(velocity_angle/180 * np.pi),
                                  velocity * np.sin(velocity_angle/180 * np.pi)])

        # drag coefficient and area based on shape
        match shape:
            case "cube":
                self.area = np.power(length, 2)
                self.DRAG_COEFFICIENT = 1.05
            case "sphere":
                self.area = np.pi * np.power(length/2, 2)
                self.DRAG_COEFFICIENT = 0.47
            case _:
                print("Invalid shape type. Defaulting to cube...")
                self.area = np.power(length, 2)
                self.DRAG_COEFFICIENT = 1.05


        self.time = 0
        # set the acceleration vector a = [ax, ay]
        self.acceleration = np.array([0.0, 0.0])

        # set the data storage for plotting
        self.time_data = np.array([self.time])
        self.position_data = np.array([self.position])
        self.velocity_data = np.array([self.velocity])

    def reset(self, height, velocity = 0, velocity_angle = 90):
        """Reset the simulation to new conditions"""
        self.position = np.array([0.0, height])
        self.velocity = np.array([velocity * np.cos(velocity_angle/180 * np.pi),
                                  velocity * np.sin(velocity_angle/180 * np.pi)])
        
        self.time = 0

        self.time_data = np.array([self.time])
        self.position_data = np.array([self.position])
        self.velocity_data = np.array([self.velocity])

    def update_drag_force(self):
        """
        Calculate drag force according to the following formula:
        F_drag = 0.5 * rho * |v|^2 * C_d * A , where:
            rho - aur density (~1,225 kg/m^3)
            v - velocity of object relative to fluid
            C_d - coefficent of drag (depends on shape)
            A - cross sectional area
        """
        rho = 1.225 #air density (kg/m^3)
        # velocity magnitude = |v|
        velocity_magnitude = np.linalg.norm(self.velocity)

        if velocity_magnitude == 0:
            self.drag_force = np.array([0.0, 0.0])
        else:
            drag_magnitude = 0.5 * rho * np.power(velocity_magnitude, 2) * self.DRAG_COEFFICIENT * self.area
            # drag direction = - velocity angle (!Opposite of the velocity angle!)
            drag_direction = -self.velocity / velocity_magnitude
            # F drag = magnitude * direction
            self.drag_force = drag_magnitude * drag_direction

    def update_acceleration(self):
        """Update the acceleration based on net forces and Newton's second law: F = m*a"""
        # F = G + F_drag
        self.update_drag_force()
        force_net = self.weight_force + self.drag_force

        self.acceleration = force_net / self.mass

    def update_velocity(self, time_interval: float):
        """Update velocity based on acceleration using Euler's method v = v + a*t"""
        self.update_acceleration()
        self.velocity = self.velocity + self.acceleration * time_interval

    def update_position(self, time_interval: float):
        """update the position using Euler's method: r = r"""
        self.update_velocity(time_interval)
        self.position = self.position + self.velocity * time_interval

        #stop when the object hits the ground
        if self.position[1] < 0:
            self.position[1] = 0
            self.velocity = np.array([0.0, 0.0])

        self.time += time_interval
        self.store_data()

    def store_data(self):
        """Store the simulation data using np.append and np.vstack for 2d arrays""" 
        self.time_data = np.append(self.time_data, self.time)
        # for 2D positions:
        self.position_data = np.vstack([self.position_data, self.position])
        # for 2D velocities:
        self.velocity_data = np.vstack([self.velocity_data, self.velocity])

def simulate(object: FallingObject, time_interval: float):
    while object.position[1] > 0:
        object.update_position(time_interval)

def visualise(object: FallingObject):
    """visualise a trajectory in matplotlib"""
    plt.style.use("dark_background")

    positions = np.array(object.position_data)

    fig, ax = plt.subplots(figsize = (8,6))

    ax.set_title("Object Trajectory")
    ax.set_xlabel("Horizontal Position (m)")
    ax.set_ylabel("Vertical Position (m)")
    ax.grid()

    ax.plot(positions[: , 0], positions[:, 1], label = "Trajectory")
    ax.legend()
    plt.show()

def main():
    print("example: estimating the time it takes for a body to fall down")

    mass = float(input("input the mass of the object (kg): "))
    height = float(input("input the height at which the object is dropped (meters): "))
    velocity = float(input("input the velocity of the object (m/s): "))
    angle = int(input("Enter the start angle (degrees): "))

    obj = FallingObject(mass, height, velocity, angle, shape="sphere", length=1)

    time_interval = float(input("Enter the desired timespot interval for the simulation (seconds): "))

    simulate(obj, time_interval)

    print()
    print("Simulation complete. ")
    print(f"Final positon: \n{obj.position}")
    print(f"Final velocity: \n{obj.velocity}")
    print()

    visualise(obj)

if __name__ == "__main__":
    main()