import soundfile


def task_10(data, sample_frequency):
    soundfile.write('audio/clean_bandstop.wav', data, sample_frequency)
    print('Process done')


