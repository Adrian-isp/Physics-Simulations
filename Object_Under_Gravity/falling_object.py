import numpy as np

class falling_object:
    """
    simulate iteratively an object with mass falling from a height
    using Euler's Method
    
    done: weight force implementation

    to do: drag force, horizontal motion, visualisation
    """
    GRAVITY = 9.81

    def __init__(self, mass: float, height: float, velocity: float = 0, shape: str = "cube", length: float = 1):
        """Initialise the simulation with the mass(kg), height(m) and velocity(m/s)"""
        self.mass = mass
        """calculate weight: G = m*g"""
        self.weight = self.mass * self.GRAVITY

        self.height = height
        self.velocity = velocity

        match shape:
            case "cube":
                self.area = np.pow(length, 2)
                self.DRAG_COEFFICIENT = 1.05
            case "sphere":
                self.area = np.pi * np.pow(length/2, 2)
                self.DRAG_COEFFICIENT = 0.47

        self.time = 0

        """set the data"""
        self.time_data = np.array([self.time])
        self.height_data = np.array([self.height])
        self.velocity_data = np.array([self.velocity])

    def reset(self, height, velocity):
        """Reset the simulation to new conditions"""
        self.height = height
        self.velocity = velocity
        self.time = 0

        self.time_data = np.array([self.time])
        self.height_data = np.array([self.height])
        self.velocity_data = np.array([self.velocity])

    def update_data(self):
        """update data""" 
        self.time_data = np.append(self.time_data, self.time)
        self.height_data = np.append(self.height_data, self.height)
        self.velocity_data = np.append(self.velocity_data, self.velocity)

    def update_drag_force(self):
        """Calculate drag force according to the following formula:
        F_drag = 1/2 * rho * v^2 * C_d * A , where:
        rho - aur density (~1,225 kg/m^3)
        v - velocity of object relative to fluid
        C_d - coefficent of drag (depends on shape)
        A - cross sectional area """
        self.drag_force = 0.5 * 1.225 * np.pow(self.velocity, 2) * self.DRAG_COEFFICIENT * self.area

    def update_acceleration(self):
        """Update the acceleration based on Newton's second law: F = m*a"""
        force_net = -self.weight
        self.acceleration = force_net / self.mass

    def update_velocity(self, time_interval: float):
        """calculate the updated velocity based on acceleration v = v + a*t"""
        self.update_acceleration()
        self.velocity = self.velocity + self.acceleration * time_interval

    def update_height(self, time_interval: float):
        """update the height with the updated vertical velocity h = h + v * t"""
        self.update_velocity(time_interval)
        self.height = self.height + self.velocity * time_interval

        """stop the object from falling through the floor"""
        if self.height < 0:
            self.height = 0
            self.velocity = 0

        self.time += time_interval

        self.update_data()


def simulate(object: falling_object, time_interval: float):
    while object.height > 0:
        object.update_height(time_interval)


def main():
    print("example: estimating the time it takes for a body to fall down")

    mass = float(input("input the mass of the object (kg): "))
    height = float(input("input the height at which the object (meters): "))
    velocity = float(input("input the velocity of the object (m/s): "))

    cube = falling_object(mass, height, velocity)

    time_interval = float(input("Enter the desired timespot interval for the simulation (seconds): "))

    simulate(cube, time_interval)
    
    print("height data: ")
    print(cube.height_data)


if __name__ == "__main__":
    main()