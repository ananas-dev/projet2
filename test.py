import numpy as np
from scipy import signal, integrate
import matplotlib.pyplot as plt

# Define the circuit parameters
L = 1  # inductance (H)
R = 10  # resistance (ohm)

# Define the sampling frequency and duration of the signal
fs = 1000  # Hz
duration = 1  # seconds

# Generate a square wave with a frequency of 10 Hz
t = np.arange(0, duration, 1/fs)
square_wave = signal.square(2*np.pi*10*t)

# Define the function that describes the behavior of the RL circuit
def rl_circuit(i, t):
    return (square_wave[t] - L/R * i) / L

# Integrate the differential equation that describes the behavior of the circuit
initial_condition = 0
i = integrate.odeint(rl_circuit, initial_condition, t)[:,0]

# Plot the input square wave and the resulting current through the RL circuit
fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(t, square_wave)
ax[0].set_ylabel('Input Voltage')
ax[1].plot(t, i)
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('Current (A)')
ax[1].set_ylim([-1, 1])
plt.show()