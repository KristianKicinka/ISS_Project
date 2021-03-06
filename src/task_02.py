
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sound_file


def get_frames(signal):
    frames = list()
    block_size = 1024
    overlap = 512

    for frame in range(0, len(signal), overlap):
        frames.append(signal[frame: frame + block_size])

    return frames


def task_2(frames, time_line, sample_frequency):
    # choose correct frame from signal
    my_frame = frames[66]
    show_frames_graph(frames, my_frame, time_line, sample_frequency)
    return my_frame


def show_frames_graph(frames, my_frame, time_line, sample_frequency):
    plt.figure(figsize=(30, 10))
    time_line = np.arange(my_frame.size) / sample_frequency
    plt.plot(time_line, my_frame)
    plt.ylabel('Hodnota []')
    plt.gca().set_xlabel('Čas [s]')
    plt.gca().set_title('Pekný rámec')
    plt.tight_layout()
    plt.show()
