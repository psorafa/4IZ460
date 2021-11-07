import matplotlib.pyplot as plt

# nepatří to logicky k modelům, ale nějak jsem si odvykl na moduly v pythonu - pak přesunout

def draw_hist(filename, label, values, categories, xlabel, ylabel):
    font = {
        'size'   : 8
    }
    plt.rc('font', **font)

    plt.bar(categories, values)
    plt.title(label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(filename)

    plt.clf()