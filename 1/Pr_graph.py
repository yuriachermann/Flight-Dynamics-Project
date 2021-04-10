import numpy as np
import matplotlib.pyplot as plt
from performance import pot_req


X = np.linspace(1, 81, 80)
Y1 = pot_req(X, 0)
Y2 = pot_req(X, 900)
Y3 = pot_req(X, 1800)
Y4 = pot_req(X, 2700)
Y5 = pot_req(X, 3600)
Y6 = pot_req(X, 4500)
y = [Y1, Y2, Y3, Y4, Y5, Y6]

for Y in y:
    plt.plot(X, Y)

# Y = pot_req(X, 2600)
# plt.plot(X, Y)

plt.xlim([0, 80])
plt.ylim([0, 30])
plt.xlabel("velocidade")
plt.ylabel("potencia requerida")
plt.grid(True)
plt.show()
