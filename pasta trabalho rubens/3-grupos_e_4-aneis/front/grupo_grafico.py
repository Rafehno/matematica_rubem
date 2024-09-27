import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from back.grupo import grupo_ciclico


def plot_grupo_ciclico(n):
    group_elements = grupo_ciclico(n)
    plt.figure(figsize=(5, 5))
    plt.plot(group_elements, [0] * n, 'bo')  

    for i, elem in enumerate(group_elements):
        plt.text(i, 0.1, f"{elem}", fontsize=12, ha='center')

    plt.xlim(-1, n)
    plt.ylim(-0.5, 1)
    plt.title(f'Grupo Cíclico C_{n}')
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

if __name__ == "__main__":
    plot_grupo_ciclico(6)