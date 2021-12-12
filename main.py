import matplotlib as matplotlib
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import IPython
from scipy.signal import spectrogram, lfilter, freqz, tf2zpk



def load_sound_file():
    global signal, sampl_frekv, time_line, time

    signal, sampl_frekv = sf.read('xkicin02.wav')
    time_line = np.arange(signal.size) / sampl_frekv
    time = signal.size / sampl_frekv

    print(f'count of samples : {signal.size}')
    print(f'FS is : {sampl_frekv}')
    print(f'time of recordes sound : {time} ')

def show_input_graph():
    plt.figure(figsize=(8, 5))
    plt.plot(time_line, signal)
    plt.ylabel('value')
    plt.gca().set_xlabel('time [s]')
    plt.gca().set_title('Vstupný zvukový signál')
    plt.tight_layout()
    plt.show()

def show_frames_graph():
    plt.figure(figsize=(30, 8))
    time_line = np.arange(frames[7].size) /sampl_frekv
    plt.plot(time_line, frames[7])
    plt.ylabel('value')
    plt.gca().set_xlabel('time [s]')
    plt.gca().set_title('Rámce')
    plt.tight_layout()
    plt.show()

def task_1():
    show_input_graph()
    # print max and min values
    max_val = np.max(signal)
    min_val = np.min(signal)
    print(f'Max value is : {max_val}')
    print(f'Min value is : {min_val}')

def task_2():
    # choose correct frame from signal
    global frames
    frames = list(sf.blocks('xkicin02.wav',blocksize=1024,overlap=512))
    show_frames_graph()

if __name__ == '__main__':
    load_sound_file()
    task_1()
    task_2()
