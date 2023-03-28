import numpy as np
import matplotlib.pyplot as plt

def graph1():
    t = np.linspace(0, 10, 100)
    thau = 2
    Vc = 1-np.exp(-t/thau)


def main():
    T = 5
    V_0 = 2
    t = np.linspace(0, 10, 100)
    period_len = np.size(t)/t[-1] * T
    period_mask = np.tile(np.repeat([True, False], period_len), 1)
    V = np.zeros_like(t)
    V[period_mask] = V_0

    print(V)

    print(t)
    print(period_mask)

    plt.plot(t, V)

    plt.show()


if __name__ == "__main__":
    main()
