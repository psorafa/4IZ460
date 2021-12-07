from matplotlib.pyplot import draw
from fourfold import draw_heatmap
from fourfold import draw_double_fourfold
import os
import numpy as np

class HypothesisWraper:
    
    def __init__(self, question, method, hypothesis) -> None:
        self.q = question
        self.method = method
        self.hypothesis = hypothesis
        if(method == "4ft"):
            self.pim = hypothesis["params"]["pim"]
            self.base = hypothesis["params"]["base"]
        if(method == "sd4ft"):
            self.base1 = hypothesis["params"]["base1"]
            self.base2 = hypothesis["params"]["base2"]
            self.pim1 = hypothesis["params"]["pim1"]
            self.pim2 = hypothesis["params"]["pim2"]
            self.deltapim = hypothesis["params"]["deltapim"]
       
        
    def draw_fourfold(self, filename_prepend = None) -> None:
        ant = self.hypothesis["cedents"]["ante"]
        suc = self.hypothesis["cedents"]["succ"]
        # aa = self.hypothesis["params"]["aad"]

        filename = (str(filename_prepend) if filename_prepend != None else "") + "_" + suc + ".png"
        current_dir = os.path.dirname(__file__)
        values = []
        if(self.method == "4ft"):
            values = np.array(self.hypothesis["params"]["fourfold"]).reshape(2,2)
        if(self.method == "sd4ft"):
            values1 = np.array(self.hypothesis["params"]["fourfold1"]).reshape(2,2)
            values2 = np.array(self.hypothesis["params"]["fourfold2"]).reshape(2,2)
            values = np.hstack((values1,values2))  # zajisti rozlozeni ktere chceme
            draw_double_fourfold(os.path.join(current_dir, self.q, "double_fourfolds", filename),
            ant + "-> " + suc, 
            np.array(self.hypothesis["params"]["fourfold1"]),
            np.array(self.hypothesis["params"]["fourfold2"]))


        # draw_fourfold(
        draw_heatmap(
            os.path.join(current_dir, self.q, "fourfolds", filename),
            ant + "-> " + suc,
            values
        )

# Vybere pravidla s nejlepší důveryhodností a vykreslí jejich čtyřpolni tabulky
def draw_fourfolds_best_confidence(hypothesis, num_hypo):

    best_pim = sorted(hypothesis, key = lambda x: x.pim, reverse=True)
    num_list_hit_0 = 0
    num_list_hit_1 = 0

    for i in range(0, len(best_pim)):
        h = best_pim[i]
        if h.hypothesis["cedents"]["succ"] == "hit(0 )":
            # print(best_pim[i].hypothesis)

            h.draw_fourfold("pim_" + format(h.pim, '.3f') + "_hit_0_")

            num_list_hit_0 = num_list_hit_0 + 1
        
            if num_list_hit_0 > num_hypo:
                break

    for i in range(0, len(best_pim)):
        h = best_pim[i]
        if h.hypothesis["cedents"]["succ"] == "hit(1 )":

            h.draw_fourfold("pim_" + format(h.pim, '.3f')  + "_hit_1_")

            num_list_hit_1 = num_list_hit_1 + 1
        
            if num_list_hit_1 > num_hypo:
                break

# Vybere pravidla s největší podporou a vykreslí jejich čtyřpolní tabulky
def draw_fourfolds_best_base(hypothesis, num_hypo):
    num_list = 0

    best_base = sorted(hypothesis, key = lambda x: x.base, reverse=True)

    for i in range(0, len(best_base)):
        h = best_base[i]
        if h.hypothesis["cedents"]["succ"] == "hit(1 )":
            # print(best_base[i].hypothesis)

            h.draw_fourfold("base_" + str(h.base) + "_")

            num_list = num_list + 1

            if num_list > num_hypo:
                break

# Vybere pravidla s nejlepší důveryhodností a vykreslí jejich čtyřpolni tabulky
def draw_double_fourfolds_greatest_deltapim(hypothesis, num_hypo):

    best_pim = sorted(hypothesis, key = lambda x: x.deltapim, reverse=True)
    num_list = 0

    for i in range(0, len(best_pim)):
        h = best_pim[i]
        if h.hypothesis["cedents"]["succ"] == "hit(0 )":
            # print(best_pim[i].hypothesis)

            h.draw_fourfold("pim_" + format(h.deltapim, '.3f') + "_hit_0_")

            num_list = num_list + 1
        
            if num_list > num_hypo:
                break

    for i in range(0, len(best_pim)):
        h = best_pim[i]
        if h.hypothesis["cedents"]["succ"] == "hit(1 )":
            h.draw_fourfold("pim_" + format(h.deltapim, '.3f')  + "_hit_1_")

            num_list = num_list + 1
        
            if num_list > num_hypo:
                break