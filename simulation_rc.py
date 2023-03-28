import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def graph1():
    T = 1 * 10**-4
    R = 10**5
    C = 5 * 10**-10
    thau = R*C
    Vcc = 2

    t = np.linspace(0, 20*T, 1000)
    V0 = signal.square(2 * np.pi * 1/T * t) * Vcc/2 + Vcc/2
    Vinm = np.zeros_like(V0)
    Vinp = np.zeros_like(V0)

    bloc = 1000 // (2*20)

    for i in range(2*20):
        if i % 2 == 0:
            Vinp[bloc*i:bloc*(i+1)] = 2/3 * Vcc
            if i == 0:
                Vinm[:bloc] = Vcc * (1 - np.exp(-t[:bloc]/thau))
            else:
                Vinm[bloc*i:bloc*(i+1)] = Vcc * (1 - np.exp(-(t[:bloc] -
                                                         thau * np.log(1 - Vinm[bloc*i-1]/Vcc))/thau))
        else:
            Vinm[bloc*i:bloc*(i+1)] = Vcc * \
                np.exp((-(t[:bloc] - thau * np.log(Vinm[bloc*i-1]/Vcc)))/thau)

            Vinp[bloc*i:bloc*(i+1)] = 1/3 * Vcc

    plt.plot(t, V0, label="Vcc")
    plt.plot(t, Vinm, label="Vin-")
    plt.plot(t, Vinp, label="Vin+")
    plt.xlabel("Temps [s]")
    plt.ylabel("Tension [V]")
    plt.legend()
    plt.grid()
    plt.show()


graph1()
