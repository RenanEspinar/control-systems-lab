
import os
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Day 2 — PID Vacuum Pressure Simulation with Engineering Plots
# Biomedical Vacuum Pressure Control System
# ============================================================

# Hardware reference:
# Pump model: PENGPU G4BW12170S
# Supply voltage: 12 V DC
# Control input: PWM
# Feedback signal: speed feedback / tachometer

# Create results folder
os.makedirs("results", exist_ok=True)

# Simulation time
dt = 0.01
t_final = 10
t = np.arange(0, t_final, dt)

# System parameters
a = 10.0   # Pump effect [kPa/s]
b = 0.3    # Leakage coefficient

# PID parameters
Kp = 0.1
Ki = 0.05
Kd = 0.01

# Desired pressure
P_set = -50  # kPa

# Arrays
P = np.zeros_like(t)
u = np.zeros_like(t)
error_array = np.zeros_like(t)

# Initial conditions
integral = 0
prev_error = 0

# Simulation loop
for i in range(1, len(t)):
    error = P_set - P[i - 1]
    error_array[i] = error

    integral += error * dt
    derivative = (error - prev_error) / dt

    control = Kp * error + Ki * integral + Kd * derivative

    # For vacuum control, the control action is inverted
    u[i] = max(0, min(1, -control))

    # Dynamic model
    dPdt = -a * u[i] - b * P[i - 1]
    P[i] = P[i - 1] + dPdt * dt

    prev_error = error

# Plot 1: Pressure response
plt.figure()
plt.plot(t, P, label="Pressure")
plt.axhline(P_set, linestyle="--", label="Setpoint")
plt.title("Vacuum Pressure Response")
plt.xlabel("Time [s]")
plt.ylabel("Pressure [kPa]")
plt.grid()
plt.legend()
plt.savefig("results/pressure_response.png", dpi=300)
plt.show()

# Plot 2: PWM control signal
plt.figure()
plt.plot(t, u, label="PWM signal")
plt.title("Pump PWM Control Signal")
plt.xlabel("Time [s]")
plt.ylabel("PWM duty cycle [0-1]")
plt.grid()
plt.legend()
plt.savefig("results/pwm_control_signal.png", dpi=300)
plt.show()

# Plot 3: Control error
plt.figure()
plt.plot(t, error_array, label="Control error")
plt.title("PID Control Error")
plt.xlabel("Time [s]")
plt.ylabel("Error [kPa]")
plt.grid()
plt.legend()
plt.savefig("results/control_error.png", dpi=300)
plt.show()

print("Simulation completed.")
print("Saved figures in the results/ folder.")
