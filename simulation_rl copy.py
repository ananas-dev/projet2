import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from matplotlib.widgets import Slider


def simulate(T, R, L, Vcc):
    tau = L/R

    t = np.linspace(0, 5*T, 1000)
    V0 = signal.square(2 * np.pi * 1/T * t) * Vcc/2 + Vcc/2
    V = np.zeros_like(V0)

    Vh = Vcc * np.exp(-T/(2 * tau))
    Vl = Vcc * (1 - np.exp(-T/(2 * tau)))

    #V[V0 == Vcc] = np.tile(Vcc *(1 - np.exp(-t[:100]/tau) * (1-Vh/Vcc)**(-1/tau)), 5)
    V[V0 == 0] = np.tile(Vcc * np.exp(-(t[:100] - tau*np.log(Vl/Vcc)/tau)/tau), 5)

    return t, V, V0


def graph1():
    T = 1 * 10**-4
    R = 10**5
    L = 1 * 10**-2
    Vcc = 2

    t, V, V0 = simulate(T, R, L, Vcc)

    fig, ax = plt.subplots()
    line1, = ax.plot(t, V0, label="V0")
    line2, = ax.plot(t, V, label="V")
    ax.set_xlabel("Temps [s]")
    ax.set_ylabel("Tension [V]")
    ax.legend()
    ax.grid()

    fig.subplots_adjust(bottom=0.25)

    axL = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    L_slider = Slider(
        ax=axL,
        label='L [H]',
        valmin=0.0001,
        valmax=5,
        valinit=L,
    )

    def update(val):
        t, V, V0 = simulate(T, R, L_slider.val, Vcc)

        line1.set_ydata(V0)
        line2.set_ydata(V)
        fig.canvas.draw_idle()

    L_slider.on_changed(update)

    plt.show()


graph1()
