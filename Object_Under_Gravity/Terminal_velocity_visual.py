import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle, FancyArrow

from falling_object import FallingObject

class Simulation:
    plt.style.use("dark_background")

    def __init__(self, mass, height, length, time_interval: float):
        self.length = length
        self.time_interval = time_interval

        #simulate the falling object
        falling_object = FallingObject(mass, height, length=length)
        self.force_data = []

        while falling_object.position[1] > 0:
            falling_object.update_position(time_interval)
            #add the force_data (gravity, drag)
            self.force_data.append((falling_object.weight_force, falling_object.drag_force))
        
        #extract stored data
        self.force_data = np.array(self.force_data)
        self.height_data = np.array([pos[1] for pos in falling_object.position_data])
        self.time_data = falling_object.time_data
        self.velocity_data = falling_object.velocity_data

    
    def initial_graph(self):
        #Set up the figure and axis
        self.fig, self.ax = plt.subplots(dpi = 100)

        self.ax.set_aspect('equal')
        self.ax.set_title("Free fall simulation")
        self.ax.set_ylabel("Altitude (m)")
        self.ax.grid(color = "#999999", alpha = 0.2)

        #set the limits to only see the object directly
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(self.height_data[0] - 1, self.height_data[0]+1)

        #add a ground plane:
        self.ax.plot((-10, 10), (0, 0), color = "grey")

        #Create the rectangle
        self.rectangle = Rectangle((-self.length/2, self.height_data[0]), 
                                   self.length, self.length,
                                   color = "white")

        self.ax.add_patch(self.rectangle)

        #Create the arrow objects:
        self.weight_arrow = FancyArrow(0, self.height_data[0], 0, self.force_data[0][0][1]/20, color = 'lime', 
                                       width=0.02, head_width=0.05, length_includes_head=True)
        self.drag_arrow = FancyArrow(0, self.height_data[0]+self.length, 0, 0, color = 'red', 
                                     width=0.02, head_width=0.05, length_includes_head=True)
        
        self.ax.add_patch(self.weight_arrow)
        self.ax.add_patch(self.drag_arrow)

        #Add text:
        self.force_text = self.ax.text(-0.8, self.height_data[0]+0.6, "")

        self.fig.savefig("Object_under_gravity/graphics/initial_graph.png")

    def update_frame(self, frame):
        """Update rectangle position, arrows and text for each frame"""
        #update x y coordinates
        self.rectangle.set_xy((-self.length/2, self.height_data[frame]))

        #update the gravity arrow
        weight_force = self.force_data[frame][0][1]
        self.weight_arrow.set_data(x=0, y=self.height_data[frame], dx=0, dy=weight_force / 20) # /20 for visualisation

        #update the drag arrow
        drag_force = self.force_data[frame][1][1]
        self.drag_arrow.set_data(x=0, y=self.height_data[frame]+self.length, dx=0, dy=drag_force / 20)
        
        #update the limit
        self.ax.set_ylim(self.height_data[frame] - 1, self.height_data[frame]+1)

        #update the text placement
        self.force_text.set_position(xy= (-0.9, self.height_data[frame]+0.6))
        self.force_text.set_text(f"Weight: {np.abs(weight_force):.2f} N\nDrag: {np.abs(drag_force):.2f} N\nVelocity: {np.abs(self.velocity_data[frame][1]):.2f} m/s")

        return (self.rectangle, self.weight_arrow, self.drag_arrow)
    
    def animate(self):
        self.initial_graph()

        #create the animation
        frames = len(self.force_data)
        ani = FuncAnimation(self.fig, self.update_frame, frames, interval = self.time_interval * 1000, repeat = True)
        ani.save("Object_under_gravity/graphics/fall_animation.gif", fps = 60, dpi=200)

        plt.show()
        plt.close()

    def final_graph(self):
        self.initial_graph()
        self.rectangle.set_xy((-self.length/2, 0))
        self.ax.set_ylim(-1,1)

        self.weight_arrow.set_data(x=0, y=0, dx=0, dy=self.force_data[-1][0][1] / 20)
        self.drag_arrow.set_data(x=0, y=1, dx=0, dy=0)

        self.fig.savefig("Object_under_gravity/graphics/final_graph.png")
        plt.show()
        plt.close()

    def velocity_graph(self):
        #Set up the figure and axis
        fig, ax = plt.subplots(dpi = 100)

        ax.set_title("Velocity according to time")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Velocity (m/s)")
        ax.grid(color = "#999999", alpha = 0.2)

        ax.set_xlim(-1, np.round(self.time_data[-1])+1)
        ax.set_ylim(-1, np.abs(np.round(self.velocity_data[-2, 1])) + 1)

        #add vertical velocity data plot
        ax.plot(self.time_data[:-1], np.abs(self.velocity_data[:-1,1]), label="v(t)", color = "cyan")
        ax.legend()

        fig.savefig("Object_under_gravity/graphics/velocity_graph")
        plt.show()


sim = Simulation(mass = 1, height = 750, length = 0.1, time_interval = 0.05)
sim.animate()
sim.final_graph()
sim.velocity_graph()