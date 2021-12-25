
import matplotlib.pyplot as plt
import numpy as np


def task_1(time_line, signal):
    # print max and min values
    max_val = np.max(signal)
    min_val = np.min(signal)
    print(f'Max value is : {max_val}')
    print(f'Min value is : {min_val}')
    show_task_1_graph(time_line, signal)


def show_task_1_graph(time_line, signal):
    plt.figure(figsize=(8, 5))
    plt.plot(time_line, signal)
    plt.ylabel('Hodnota []')
    plt.gca().set_xlabel('čas [s]')
    plt.gca().set_title('Vstupný zvukový signál')
    plt.tight_layout()
    plt.show()
