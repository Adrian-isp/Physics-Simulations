import numpy as np
import matplotlib.pyplot as plt

"""Gravity simulation module
Works for both 2D and 3D
For Blender visualisation"""

class CelestialBody:
    def __init__(self, mass: int, position_vector: list[int], velocity_vector: list[int], name: str = ""):
        """Units:
        mass - kilograms (kg)
        position - thosands of kilometers (1000 km)
        time - seconds (s)
        velocity - kilometers per second (km/s)
        forces - Newtons (N)"""
        self.name = name

        self.mass = mass

        self.position = np.array(position_vector)
        self.velocity = np.array(velocity_vector)

        #forces are calculated by the simulation
        self.forces = np.zeros_like(self.position)

        self.position_data = np.array([self.position])

    def reset_body(self, position_vector: list[int], velocity_vector: list[int]):
        self.position = np.array(position_vector)
        self.velocity = np.array(velocity_vector)
        
        self.position_data = np.array([self.position])

    def update_acceleration(self):
        """Using Newton's second law
        !requires simulation force data!"""
        #(unit: km/s^2)
        self.acceleration = self.forces / self.mass / 1000 #divide to convert meters to kilometers

    def update_velocity(self, time_step):
        """Update iteratively using Euler's method v = v + a * dt"""
        self.update_acceleration()
        #(unit: km/s)
        self.velocity = self.velocity + self.acceleration * time_step

    def update_position(self, time_step):
        """Update iteratively using Euler's method r = r + v * dt"""
        self.update_velocity(time_step)
        #(unit: 1000km = Mm)
        self.position = self.position + self.velocity * time_step / 1000 #divide to convert km to 1000km

        self.store_data()

    def store_data(self):
        self.position_data = np.vstack([self.position_data, self.position])

class Simulation:
    GRAVITATION = 6.674e-11 #N * m^2 / kg^2

    def __init__(self, bodies: list[CelestialBody]):
        self.bodies = bodies

    def get_gravity_force(self, body1: CelestialBody, body2: CelestialBody):
        """Calculate the gravity between two objects using the law of universal gravitation"""
        r1_vector = body1.position * 1e+6 #convert to meters
        r2_vector = body2.position * 1e+6
        # distance = |r2-r1|
        distance = np.linalg.norm(r1_vector - r2_vector) 

        # force in Newtons N(kg * m / s^2)
        force_magnitude = self.GRAVITATION * body1.mass * body2.mass / np.power(distance, 2)
        # orientation: from body1 to body2
        orientation = (r2_vector-r1_vector) / distance

        return force_magnitude * orientation

    def update_gravity(self):
        """Updates the gravity force for every simulated body"""
        for selected_body in self.bodies:
            selected_body.forces = np.zeros_like(selected_body.forces)
            # update the force for each body to zero and calculate gravity with each other object
            for body in self.bodies:
                if body != selected_body:
                    selected_body.forces = selected_body.forces + self.get_gravity_force(selected_body, body)

    def update_simulation(self, time_step):
        """Time unit: seconds (s)"""
        self.update_gravity()

        for celestial_body in self.bodies:
            celestial_body.update_position(time_step)

    def plot_data_2D(self):
        plt.style.use("dark_background")

        fig, ax = plt.subplots()

        ax.set_title("Gravitational Simulation")
        ax.grid()
        ax.set_xlabel("x distance (Mega meters)")
        ax.set_ylabel("y distance (Mega meters)")

        for body in self.bodies:
            ax.plot(body.position_data[:, 0], body.position_data[:, 1], label = body.name)
        ax.legend()

        plt.show()

    def find_orbital_velocity(self, body1: CelestialBody, body2: CelestialBody):
        """Estimate the value of the orbital velocity (for debugging):"""
        weight_force = np.linalg.norm(self.get_gravity_force(body1, body2)) / 1000 #convert newtons to kg * Km/s^2
        r_distance = np.linalg.norm(body1.position - body2.position) * 1000 #convert Mm to km

        orbital_vel = np.sqrt(weight_force * r_distance / body1.mass)
        print(f"{orbital_vel} km/s")
        

def main():
    sun = CelestialBody(2e+30, position_vector=[0,0], velocity_vector=[0,0], name = "Sun")
    body2 = CelestialBody(0.2e+30, position_vector=[5000, 0], velocity_vector=[0, -51.66], name = "Proxima")
    body3 = CelestialBody(0.1e+30, position_vector=[0, 10000], velocity_vector=[-25.83, 0], name = "Alpha Centauri A")

    celestialBodies = [sun, body2, body3]

    sim1 = Simulation(celestialBodies)
    sim1.find_orbital_velocity(sun, body2)
    sim1.find_orbital_velocity(sun, body3)

    for _ in range(5000):
        sim1.update_simulation(20)

    sim1.plot_data_2D()

if __name__ == "__main__":
    main()