import matplotlib as mpl
import matplotlib.pyplot as plt
import supporters.Generators as generator

def plot_ecg(data, title = "ECG"):
    ticks = []
    tick_labels = [n for n in range(31)]

    for ele in generator.gen_ticks(15000, 500):
        ticks.append(ele)

    plt.subplot(frame_on=False, xlabel="Sekunder", xticks=ticks, xticklabels=tick_labels, title=title)

    plt.plot(data)
    plt.axis([0, 15000, -1000, 1000])

    plt.show()