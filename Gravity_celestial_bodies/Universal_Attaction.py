import numpy as np
import matplotlib.pyplot as plt

"""
Project: Simulating a trinary Star System
using Newton's Law of Universal Attraction
F = G * m1*m2 / r^2

mass - tons
distance - km
force - Newtons
time - hours
"""
GRAVITATIONAL_CONSTANT = 6.674e-11

class CelestialBody:
    """Define each star object"""
    def __init__(self, mass_tons, position_vector_km = np.array([0, 0]), velocity_vector = np.array([0, 0])):
        """Enter the mass, position and velocity of the body"""
        self.mass = mass_tons
        self.position = np.array([position_vector_km])
        self.velocity = np.array([velocity_vector])

def gravitational_force(Body1: CelestialBody, Body2: CelestialBody):
    """Calculate the gravitational force using: F = G*m1*m2 / r^2"""
    r_vector = Body1.position - Body2.position

    # find modulus of position vectors for the distance
    distance = np.linalg.norm(r_vector)
    if distance == 0:
        return np.array([0, 0])

    # find the gravity magnitude using the formula
    grav_magnitude = GRAVITATIONAL_CONSTANT * Body1.mass * Body2.mass / np.power(distance, 2)

    # orientation: opposite of r_vector
    orientation = - (Body1.position - Body2.position) / distance

    return orientation * grav_magnitude

def update_bodies(bodies: list, time_interval_hours: float):
    # list comprehension
    forces = np.array([np.zeros(2) for _ in bodies])

    # enumerate(list) = [(0, value0), (1, value1)...]
    for i, body1 in enumerate(bodies):
        for j, body2 in enumerate(bodies):
            if i != j:
                forces[i] = forces[i] + gravitational_force(body1, body2)

    for i,body in enumerate(bodies):
        # update velocity: v = v + F/m * dt
        body.velocity = body.velocity + forces[i] * np.power(3600, 2) / body.mass * time_interval_hours /1000 #/1000 - convert to kilometers /3600^2 convert to hours
        # update position: r = r + v * dt
        body.position = body.position + body.velocity * time_interval_hours

def get_Earth_grav_data():
    """for verification"""
    # earth mass = 5.972 * 10^24 kg
    # moon mass = 7.34 * 10^22 kg
    #      distance ~384,000 km
    # sun mass = 1.989 * 10^30 kg
    #     distance ~150,000,000 km

    sun = CelestialBody(2e+27, [0, 149000000])
    earth = CelestialBody(5.972e+21, [0,0])
    moon = CelestialBody(7.34e+19, [384000, 0])

    earth_moon = np.linalg.norm(gravitational_force(earth, moon))
    print(f'Earth-Moon: \n{earth_moon:.2e} Newtons')

    earth_sun = np.linalg.norm(gravitational_force(earth, sun))
    print(f'Earth-Sun: \n{earth_sun:.2e} Newtons')
#get_Earth_grav_data()

def main():
    """Example: earth moon system:"""
    time_step_hours = 0.001 #hour
    num_steps = 3650

    earth = CelestialBody(5.972e+21, [0,0])
    moon = CelestialBody(7.34e+19, [384000, 0])
    bodies = [earth, moon]

    def simulate(time_step_hours, num_steps):
        for i in range(num_steps):
            update_bodies(bodies, time_step_hours)

    simulate(time_step_hours, num_steps)

    print(earth.position)
    print(moon.position)

if __name__ == "__main__":
    main()
