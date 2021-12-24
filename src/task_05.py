import matplotlib as matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from scipy.signal import spectrogram


def task_5(my_frame,signal):
    print('Task 5')
    max_dft_value = max(abs(my_frame))
    task_5_graf_abs(abs(my_frame))
    frekv_array = scipy.signal.find_peaks(abs(my_frame),(max_dft_value/2))
    #print(frekv_array)
    frekv_index = []
    for index in range(4):
        frekv_index.append((frekv_array[0][index]*8000)/np.size(my_frame)-1)
        print(f'f{index+1} = {(frekv_array[0][index]*8000)/np.size(my_frame)-1}')

    return frekv_index

def task_5_graf_abs(my_frame):
    plt.figure(figsize=(8, 5))
    time_line = np.arange(np.size(np.real(my_frame)))*8000/512
    #split_array[0] = abs(split_array[0])
    plt.plot(time_line, np.real(my_frame))
    plt.ylabel('Hodnota []')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.gca().set_title('Diskrétna fourierova transformácia (DFT) Abs')
    plt.tight_layout()
    plt.show()
