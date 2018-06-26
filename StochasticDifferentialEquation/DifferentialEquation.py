import numpy as np
import matplotlib.pyplot as plt

def main():
    # u = 4

    # sigma = u
    # mue = - 0.5 * (u ** 2)

    sigma = 2
    mue = 1

    T = 1.0
    N = 1000
    dt = T / N

    t = np.arange(0.0, T, dt)
    dw = np.sqrt(dt) * np.random.randn(N)
    dw[0] = 0.0
    W = np.cumsum(dw)
    Xt = np.exp( sigma * W + mue * t )

    Yt = np.zeros(N)
    Yt[0] = 1.0
    temp = 0.0;

    for i in range(1, N):
        Yt[i] = Yt[i-1] + (mue + 0.5 * sigma ** 2) * Yt[i-1] * dt + sigma  * Yt[i-1] * dw[i]

    plt.plot(t, Xt, label = "Analytic")
    plt.plot(t, Yt, label = "EM rows")
    plt.legend()
    plt.show()

main()