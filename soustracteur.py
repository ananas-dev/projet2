import matplotlib.pyplot as plt
import numpy as np


def theorique():
    t = np.linspace(0, 100, 1000)
    Vd = np.full_like(t, 5)
    Vs = np.full_like(t, 3)
    Vf = Vd - Vs
    plt.plot(t, Vd, label="Vd")
    plt.plot(t, Vs, label="Vs")
    plt.plot(t, Vf, label="Vf")
    plt.xlabel("Temps [μs]")
    plt.ylabel("Tension [V]")
    plt.ylim(0, 7)
    plt.legend()
    plt.grid()
    plt.show()

def expe():
    # Time Channel A Channel B
    # (us) (V) (V)
    
    t, V_1, V_2 = np.loadtxt("data/lab6-r3r4-10000-r1r2-100ohm_32.csv", unpack=True)
    t2, V_3, V_4 = np.loadtxt("data/lab6-100ohm_32.csv", unpack=True)

    plt.plot(t, V_2, label="Vd")
    plt.plot(t, np.full_like(V_2, 3), label="Vs (théorique)", linestyle="--")
    plt.plot(t, V_1, label="Vf")
    plt.xlabel("Temps [μs]")
    plt.ylabel("Tension [V]")
    plt.ylim(0, 7)
    plt.xlim(0, 100)
    plt.legend()
    plt.grid()
    plt.show()


theorique()
expe()

