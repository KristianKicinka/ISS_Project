
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal


def task_5(my_frame, signal):

    max_dft_value = max(abs(my_frame))
    frequency_array = scipy.signal.find_peaks(abs(my_frame), (max_dft_value/2))

    frequency_index = []
    for index in range(4):
        frequency_index.append((frequency_array[0][index]*8000)/np.size(my_frame)-1)
        print(f'f{index+1} = {(frequency_array[0][index]*8000)/np.size(my_frame)-1}')

    return frequency_index


