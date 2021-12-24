import numpy as np
import scipy.signal
import soundfile
from matplotlib import pyplot as plt
from scipy.signal import spectrogram


def filter(frekvency,sample_frekvency,data):
    pass_correction = 15
    stop_correction = 50
    g_pass = 3
    g_stop = 40
    nyquest_frekv = sample_frekvency/2

    pass_start = (frekvency-pass_correction)
    pass_end = (frekvency+pass_correction)
    stop_start = (pass_start-stop_correction)
    stop_end = (pass_end+stop_correction)

    pass_start = pass_start/nyquest_frekv
    pass_end = pass_end/nyquest_frekv
    stop_start = stop_start/nyquest_frekv
    stop_end = stop_end/nyquest_frekv

    N,Wn = scipy.signal.buttord([stop_start,stop_end], [pass_start,pass_end], g_pass, g_stop, False)

    b, a = scipy.signal.butter(N,Wn,'bandstop',analog=False)

    filtered_signal = scipy.signal.filtfilt(b,a,data)
    return filtered_signal


def task_7_spectogram(signal,sample_frekvency):
    f, t, sgr = spectrogram(signal, sample_frekvency, nperseg=1024, noverlap=512)
    sgr_log = 10 * np.log10(pow(np.abs(sgr), 2))
    plt.figure(figsize=(9, 3))
    plt.pcolormesh(t, f, sgr_log)
    plt.gca().set_xlabel('Čas [s]')
    plt.gca().set_ylabel('Frekvencia [Hz]')
    cbar = plt.colorbar()
    cbar.set_label('Spektrálna hustota výkonu [dB]', rotation=270, labelpad=15)
    plt.tight_layout()
    plt.show()


def task_7(found_frekvencies, sample_frekvency, signal):
    data = signal
    for frequency in found_frekvencies:
        data = filter(frequency,sample_frekvency,data)
    print(f'{data}')
    print(f'data done')
    task_7_spectogram(data,sample_frekvency)
    return data


