import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def graph1():
    T = 1 * 10**-4
    R = 100 * 10**3
    C = 5 * 10**-10
    tau = R*C
    Vcc = 5

    

    t = np.linspace(0, 5*T, 1000)
    V0 = signal.square(2 * np.pi * 1/T * t) * Vcc/2 + Vcc/2
    Vinm = np.zeros_like(V0)
    Vinp = np.zeros_like(V0)

    Vinp[V0==Vcc] = np.full_like(Vinp[V0==Vcc], 2/3*Vcc)
    Vinp[V0==0] = np.full_like(Vinp[V0==0], 1/3*Vcc)

    Vinm[V0 == Vcc] = np.tile(Vcc + (1/3 * Vcc - Vcc) * np.exp(-t[:100]/tau), 5)
    Vinm[V0 == 0] = np.tile(2/3 * Vcc * np.exp(-t[:100]/tau), 5)

    plt.plot(t, V0, label="Vcc")
    plt.plot(t, Vinm, label="Vin-")
    plt.plot(t, Vinp, label="Vin+")
    plt.xlabel("Temps [s]")
    plt.ylabel("Tension [V]")
    plt.legend()
    plt.grid()
    plt.show()


graph1()

