import matplotlib as matplotlib
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import IPython
from scipy.signal import spectrogram, lfilter, freqz, tf2zpk



def load_sound_file():
    global signal, sample_frekv, time_line, time

    signal, sample_frekv = sf.read('xkicin02.wav')
    time_line = np.arange(signal.size) / sample_frekv
    time = signal.size / sample_frekv

    print(f'count of samples : {signal.size}')
    print(f'FS is : {sample_frekv}')
    print(f'time of recordes sound : {time} ')

def show_input_graph():
    plt.figure(figsize=(8, 5))
    plt.plot(time_line, signal)
    plt.ylabel('Hodnota []')
    plt.gca().set_xlabel('čas [s]')
    plt.gca().set_title('Vstupný zvukový signál')
    plt.tight_layout()
    plt.show()

def show_frames_graph():
    plt.figure(figsize=(30, 8))
    time_line = np.arange(my_frame.size) /sample_frekv
    plt.plot(time_line, my_frame)
    plt.ylabel('Hodnota []')
    plt.gca().set_xlabel('Čas [s]')
    plt.gca().set_title('Rámce')
    plt.tight_layout()
    plt.show()

def task_1():
    # print max and min values
    max_val = np.max(signal)
    min_val = np.min(signal)
    print(f'Max value is : {max_val}')
    print(f'Min value is : {min_val}')
    # show_input_graph()

def task_2():
    # choose correct frame from signal
    global frames, my_frame
    frames = list(sf.blocks('xkicin02.wav',blocksize=1024,overlap=512))
    my_frame = frames[7]
    #show_frames_graph()

def task_3():
    global my_frame

    N = my_frame.size
    omega = np.exp((-2 * np.pi * 1j) / N)
    r = np.arange(N)
    w_matrix = np.vander(omega ** r, increasing=True)
    my_frame = w_matrix @ my_frame

    #frames[7] = np.fft.fft(frames[7])
    #task_3_graf()

def task_3_graf():
    plt.figure(figsize=(8, 5))
    split_array = np.split(my_frame,2)
    time_line = np.arange(np.size(np.real(split_array[0])))
    plt.plot(time_line,np.real(split_array[0]))
    plt.ylabel('Hodnota []')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.gca().set_title('Diskrétna fourierova transformácia (DFT)')
    plt.tight_layout()
    plt.show()

def task_4():
    f, t, sgr = spectrogram(my_frame, )
    sgr_log = 10 * np.log10(sgr + 1e-20)
    plt.figure(figsize=(9, 3))
    plt.pcolormesh(t, f, sgr_log)
    plt.gca().set_xlabel('Čas [s]')
    plt.gca().set_ylabel('Frekvencia [Hz]')
    cbar = plt.colorbar()
    cbar.set_label('Spektrálna hustota výkonu [dB]', rotation=270, labelpad=15)
    plt.tight_layout()
    plt.show()




if __name__ == '__main__':
    load_sound_file()
    task_1()
    task_2()
    task_3()
    task_4()
