import soundfile

def task_10(data,sample_frekvency):
    soundfile.write('audio/clean_bandstop.wav', data, sample_frekvency)
    print('Process done')


