import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_ecg_data(x_data=None, y_data=None, title="ECG", ticks=30):
    __plot_instance(len(y_data), ticks)

    if x_data is None:
        plt.plot(y_data)
    else:
        plt.plot(x_data, y_data)

    plt.suptitle(title)
    plt.show()

def __plot_instance(data_readings, nr_of_ticks):
    tick_labels = [tick_label for tick_label in range(nr_of_ticks+1)]
    ticks = [tick * (data_readings // nr_of_ticks) for tick in range(nr_of_ticks+1)]

    plt.subplot(frame_on=False, xticks=ticks, xticklabels=tick_labels)
    
    if nr_of_ticks == 30:
        left, right, bottom, top = (0.04, 0.98, 0.42, 0.46)
    
    plt.subplots_adjust(left=left, right=right, bottom=bottom, top=top, wspace=1., hspace=1.)
    plt.axis([0, data_readings, -1000, 1000])