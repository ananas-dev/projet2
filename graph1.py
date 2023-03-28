import numpy as np
import matplotlib.pyplot as plt


def graph1():
    T = 1 * 10**-4
    R = 10**5
    C = 5 * 10**-10
    thau = R*C
    V_0 = 2

    t = np.linspace(0, 3*T, 100)

    V_c = V_0 * (1 - np.exp(-t/thau))

    plt.plot(t, V_c, label="Vc [V]")
    plt.plot(t, np.full_like(t, V_0), "--", label="Vcc [V]")
    plt.xlabel("Temps [s]")
    plt.legend()
    plt.show()


def graph2():
    T = 1 * 10**-4
    R = 10**5
    C = 5 * 10**-10
    thau = R*C
    V_0 = 2
    V_ch = V_0 * (1 - np.exp(-T/(thau * 2)))
    t = np.linspace(0, 3*T, 100)

    V_c = V_ch * np.exp(-t/thau)

    plt.plot(t, V_c,  label="Vc [V]")
    plt.plot(t, np.full_like(t, V_ch), "--", label="Vch [V]")
    plt.xlabel("Temps [s]")
    plt.legend()
    plt.show()


def graph4():
    pR = 10**5
    R = 10**4
    C = 5 * 10**-10
    thau = pR*C
    V_cc = 5
    V_inp1 = V_cc * 2/3
    V_inp2 = V_cc * 1/3

    t = np.linspace(0, 3 * 10**-4, 600)
    V_inm = np.zeros_like(t)
    V_inm_temp = np.zeros_like(t)

    V_inm_temp = V_cc * (1 - np.exp(-t/thau))
    pre_chunk = V_inm_temp[V_inm_temp < V_inp1]
    pcs = len(pre_chunk)
    V_inm[0:pcs] = pre_chunk
    V_inm_temp = V_inp1 * np.exp(-t/thau)
    first_chunk = V_inm_temp[V_inm_temp > V_inp2]
    cs = len(first_chunk)
    V_inm[pcs:pcs+cs] = first_chunk
    V_inm_temp = V_cc + (V_inp2 - V_cc) * np.exp(-t/thau)
    sec_chunk = V_inm_temp[V_inm_temp < V_inp1]
    V_inm[pcs + cs:pcs + 2*cs] = sec_chunk

    V_inm[pcs + 2*cs:pcs + 4 *
          cs] = V_inm[pcs:pcs + 2*cs]
    V_inm[pcs + 4*cs:pcs + 6 *
          cs] = V_inm[pcs:pcs + 2*cs]

    V_out = np.zeros_like(t)
    V_out[0:pcs] = np.full(pcs, V_cc)
    V_out[pcs:pcs+cs] = np.full(cs, V_cc)
    V_out[pcs+2*cs:pcs+3*cs] = np.full(cs, V_cc)
    V_out[pcs+4*cs:pcs+5*cs] = np.full(cs, V_cc)

    V_inp = np.zeros_like(t)
    V_inp[0:pcs] = np.full(pcs, V_inp1)
    V_inp[pcs:pcs+cs] = np.full(cs, V_inp2)
    V_inp[pcs+cs:pcs+2*cs] = np.full(cs, V_inp1)
    V_inp[pcs+2*cs:pcs+3*cs] = np.full(cs, V_inp2)
    V_inp[pcs+3*cs:pcs+4*cs] = np.full(cs, V_inp1)
    V_inp[pcs+4*cs:pcs+5*cs] = np.full(cs, V_inp2)
    V_inp[pcs+5*cs:pcs+6*cs] = np.full(cs, V_inp1)

    plt.plot(t, V_out, label="Vout [V]")
    plt.plot(t, V_inm, label="Vin- [V]")
    plt.plot(t, V_inp, label="Vin+ [V]")

    plt.xlim((0,((pcs + 6 * cs - 1)/600) * 3 * 10**-4))
    plt.xlabel("Temps [s]")
    plt.legend()

    plt.show()


def graph3():
    T = 1 * 10**-4
    R = 10**5
    C = 5 * 10**-10
    thau = R*C
    V_0 = 2
    V_ch = V_0 * (1 - np.exp(-T/(thau * 2)))

    t = np.linspace(0, T, 200)
    V_c = np.zeros_like(t)

    V_c[0:100] = V_0 * (1 - np.exp(-t[0:100]/thau))
    V_c[100:200] = V_ch * np.exp(-t[0:100]/thau)

    plt.plot(t, V_c, label="Vc [V]")
    plt.plot(t, np.full_like(t, V_0), "--", label="V0 [V]")
    plt.plot(t, np.full_like(t, V_ch), "--", label="Vch [V]")
    plt.xlabel("Temps [s]")
    plt.legend()
    plt.show()


def exp2_data():
    # Time Channel A Channel B
    # (us) (V) (V)
    t, V_1, V_2 = np.loadtxt("exp2.csv", unpack=True)

    plt.plot(t, V_1, label="Vout")
    plt.plot(t, V_2, label="Vin+")
    plt.xlabel("Temps [μs]")
    plt.ylabel("Tension [V]")
    plt.xlim(0, 50)
    plt.legend()
    plt.show()


def main():
    #graph4()
    #graph1()
    #graph2()
    graph4()
    #exp2_data()


if __name__ == "__main__":
    main()
