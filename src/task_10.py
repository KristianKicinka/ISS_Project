import soundfile


def task_10(data, sample_frequency):

    print(f'\nData check')
    print(f'Max of data : {max(data)}')
    print(f'Min of data : {min(data)}')

    soundfile.write('../audio/clean_bandstop.wav', data, sample_frequency)
    print('\nProcess done')


