#!/usr/bin/env python3
"""
Darcy.py
Simple Darcy flow calculation and plot.

Calculates Q = K * i * A and plots a point where x=K and y=i,
annotating the point with the computed flow Q (m^3/s).
"""

import matplotlib.pyplot as plt

# --------------------------
# User-editable variables
# --------------------------
K = 1e-5       # Hydraulic conductivity (m/s) -- change as needed
i = 0.01       # Hydraulic gradient (unitless) -- change as needed
A = 0.1        # Cross-sectional area (m^2) -- change as needed
# --------------------------

# Calculate Darcy flow (m^3/s)
Q = K * i * A

# Print result to console
print(f"Hydraulic conductivity K = {K} m/s")
print(f"Hydraulic gradient i = {i}")
print(f"Cross-sectional area A = {A} m^2")
print(f"Darcy flow Q = {Q:.6e} m^3/s")

# Plot K (x) vs i (y) as a single point and annotate with Q
plt.figure(figsize=(6, 4))
plt.scatter([K], [i], s=80, color='tab:blue')
plt.xlabel("Hydraulic conductivity K (m/s)")
plt.ylabel("Hydraulic gradient i (unitless)")
plt.title("Darcy flow (point): x=K, y=i")

# Annotate the point with the Q value
plt.annotate(f"Q = {Q:.3e} m^3/s", xy=(K, i), xytext=(10, 10), textcoords="offset points",
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.8))

plt.grid(True)
plt.tight_layout()
plt.show()