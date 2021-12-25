
import numpy as np
import soundfile
from matplotlib import pyplot as plt
from scipy.signal import spectrogram


def task_6(frequencies, sample_frequency, signal):
    norm_frequency = np.size(signal) / sample_frequency
    step = 1/sample_frequency
    cos_signal = np.empty(np.size(signal))*0.0
    for frequency in frequencies:
        cos_signal = cos_signal + np.cos(np.arange(0, norm_frequency, step)*(2*np.pi*frequency))

    print(f'cos : {cos_signal}')
    task_6_spectogram(cos_signal, sample_frequency)
    soundfile.write('audio/4cos.wav', cos_signal, sample_frequency)


def task_6_spectogram(signal, sample_frequency):
    f, t, sgr = spectrogram(signal, sample_frequency, nperseg=1024, noverlap=512)
    sgr_log = 10 * np.log10(pow(np.abs(sgr), 2))
    plt.figure(figsize=(9, 3))
    plt.pcolormesh(t, f, sgr_log)
    plt.gca().set_xlabel('Čas [s]')
    plt.gca().set_ylabel('Frekvencia [Hz]')
    cbar = plt.colorbar()
    cbar.set_label('Spektrálna hustota výkonu [dB]', rotation=270, labelpad=15)
    plt.tight_layout()
    plt.show()