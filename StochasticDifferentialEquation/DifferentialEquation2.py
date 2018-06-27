import numpy as np
import matplotlib.pyplot as plt

def main():
    mue = 1
    sigma = 2

    A = sigma
    B = mue + 0.5 * sigma ** 2

    N = 1000
    T = 1.0
    dt = T / N
    t = np.arange(0, T, dt)

    dW = np.sqrt(dt) * np.random.randn(N)
    dW[0] = 0
    W = np.cumsum(dW)
    Xt = np.exp(A * W + (B - 0.5 * A ** 2) * t)

    Yt = np.zeros(N)
    Yt[0] = 1.0

    for i in range(1, N):
        Yt[i] = Yt[i-1] + B * Yt[i-1] * dt + A * Yt[i-1] * dW[i]

    plt.plot(t, Xt, label = "Analysis")
    plt.plot(t, Yt, label = "Equation")
    plt.xlim(0, T)
    plt.legend()
    plt.show()

main()