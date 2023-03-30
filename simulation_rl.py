import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from matplotlib.widgets import Slider


def square_signal(t, f, V):
    return signal.square(2 * np.pi * f * t) * V/2 + V/2

def RL(t, R, L, Vin):
    tau = L/R
    Vcc = np.max(Vin)

    Vout = np.zeros_like(Vin)

    charging = False
    ti = 0

    last_V = 0

    for i in range(np.size(t)):
        if Vin[i] == 0:
            if charging:
                charging = False
                ti = 0
                if i == 0:
                    last_V = 0
                else:
                    last_V = Vout[i-1]
            if i == 0:
                Vout[i] = Vcc * \
                    np.exp((-t[ti])/tau)

            else:
                Vout[i] = Vcc * \
                    np.exp((-(t[ti] - tau * np.log(last_V/Vcc)))/tau)
        else:
            if not charging:
                charging = True
                ti = 0
                if i == 0:
                    last_V = 0
                else:
                    last_V = Vout[i-1]

            Vout[i] = Vcc * (1 - np.exp(-(t[ti] -
                                          tau * np.log(1 - last_V/Vcc))/tau))
    
        ti += 1

    return Vout

def graph1():
    f = 100 # kHz
    R = 200 # Ohm
    L = 0.66 # mH
    Vcc = 5 # V

    t = np.linspace(0, 100 * 10**-6, 1000)
    Vin = square_signal(t, f*10**3, Vcc)
    Vout = RL(t, R, L*10**-3, Vin)
    
    fig, ax = plt.subplots()
    ax.set_title("Simulation WeeMet-all")

    line1, = ax.plot(t * 10**6, Vin, label="Vin")
    line2, = ax.plot(t * 10**6, Vout, label="Vout")
    ax.set_xlabel("Temps [μs]")
    ax.set_ylabel("Tension [V]")
    ax.legend()
    ax.grid()

    fig.subplots_adjust(bottom=0.35)

    axL = fig.add_axes([0.25, 0.2, 0.65, 0.03])
    L_slider = Slider(
        ax=axL,
        label='L [mH]',
        valmin=0.01,
        valmax=10,
        valinit=L,
    )

    axR = fig.add_axes([0.25, 0.15, 0.65, 0.03])
    R_slider = Slider(
        ax=axR,
        label='R [ohm]',
        valmin=200,
        valmax=10_000,
        valinit=R,
    )

    axf = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    f_slider = Slider(
        ax=axf,
        label='f [kHz]',
        valmin=10,
        valmax=100,
        valinit=f,
    )

    def update(val):
        Vin = square_signal(t, f_slider.val * 10**3, Vcc)
        Vout = RL(t, R_slider.val, L_slider.val * 10**-3, Vin)

        line1.set_ydata(Vin)
        line2.set_ydata(Vout)
        fig.canvas.draw_idle()

    L_slider.on_changed(update)
    R_slider.on_changed(update)
    f_slider.on_changed(update)

    plt.show()

def graph2():
    f = 100 # kHz
    R = 200 # Ohm
    L1 = 0.66 # mH
    L2 = 0.86 # mH
    Vcc = 5 # V

    t = np.linspace(0, 100 * 10**-6, 1000)
    Vin = square_signal(t, f*10**3, Vcc)
    Vout1 = RL(t, R, L1*10**-3, Vin)
    Vout2 = RL(t, R, L2*10**-3, Vin)
    

    plt.plot(t * 10**6, Vin, label="Vin")
    plt.plot(t * 10**6, Vout1, label="Vout sans métal")
    plt.plot(t * 10**6, Vout2, label="Vout avec métal")
    plt.xlabel("Temps [μs]")
    plt.ylabel("Tension [V]")
    plt.legend()
    plt.grid()
    plt.savefig("results/RL_simu.svg")

    plt.show()

def graph3():
    # Time Channel A Channel B
    # (us) (V) (V)
    
    t, V_1, V_2 = np.loadtxt("data/s7-metal_32.csv", unpack=True)
    t2, _, V_3 = np.loadtxt("data/s7-oscillateur-rien_32.csv", unpack=True)

    # Quick hack start at 0
    t += -t[0]

    plt.plot(t, V_1, label="Vin")
    plt.plot(t, V_2, label="Vout sans métal")
    plt.plot(t, V_3, label="Vout avec métal")

    plt.xlabel("Temps [μs]")
    plt.ylabel("Tension [V]")
    plt.ylim(0, 6.5)
    plt.grid()
    plt.legend()
    plt.savefig("results/RL_experimental.svg")
    plt.show()

graph2()
graph3()
