import numpy as np
import matplotlib.pyplot as plt
import random as rand

def main():
    N = 10000
    T = 1.0
    step = float(T / N)
    mue = 0.5
    sigma = 9

    Wt = 0.0
    t = 0.0
    Sx = np.empty(N, float)
    Ex = np.empty(N, float)
    Tx = np.empty(N, float)

    for i in range(N):
        Tx[i] = t
        Wt += sigma * step if rand.randint(0, 1) > 0 else -1 * sigma * step
        Wt += mue * step
        Ex[i] = mue * t
        Sx[i] = Wt
        t += step
        
    plt.plot(Tx, Sx)
    plt.plot(Tx, Ex)
    plt.xlabel("t")
    plt.xlim(0, T)
    plt.ylabel("W(t)")
    plt.show()

main()

