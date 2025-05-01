import numpy as np
from euler_explicite import euler_explicite

def schema(sigma, L, f, h, tau, tf):
    n = int(L / h)
    x = np.linspace(0, L, n + 1)
    x_ = x[1:-1]

    U0 = f(x_)

    N = n - 1
    Ah = np.zeros((N, N))
    for j in range(N):
        Ah[j, j] = -2
        if j > 0:
            Ah[j, j - 1] = 1
        if j < N - 1:
            Ah[j, j + 1] = 1
    Ah *= sigma / h**2

    def F(t, U):
        return Ah @ U

    t_vals, y_vals = euler_explicite(F, 0, U0, tau, tf)

    return t_vals, y_vals, x_
