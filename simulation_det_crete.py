import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from matplotlib.widgets import Slider

def simulate(T, R, C, Vcc, reverse):
    thau = R*C

    t = np.linspace(0, 5*T, 1000)
    V0 = np.tile(signal.windows.triang(1000/5), 5) * Vcc
    V = np.zeros_like(V0)

    t_i = 0

    charging = True
    starting_val = 0

    for i in range(1000):
        if V0[i] < reverse:
            if not charging:
                t_i = 0
                charging = True

            V[i] = Vcc * \
                np.exp((-(t[t_i] - thau * np.log(V[i-t_i-1]/Vcc)))/thau)

        else:
            if charging:
                t_i = 0
                charging = False

            V[i] = Vcc * (1 - np.exp(-(t[t_i] -
                                       thau * np.log(1 - V[i-t_i-1]/Vcc))/thau))

        t_i += 1

    return t, V, V0


def graph1():
    T = 1 * 10**-4
    R = 500
    C = 5 * 10**-10
    Vcc = 2
    reverse = 1.9 # Seuil de la diode en reverse

    t, V, V0 = simulate(T, R, C, Vcc, reverse)

    plt.plot(t, V0, label="V0")
    plt.plot(t, V, label="V")
    plt.xlabel("Temps [s]")
    plt.ylabel("Tension [V]")
    plt.legend()
    plt.grid()

    plt.show()


graph1()
