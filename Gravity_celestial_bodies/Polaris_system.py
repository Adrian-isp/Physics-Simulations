import numpy as np
from Gravity_simulation_3D import CelestialBody, Simulation
import pandas as pd

"""Data for the polaris system"""

solar_mass = 2e30 #kg

PolarisAa = CelestialBody(mass = 5.13 * solar_mass, position_vector=[0, 0, 0], velocity_vector=[0, 0, 0], name = "Polaris Aa")
PolarisAb = CelestialBody(mass = 1.31 * solar_mass, position_vector=[-100000, 0, -5000], velocity_vector=[0, 82, 1], name = "Polaris Ab")
PolarisB  = CelestialBody(mass = 1.39 * solar_mass, position_vector=[0, 200000, 150000], velocity_vector=[45, 0, -10], name = "Polaris B")

stars = [PolarisAa, PolarisAb, PolarisB]

sim = Simulation(stars)

sim.find_orbital_velocity(PolarisAb, PolarisAa)
sim.find_orbital_velocity(PolarisB, PolarisAa)

for _ in range(60000):
    sim.update_simulation(1000)

sim.plot_data_2D()

"""save position data in a csv file (million kilometers unit)"""

Aa_data = np.round(PolarisAa.position_data[0::100] / 1000, 3)
Ab_data = np.round(PolarisAb.position_data[0::100] / 1000, 3)
B_data = np.round(PolarisB.position_data[0::100] / 1000, 3)

frame_data = np.arange(1,602)

all_data = np.concatenate((Aa_data, Ab_data, B_data), axis = 1)

print(all_data[-1])

filepath = "Gravity_celestial_bodies/Polaris_data.csv"

data_names = ['PolarisAa_x','PolarisAa_y','PolarisAa_z','PolarisAb_x','PolarisAb_y','PolarisAb_z','PolarisB_x','PolarisB_y','PolarisB_z']

df = pd.DataFrame(all_data, columns=data_names, index=frame_data)

df.to_csv(filepath, header=True, index=True, sep=',')
