
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import tf2zpk


def task_8(b, a, index):
    z, p, k = tf2zpk(b, a)

    plt.figure(figsize=(12, 11.5))
    plt.title(f'Zobrazenie nulov a pólov filtra frekvencie f{index}')

    # jednotková kružnica
    ang = np.linspace(0, 2 * np.pi, 100)
    plt.plot(np.cos(ang), np.sin(ang))

    # nuly, poly
    plt.scatter(np.real(z), np.imag(z), marker='o', facecolors='none', edgecolors='r', label='nuly')
    plt.scatter(np.real(p), np.imag(p), marker='x', color='g', label='póly')

    plt.gca().set_xlabel('Reálna zložka $\mathbb{R}\{$z$\}$')
    plt.gca().set_ylabel('Imaginárna zložka $\mathbb{I}\{$z$\}$')

    plt.grid(alpha=0.5, linestyle='--')
    plt.legend(loc='upper left')

    plt.tight_layout()
