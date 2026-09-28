# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Hermetic Magnetic Drive & He-Xe Gas Loop Simulation
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Abhishek1033ubuntu/hermetic-vacuum-tribology-drive/blob/main/notebooks/vacuum_tribology_sim.py)
#
# Multi-physics simulation of convective heat extraction and non-conductive barrier torque transfer.

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Configure Matplotlib math rendering
mpl.rcParams['text.usetex'] = False
mpl.rcParams['mathtext.fontset'] = 'cm'

# Domain Setup
time_steps = 300
delta_T_range = np.linspace(10, 350, time_steps)
rpm_range = np.linspace(500, 10000, time_steps)

# Binary He-Xe Mixture Parameters
cp_he_xe = 850.0      # J/(kg*K)
m_dot_he_xe = 0.28    # kg/s
Q_he_xe_kW = (m_dot_he_xe * cp_he_xe * delta_T_range) / 1000.0

# Baseline Pure Helium
cp_pure_he = 5193.0   # J/(kg*K)
m_dot_pure_he = 0.025 # kg/s
Q_pure_he_kW = (m_dot_pure_he * cp_pure_he * delta_T_range) / 1000.0

# Magnetic Drive & Si3N4 Ceramic Barrier
Torque_Nm = 4.5 * np.ones_like(rpm_range)
P_eddy_Si3N4 = np.zeros_like(rpm_range)  # Zero electrical conductivity

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(9, 7))

# Subplot 1: Heat Extraction
axs[0].plot(delta_T_range, Q_pure_he_kW, 'g--', linewidth=2, label=r'Baseline Pure Helium ($\dot{m}=0.025\mathrm{kg/s}$)')
axs[0].plot(delta_T_range, Q_he_xe_kW, 'b-', linewidth=2.5, label=r'Optimized He-Xe Mixture ($\dot{m}=0.28\mathrm{kg/s}$)')
axs[0].set_ylabel(r'Heat Extraction Rate ($\mathrm{kW}$)')
axs[0].set_xlabel(r'Thermal Differential $\Delta T$ ($^\circ\mathrm{C}$)')
axs[0].set_title('Convective Heat Extraction in UHV Thermal Loop')
axs[0].grid(True, ls='--')
axs[0].legend(loc='upper left')

# Subplot 2: Torque & Eddy Loss
ax2 = axs[1].twinx()
axs[1].plot(rpm_range, Torque_Nm, 'b-', linewidth=2, label=r'Magnetic Coupling Torque ($\mathrm{N\cdot m}$)')
ax2.plot(rpm_range, P_eddy_Si3N4, 'r-', linewidth=2, label=r'$\mathrm{Si_3N_4}$ Ceramic Barrier Eddy Loss ($\mathrm{W}$)')
axs[1].set_xlabel(r'Pump Rotational Velocity ($\mathrm{RPM}$)')
axs[1].set_ylabel(r'Torque Capacity ($\mathrm{N\cdot m}$)', color='b')
ax2.set_ylabel(r'Barrier Power Loss ($\mathrm{W}$)', color='r')
ax2.set_ylim(-0.1, 1.0)
axs[1].grid(True, ls='--')

plt.tight_layout()
plt.show()
