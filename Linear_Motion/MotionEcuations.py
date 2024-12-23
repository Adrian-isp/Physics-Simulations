import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('dark_background')
# Set up figure
fig, ax = plt.subplots()
ax.axis('off')  # Turn off axes for clean background

# Add physics formulas
ax.text(0.5, 0.8, r"$v = v_0 + at$", fontsize=24, ha='center', va='center')
ax.text(0.5, 0.6, r"$v^2 = v_0^2 + 2a$", fontsize=24, ha='center', va='center')
#ax.text(0.5, 0.4, r"$d = d_0 + v_0t + \frac{1}{2}at^2$", fontsize=24, ha='center', va='center')

# Save as image
plt.savefig("LinearMotion/formulas_velocity.png", dpi=300, bbox_inches='tight', transparent=True)

plt.show()
plt.close(fig)

fig, ax = plt.subplots()
ax.axis('off')
ax.text(0.5, 0.4, r"$d = d_0 + v_0t + \frac{1}{2}at^2$", fontsize=24, ha='center', va='center')

plt.savefig("LinearMotion/formula_distance.png", dpi=300, bbox_inches='tight', transparent=True)

plt.show()

plt.close(fig)
