import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)
y = x ** 2

df = pd.DataFrame({'x': x, 'y': y})

plt.plot(df['x'], df['y'], color="green", alpha=0.5)
plt.title("Ejemplo")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["y = x^2"])
plt.grid(True)

plt.show()