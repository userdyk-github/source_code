import numpy as np
import matplotlib.pyplot as plt

x = np.mgrid[-1:1:100j]
y = lambda x, n : x**2 + np.sin(x**n)

def signal_plot(m):
    fig, axes = plt.subplots(m,m, figsize=(50,50))

    count = 0
    for i in range(m):
        for j in range(m):
            count += 1
            axes[i,j].plot(x, y(x, count))
            axes[i,j].set_title("x**2 + sin(x**{})".format(count))
            axes[i,j].grid()
    plt.show()

signal_plot(5)
