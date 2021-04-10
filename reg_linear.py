import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([3750, 4500, 4700, 5000, 5250]).reshape((-1, 1))
y = np.array([10, 16, 17.5, 20, 22.5])

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

X = np.linspace(3000, 6000, 100)
Y = model.coef_ * X + model.intercept_

plt.plot(X, Y)
plt.show()
