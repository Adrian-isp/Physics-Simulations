import matplotlib.pyplot as plt
from matplotlib import style 

style.use("dark_background")

# Enable LaTeX in Matplotlib
plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "serif"

# Create a figure for the formula
fig, ax = plt.subplots(figsize=(6, 2))
ax.axis("off")  # Hide axes

# Add a LaTeX formula
formula = r"$y(t) = v_{y0}t - \frac{1}{2} g t^2$"
ax.text(0.5, 0.55, formula, fontsize=24, ha="center", va="center")
ax.text(0.5, 0.8, r"$x(t) = v_{x0}t$", fontsize = 24, ha = "center", va = "center")

ax.text(0.5, 0.15, r"$v_y(t) = v_{y0} - gt$", fontsize = 24, ha = "center", va = "center")

# Save the image
plt.savefig("ProjectileMotion/dist_formula.png", dpi=300, bbox_inches="tight", transparent=True)
plt.show()
plt.close()

"""write the basic velocity formulas"""
fig, ax = plt.subplots(figsize = (6, 2))
ax.axis("off")

ax.text(0.35, 0.8, r"$v_0 = 100 m/s$", fontsize = 20, ha = "center", va = "center")
ax.text(0.65, 0.8, r"$\theta = 75 ^{\circ}$", fontsize = 20, ha = "center", va = "center")

plt.savefig("ProjectileMotion/starter_conditions.png", dpi=300, bbox_inches="tight", transparent=True)
plt.show()
plt.close()

fig, ax = plt.subplots(figsize = (6, 2))
ax.axis("off")

ax.text(0.5, 0.5, r"$v_{x0} = v_0 sin \theta$", fontsize = 20, ha = "center", va = "center")
ax.text(0.5, 0.3, r"$v_{y0} = v_0 cos \theta$", fontsize = 20, ha = "center", va = "center")

plt.savefig("ProjectileMotion/v_x_v_y.png", dpi=300, bbox_inches="tight", transparent=True)
plt.show()
plt.close()

"""
from here it doesn't work

fig, ax = plt.subplots(figsize = (6, 2))
ax.axis("off")

ax.text(0.5, 0.6, r"$y_{max} = \frac {v_{y0}^2} {2g}$", fontsize = 20, ha = "center", va = "center")
ax.text(0.5, 0.4, r"$t_{total} = \frac {2 v_{y0}} {g}", fontsize = 20, ha = "center", va = "center")

plt.savefig("ProjectileMotion/final.png", dpi=300, bbox_inches="tight", transparent=True)
plt.show()
plt.close()"""