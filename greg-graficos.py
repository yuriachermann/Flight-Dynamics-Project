import matplotlib.pylab as plt
import numpy as np

W = 3420  # Peso da aeronave em N
S = 4.891  # Área molhada da asa
v = np.linspace(0, 80, 9)
vel = np.linspace(0, 90, 10)
v[0] = 5
Wa = np.array((2.5, 10, 16.05, 20.5, 23, 24.5, 25.2, 25.6, 25.9)) * 745.7
nprop = np.array((0, 30.5, 54.5, 70, 77.5, 81, 82, 83, 84, 85))
Cd_0 = np.array((0.03718, 0.03240, 0.02843, 0.02642, 0.02512, 0.02416, 0.02342, 0.02282, 0.02231))
Cld = 0.5984 / 0.03296


def Cd0(V):
    if (V == 5):
        return 0.03718
    if (V == 10):
        return 0.03240
    if V == 20:
        return 0.02843
    if V == 30:
        return 0.02642
    if V == 40:
        return 0.02512
    if V == 50:
        return 0.02416
    if V == 60:
        return 0.02342
    if V == 70:
        return 0.02282
    if V == 80:
        return 0.02231
    else:
        return 0


def rho(height):
    H = 3.28 * height
    return ((1 - 6.875E-6 * H) ** 5.2561) / (1 - 6.875E-6 * H) * 1.225377  # Densidade do ar a altitude height em kg/m³


def CL(V, height):
    return (2 * W) / (rho(height) * S * V ** 2)  # Coeficiente CL


def Cd_i(V, height):  # Função CD_i recebe velocidade em m/s e altitude H em m
    K = 1 / (np.pi * 0.9 * 18)  # Constante K
    H = 3.28 * height  # Converte de metro para pés

    return K * (CL(V, height) ** 2)


def Cd(V, height):
    return Cd_i(V, height) + Cd0(V)


def Pot_req(V, height):
    return W * Cd(V, height) / CL(V, height) * V


potrequerida0m = np.zeros(len(v))
potrequerida500m = np.zeros(len(v))
potrequerida1000m = np.zeros(len(v))
potrequerida2000m = np.zeros(len(v))
potrequerida3000m = np.zeros(len(v))
potrequerida4000m = np.zeros(len(v))
potrequerida4500m = np.zeros(len(v))
potrequerida0m[0] = Pot_req(5, 0)
potrequerida500m[0] = Pot_req(5, 500)
potrequerida1000m[0] = Pot_req(5, 1000)
potrequerida2000m[0] = Pot_req(5, 2000)
potrequerida3000m[0] = Pot_req(5, 3000)
potrequerida4000m[0] = Pot_req(5, 4000)
potrequerida4500m[0] = Pot_req(5, 4500)

for i in range(1, 9):
    potrequerida0m[i] = Pot_req(10 * i, 0)
    potrequerida500m[i] = Pot_req(10 * i, 500)
    potrequerida1000m[i] = Pot_req(10 * i, 1000)
    potrequerida2000m[i] = Pot_req(10 * i, 2000)
    potrequerida3000m[i] = Pot_req(10 * i, 3000)
    potrequerida4000m[i] = Pot_req(10 * i, 4000)
    potrequerida4500m[i] = Pot_req(10 * i, 4500)

plt.plot(v, potrequerida0m)
plt.plot(v, potrequerida500m)
plt.plot(v, potrequerida1000m)
plt.plot(v, potrequerida2000m)
plt.plot(v, potrequerida3000m)
plt.plot(v, potrequerida4000m)
plt.plot(v, potrequerida4500m)
plt.plot(v, Wa)
plt.ylabel("Potência [W]")
plt.xlabel("Velocidade [m/s]")
plt.grid()
plt.show()

plt.plot(vel, nprop)
plt.grid()
plt.xlabel("Velocidade [m/s]")
plt.ylabel("nprop %")
plt.show()

plt.plot(v, Wa)
plt.ylabel("Potência disponível [W]")
plt.xlabel("Velocidade [m/s]")
plt.grid()
plt.show()
