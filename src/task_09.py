import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import freqz


def task_9(b, a, sample_frequency, index):
    w, H = freqz(b, a)

    _, ax = plt.subplots(1, 2, figsize=(12, 3))

    ax[0].plot(w / 2 / np.pi * sample_frequency, np.abs(H))
    ax[0].set_xlabel('Frekvencia [Hz]')
    ax[0].set_title('Modul frekvenčnej charakteristiky pre f' + str(index) + ' $|H(e^{j\omega})|$')

    ax[1].plot(w / 2 / np.pi * sample_frequency, np.angle(H))
    ax[1].set_xlabel('Frekvencia [Hz]')
    ax[1].set_title('Argument frekvenčnej charakteristiky pre f' + str(index) + ' $\mathrm{arg}\ H(e^{j\omega})$')

    for ax1 in ax:
        ax1.grid(alpha=0.5, linestyle='--')

    plt.tight_layout()
