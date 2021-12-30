
from src.task_01 import *
from src.task_02 import *
from src.task_03 import *
from src.task_04 import *
from src.task_05 import *
from src.task_06 import *
from src.task_07 import *
from src.task_10 import *


def load_sound_file():
    global signal, sample_frequency, time_line, time
    signal, sample_frequency = sound_file.read('../audio/xkicin02.wav')
    time_line = np.arange(signal.size) / sample_frequency
    time = signal.size / sample_frequency

    print(f'count of samples : {signal.size}')
    print(f'FS is : {sample_frequency}')
    print(f'time of records sound : {time} ')


if __name__ == '__main__':
    global signal, sample_frequency, time, frames, found_frequencies, time_line
    load_sound_file()
    task_1(time_line, signal)
    frames = get_frames()
    my_frame = task_2(frames, time_line, sample_frequency)
    my_frame = task_3(my_frame)
    task_4(signal, sample_frequency)
    found_frequencies = task_5(my_frame, signal)
    task_6(found_frequencies, sample_frequency, signal)
    clear_signal = task_7(found_frequencies, sample_frequency, signal)
    task_10(clear_signal, sample_frequency)

