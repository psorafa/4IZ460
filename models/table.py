import matplotlib.pyplot as plt
from matplotlib.table import Table
from matplotlib.font_manager import FontProperties

# vykreslí čtyřpolní tabulku
def draw_table(filename, label, ant, succ, values) :
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')

    ax.set_aspect('equal')

    tb = Table(ax, bbox=[0,0,1,1])

    ax.set_title(label, fontsize = 8)

    #ax.text(-0.1, -0.1, label, transform=ax.transAxes, fontsize=10, verticalalignment='top')

    font = FontProperties(
        weight="bold",
        size="large"
    )

    width = 0.2
    height = 0.2

    tb.add_cell(0, 0, width=width, height=height, text="", loc='center')
    tb.add_cell(0, 1, width=width, height=height, text="S", loc='center', facecolor="#1DB954", fontproperties=font)
    tb.add_cell(0, 2, width=width, height=height, text="-S", loc='center', facecolor="#39a05d", fontproperties=font)

    tb.add_cell(1, 0, width=width, height=height, text="A", loc='center')
    tb.add_cell(1, 1, width=width, height=height, text=values[0], loc='center', facecolor="#1DB954", fontproperties=font)
    tb.add_cell(1, 2, width=width, height=height, text=values[1], loc='center', facecolor="#39a05d", fontproperties=font)

    tb.add_cell(2, 0, width=width, height=height, text="-A", loc='center')
    tb.add_cell(2, 1, width=width, height=height, text=values[2], loc='center', facecolor="#1DB954", fontproperties=font)
    tb.add_cell(2, 2, width=width, height=height, text=values[3], loc='center', facecolor="#39a05d", fontproperties=font)

    ax.add_table(tb)

    plt.savefig(filename)
    plt.close(fig)
    plt.clf()
