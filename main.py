import matplotlib as matplotlib
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import IPython
from scipy.signal import spectrogram, lfilter, freqz, tf2zpk



def load_sound_file():
    global signal, sampl_frekv, time_line
    signal, sampl_frekv = sf.read('xkicin02.wav')
    signal = signal[:250000]
    time_line = np.arange(signal.size) / sampl_frekv

def show_input_graph():
    plt.figure(figsize=(8, 5))
    plt.plot(time_line, signal)
    plt.ylabel('value')
    plt.gca().set_xlabel('time [s]')
    plt.gca().set_title('Vstupný zvukový signál')
    plt.tight_layout()
    plt.show()

def task_1():
    show_input_graph()
    # print max and min values
    max_val = np.max(signal)
    min_val = np.min(signal)
    print(f'Max value is : {max_val}')
    print(f'Min value is : {min_val}')

if __name__ == '__main__':
    load_sound_file()
    task_1()
