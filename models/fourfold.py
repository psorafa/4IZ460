import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.table import Table
from matplotlib.font_manager import FontProperties
import seaborn as sns
import pandas as pd
import re

# vykreslí čtyřpolní tabulku jako heatmapu - hezčí grafika než s matplotlib.table, ale asi trochu větší knihovna
def draw_heatmap(filename, label, values):
    xticklabels=['S', '~S']
    mpl.rcParams['figure.figsize']=(5,5)

    if (values.shape == (2,4)):
        xticklabels=['S', '~S', 'S', '~S']
        mpl.rcParams['figure.figsize']=(10,5)

    
    fig, ax = plt.subplots()

    sns.heatmap(pd.DataFrame(values), 
        annot=True, cmap="Greens" ,fmt='g', 
        xticklabels=xticklabels, yticklabels=['A', '~A'])
    plt.tight_layout()
    plt.title(re.sub("&","&\n", label))
    plt.ylabel('Antecedent')
    plt.xlabel('Succedent', labelpad=15)
    # plt.show()
    plt.savefig(filename, bbox_inches = 'tight')
    plt.close(fig)
    plt.clf()
    
# vykreslí čtyřpolní tabulku
def draw_fourfold(filename, label, values) :
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

# vykreslí dvojtou čtyřpolní tabulku
def draw_double_fourfold(filename, label, fourfold1, fourfold2) :
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
    tb.add_cell(0, 3, width=width, height=height, text="S", loc='center', facecolor="#1DB954", fontproperties=font)
    tb.add_cell(0, 4, width=width, height=height, text="-S", loc='center', facecolor="#39a05d", fontproperties=font)

    tb.add_cell(1, 0, width=width, height=height, text="A", loc='center')
    tb.add_cell(1, 1, width=width, height=height, text=fourfold1[0], loc='center', facecolor="#1DB954", fontproperties=font)
    tb.add_cell(1, 2, width=width, height=height, text=fourfold1[1], loc='center', facecolor="#39a05d", fontproperties=font)
    tb.add_cell(1, 3, width=width, height=height, text=fourfold2[0], loc='center', facecolor="#1DB954", fontproperties=font)
    tb.add_cell(1, 4, width=width, height=height, text=fourfold2[1], loc='center', facecolor="#39a05d", fontproperties=font)

    tb.add_cell(2, 0, width=width, height=height, text="-A", loc='center')
    tb.add_cell(2, 1, width=width, height=height, text=fourfold1[2], loc='center', facecolor="#1DB954", fontproperties=font)
    tb.add_cell(2, 2, width=width, height=height, text=fourfold1[3], loc='center', facecolor="#39a05d", fontproperties=font)
    tb.add_cell(2, 3, width=width, height=height, text=fourfold2[2], loc='center', facecolor="#1DB954", fontproperties=font)
    tb.add_cell(2, 4, width=width, height=height, text=fourfold2[3], loc='center', facecolor="#39a05d", fontproperties=font)

    ax.add_table(tb)

    plt.savefig(filename)
    plt.close(fig)
    plt.clf()