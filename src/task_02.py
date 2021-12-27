
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sound_file


def get_frames():
    frames = list(sound_file.blocks('audio/xkicin02.wav', blocksize=1024, overlap=512))
    return frames


def task_2(frames, time_line, sample_frequency):
    # choose correct frame from signal
    my_frame = frames[66] # 7
    show_frames_graph(frames, my_frame, time_line, sample_frequency)
    return my_frame


def show_frames_graph(frames, my_frame, time_line, sample_frequency):
    plt.figure(figsize=(30, 8))
    time_line = np.arange(my_frame.size) / sample_frequency
    plt.plot(time_line, my_frame)
    plt.ylabel('Hodnota []')
    plt.gca().set_xlabel('Čas [s]')
    plt.gca().set_title('Rámce')
    plt.tight_layout()
    plt.show()
