import matplotlib.pyplot as plt

class Formulas:
    plt.style.use("dark_background")

    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.family'] = 'serif'

    def make_plot(self):
        # Create a figure for the formula
        self.fig, self.ax = plt.subplots(figsize=(3, 2), dpi = 200)
        self.ax.axis("off")  # Hide axes

    def make_drag_formula(self):
        """Show the drag_force formula"""
        self.make_plot()
        self.ax.text(0.5, 0.8, r'$F_{drag} = \frac{1}{2} \rho v^2 C_d A$', fontsize = 20, ha = 'center', va = 'center')

        self.fig.savefig("Object_under_gravity/graphics/drag_force.png", transparent=True)
        plt.show()
        
    def drag_explain(self):
        """Add explainations for drag inputs"""
        self.make_plot()
        self.ax.text(0.5, 0.85, r"$\rho$ = air density", fontsize = 20, ha = 'center', va = 'center')
        self.ax.text(0.5, 0.6, r"$v$ = relative velocity", fontsize = 20, ha = 'center', va = 'center')
        self.ax.text(0.5, 0.35, r" $C_d$ = Coefficient of drag", fontsize = 20, ha = 'center', va = 'center')
        self.ax.text(0.5, 0.1, r"$A$ = Cross section area", fontsize = 20, ha = 'center', va = 'center')

        self.fig.savefig("Object_under_gravity/graphics/drag_explain.png", transparent=True)
        plt.show()

    def terminal_vel_condition(self):
        """Add explainations for drag inputs"""
        self.make_plot()
        self.ax.text(0.5, 0.75, "Terminal velocity\ncondition:", fontsize = 20, ha = 'center', va = 'center')
        self.ax.text(0.5, 0.4, r"$|G| = |F_{drag}|$", fontsize = 20, ha = 'center', va = 'center')

        self.fig.savefig("Object_under_gravity/graphics/terminal_velocity_condition.png", transparent=True)
        plt.show()

    def terminal_vel(self):
        self.make_plot()
        self.ax.text(0.5, 0.5, r"$v_t \approx 39.05 \, m/s$", fontsize = 20, ha = 'center', va = 'center')

        self.fig.savefig("Object_under_gravity/graphics/terminal_velocity.png", transparent=True)
        plt.show()



form = Formulas()
form.make_drag_formula()
form.drag_explain()
form.terminal_vel_condition()
form.terminal_vel()