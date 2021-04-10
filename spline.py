from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np


def spl3System(x, y):
    assert (x.shape == y.shape), "spl3System: x e y não possuem o mesmo número de elementos"

    n = len(x) - 1

    M = np.zeros([n + 1, n + 1], dtype=float)
    r = np.zeros(n + 1, dtype=float)

    for i in range(1, n):
        r[i] = 3 * ((y[i + 1] - y[i]) / (x[i + 1] - x[i]) - (y[i] - y[i - 1]) / (x[i] - x[i - 1]))
        M[i, i + 1] = x[i + 1] - x[i]
        M[i, i - 1] = x[i] - x[i - 1]
        M[i, i] = 2 * (M[i, i + 1] + M[i, i - 1])

    M[0, 0] = 1
    M[-1, -1] = 1

    return M, r


def spl3Coeff(x, y):
    n = len(x) - 1

    a = np.zeros(n, dtype=float)
    b = np.zeros(n, dtype=float)
    c = np.zeros(n, dtype=float)
    d = np.zeros(n, dtype=float)

    M, r = spl3System(x, y)

    vet = np.linalg.solve(M, r)

    for i in range(n):
        h = (x[i + 1] - x[i])
        a[i] = y[i]
        c[i] = vet[i]
        d[i] = (vet[i + 1] - vet[i]) / (3 * h)
        b[i] = ((y[i + 1] - y[i]) / h) - vet[i] * h - d[i] * h ** 2

    return a, b, c, d


def spl3EvalS(a, b, c, d, x, z):  # ESSA FOI PORRA!

    assert (z >= x[0] and z <= x[-1]), "spl3EvalS: O ponto está fora do intervalo de interpolação"

    n = len(x) - 1

    p = 0

    for i in range(n):

        if (z >= x[i] and z <= x[i + 1]):
            p = i

    return a[p] + b[p] * (z - x[p]) + c[p] * (z - x[p]) ** 2 + d[p] * (z - x[p]) ** 3


x, y = np.loadtxt("ferrari.txt", unpack=True)

f = interp1d(x, y, kind='cubic')

t = np.linspace(x[0], x[-1], 100000)

plt.plot(t, -f(t), "r")

a, b, c, d = spl3Coeff(x, y)

X = np.linspace(x[0], x[-1], 1000)

Y = np.zeros(1000)

for i in range(1000):
    Y[i] = spl3EvalS(a, b, c, d, x, X[i])

plt.plot(X, -Y, "g")

plt.plot(x, -y, '.')