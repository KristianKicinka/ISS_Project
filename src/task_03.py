import matplotlib as matplotlib
import matplotlib.pyplot as plt
import numpy as np


def task_3(my_frame):
    N = my_frame.size
    omega = np.exp((-2 * np.pi * 1j) / N)
    r = np.arange(N)
    w_matrix = np.vander(omega ** r, increasing=True)
    my_frame = w_matrix @ my_frame
    # frames[7] = np.fft.fft(frames[7])
    my_frame = task_3_graf(my_frame)
    return my_frame


def task_3_graf(my_frame):
    plt.figure(figsize=(8, 5))
    split_array = np.split(my_frame, 2)
    time_line = np.arange(np.size(np.real(split_array[0])))*8000/512
    #split_array[0] = abs(split_array[0])
    plt.plot(time_line, np.real(split_array[0]))
    plt.ylabel('Hodnota []')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.gca().set_title('Diskrétna fourierova transformácia (DFT)')
    plt.tight_layout()
    plt.show()
    return split_array[0]
