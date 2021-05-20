# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


def rho(height):
    h = 3.28 * height
    return ((1 - 6.875E-6 * h) ** 5.2561) / (1 - 6.875E-6 * h) * 1.225377


m = 634.7733
e = 0.9
AR = 18
W = m * 4.44822
S = 4.9
K = 1 / (np.pi * AR * e)


def pot_req(vel, h):
    cdo = 0.02256
    cl = 2 * W / (rho(h) * S * pow(vel, 2))
    cdi = pow(cl, 2) * K
    cd = cdo + cdi
    d = cd * rho(h) * pow(vel, 2) * S / 2
    return d * vel * 0.00134


x = np.linspace(1, 80, 500)
y = np.linspace(1500, 4500, 500)

X, Y = np.meshgrid(x, y)
Z = pot_req(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50)
ax.set_xlabel('Velocidade [m/s]')
ax.set_ylabel('Altitude [m]')
ax.set_zlabel('Potência Requerida [HP]')
ax.plot_surface(X, Y, Z, cmap='viridis')

plt.show()
