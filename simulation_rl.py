import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def graph1():
    T = 1 * 10**-4
    R = 10**5
    L = 5 * 10**-10
    thau = R*L
    Vcc = 2

    t = np.linspace(0, 5*T, 1000)
    V0 = signal.square(2 * np.pi * 1/T * t) * Vcc/2 + Vcc/2
    V = np.zeros_like(V0)

    for i in range(10):
        if i % 2 == 0:
            if i == 0:
                V[:100] = Vcc * (1 - np.exp(-t[:100]/thau))
            else:
                V[100*i:100*(i+1)] = Vcc * (1 - np.exp(-(t[:100] -
                                                         thau * np.log(1 - V[100*i-1]/Vcc))/thau))
        else:
            V[100*i:100*(i+1)] = Vcc * \
                np.exp((-(t[:100] - thau * np.log(V[100*i-1]/Vcc)))/thau)

    plt.plot(t, V0, label="V0")
    plt.plot(t, V, label="V")
    plt.xlabel("Temps [s]")
    plt.ylabel("Tension [V]")
    plt.legend()
    plt.grid()
    plt.show()


graph1()
