import numpy as np
import matplotlib.pyplot as plt

"""4 cycle piston engine cycle simulation
car model: BMW M8-competition
engine model: BMW S63B44T4 V8 twin-turbo

Goal: model iteratively an engine cycle
visualise it later in Blender
"""

class Piston:
    #constants:
    Gas_constant = 8.3145 #J/mol*K
    #c_p = 7/2; c_v = 5/2; gamma = c_p/c_v
    Adiabatic_coefficient_air = 1.4
    Temperature_ambient = 300 #K
    Pressure_boost = 1.7e5

    def __init__(self, stroke_length: float, bore_length: float, compression_ratio: float, cycle_time: int, turbocharger: bool = True):
        """Stroke/bore length - milimeters (mm); cycle time - miliseconds (ms)"""
        self.max_volume = stroke_length / 1e3 * np.pi * np.power(bore_length/2, 2) / 1e6
        self.volume_min = self.max_volume / compression_ratio
        self.pressure_min = 101325 + self.Pressure_boost if turbocharger==True else 101325

        self.cycle_time = cycle_time

        #get the max fuel quantity in piston (mols) n = pV / RT
        self.max_quantity = self.pressure_min * self.max_volume / self.Temperature_ambient / self.Gas_constant

        #start data:
        self.volume = self.volume_min
        self.pressure = self.pressure_min
        self.temperature = self.Temperature_ambient
        self.quantity = self.max_quantity / compression_ratio
        self.time = 0

        #initialise storage:
        self.volume_data = np.array([self.volume])
        self.pressure_data = np.array([self.pressure])
        self.temperature_data = np.array([self.temperature])

    def reset(self):
        self.volume_data = np.array([self.volume])
        self.pressure_data = np.array([self.pressure])
        self.temperature_data = np.array([self.temperature])
        self.time = 0

    def update_piston_volume(self):
        """find the piston volume based on the crankshaft movement"""
        self.volume = self.volume_min + (self.max_volume - self.volume_min) * (1 - np.cos( 2* np.pi * self.time / self.cycle_time )) / 2

    def intake_stroke_update(self, time_interval):
        """realise the intake transformation, adding air-fuel mixture"""

        #update time
        self.time = self.time + time_interval
        self.update_piston_volume()

        self.quantity = self.max_quantity * self.volume / self.max_volume

        self.store_data()

    def compression_stroke_update(self, time_interval):
        """Update the compression stroke (adiabatic compression)"""
        vi = self.volume

        #update the time
        self.time = self.time + time_interval
        self.update_piston_volume()

        #update adiabatic compression: p2 = p1 * (V1/V2)^gamma
        self.pressure = self.pressure * np.power(vi / self.volume, self.Adiabatic_coefficient_air)

        #temperature from ideal gas law: T = pV / nR
        self.temperature = self.pressure * self.volume / (self.quantity * self.Gas_constant)

        self.store_data()

    def ignition(self):
        """isochoric ignition transformation with heat (instant)"""
        heat_per_cycle = 900 #J
        #calculate using internal energy dU = dQ
        self.temperature = self.temperature + 0.4 * heat_per_cycle / (self.quantity * self.Gas_constant)

        #update pressure 
        self.pressure = self.quantity * self.Gas_constant * self.temperature / self.volume

        self.store_data()

    def depressurise(self):
        self.temperature = self.Temperature_ambient
        self.pressure = self.pressure_min
        self.volume = self.max_volume

        self.store_data()

    def simulate_cycle(self, stroke_timesteps: int):
        """Make a full engine cycle"""
        time_interval: float = self.cycle_time / stroke_timesteps / 2.0

        #intake stroke:
        for i in range(stroke_timesteps):
            self.intake_stroke_update(time_interval)

        #compression stroke:
        for i in range(stroke_timesteps):
            self.compression_stroke_update(time_interval)

        #ignition
        self.ignition()
        #power/expansion stroke, same as compression stroke
        for i in range(stroke_timesteps):
            self.compression_stroke_update(time_interval)

        #cool and depresurise
        self.depressurise()
        #exhaust stroke(same as intake stroke)
        for i in range(stroke_timesteps):
            self.intake_stroke_update(time_interval)

    def display_cycle(self, stroke_timesteps: int):
        """Display the data in a pressure volume graph"""
        self.reset()
        self.simulate_cycle(stroke_timesteps)

        plt.style.use("dark_background")

        x_data = self.volume_data * 1e6
        y_data = self.pressure_data / 1e5

        fig, ax = plt.subplots()

        ax.set_title("Pressure Volume graph")
        ax.set_xlabel("Volume (cm^32)")
        ax.set_ylabel("Pressure (bar)")
        ax.grid()

        ax.plot(x_data, y_data, color = "cyan")

        plt.show()

    def get_work(self, stroke_timesteps: int):
        """calculate total work of a cycle in Joules"""
        self.reset()
        self.simulate_cycle(stroke_timesteps)

        v = self.volume_data
        p = self.pressure_data
        self.work = 0

        for i in range(len(self.volume_data) - 1):
            if v[i] != v[i+1]:
                self.work += (p[i]+p[i+1]/2) * (v[i+1] - v[i])

        print("Total work of one piston cycle is:")
        print(f"{self.work:.2f} Joules")

    def get_power(self, stroke_timesteps:int, piston_number):
        """calculate the power of a car with the work(J), cycle time(ms) and number of pistons:"""
        self.reset()
        self.get_work(stroke_timesteps)

        cycle_seconds = self.cycle_time / 1000
        engine_work = self.work * piston_number

        #calculate power in Watts
        engine_power = engine_work / cycle_seconds

        print(f"Engine power in watts: {engine_power:.2f}")
        print(f"Engine power in horsepower: {engine_power / 745 :.2f}")

    def store_data(self):
        self.volume_data = np.append(self.volume_data, self.volume)
        self.pressure_data = np.append(self.pressure_data, self.pressure)
        self.temperature_data = np.append(self.temperature_data, self.temperature)

s63 = Piston(89, 88.3, 10, cycle_time = 16, turbocharger = True)

stroke_timesteps = 200

s63.display_cycle(stroke_timesteps)

s63.get_power(stroke_timesteps, 8)