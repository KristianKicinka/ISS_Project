import matplotlib as matplotlib
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sound_file
import IPython
from scipy.signal import spectrogram, lfilter, freqz, tf2zpk
from src.task_01 import *
from src.task_02 import *
from src.task_03 import *
from src.task_04 import *
from src.task_05 import *
from src.task_06 import *
from src.task_07 import *
from src.task_10 import *



def load_sound_file():
    global signal, sample_frekvency, time_line, time
    signal, sample_frekvency = sound_file.read('audio/xkicin02.wav')
    time_line = np.arange(signal.size) / sample_frekvency
    time = signal.size / sample_frekvency

    print(f'count of samples : {signal.size}')
    print(f'FS is : {sample_frekvency}')
    print(f'time of recordes sound : {time} ')


if __name__ == '__main__':
    global signal, sample_frekvency, time, frames, found_frekvencies, time_line
    load_sound_file()
    task_1(time_line, signal)
    frames = get_frames()
    my_frame = task_2(frames, time_line, sample_frekvency)
    my_frame = task_3(my_frame)
    task_4(signal, sample_frekvency)
    found_frekvencies = task_5(my_frame, signal)
    task_6(found_frekvencies, sample_frekvency, signal)
    clear_signal = task_7(found_frekvencies, sample_frekvency, signal)
    task_10(clear_signal, sample_frekvency)

