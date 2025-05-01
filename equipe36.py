import numpy as np
import matplotlib.pyplot as plt
from schema import schema


sigma = 1
L = 1
f = lambda x: np.sin(np.pi * x)
u_exact = lambda x, t: np.exp(-np.pi**2 * t) * np.sin(np.pi * x)
h = 0.1

def tracer(tau):
    tf = 1
    t_vals, y_vals, x_interior = schema(sigma, L, f, h, tau, tf)

    temps = [0, 0.05, 0.1, 1]
    indices = [np.argmin(np.abs(t_vals - t)) for t in temps]

    plt.figure(figsize=(10, 6))
    for t, idx in zip(temps, indices):
        u_num = y_vals[:, idx]
        u_th = u_exact(x_interior, t)
        plt.plot(x_interior, u_th, '--', label=f"Exacte t={t}")
        plt.plot(x_interior, u_num, label=f"Numérique t={t}")

    plt.title(f"Comparaison numérique vs exacte (tau = {tau})")
    plt.xlabel("x")
    plt.ylabel("Température u(x,t)")
    plt.legend()
    plt.grid(True)
    plt.show()


tracer(0.01)
tracer(0.001)
