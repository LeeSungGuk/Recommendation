# -*- coding: utf-8 -*-
import numpy as np

class similarity_function(object) :

    def __init__(self):
        pass

    #Consie Similarity
    def consie(self, x, y):
        ndx = np.array(x.values())
        ndy = np.array(y.values())

        norm_product = float(np.sqrt(np.sum(ndx ** 2)) * np.sqrt(np.sum(ndy ** 2)))
        dot_product = float(np.sum([ x[movie_id] * y[movie_id] for movie_id in
                                                            x.keys() if movie_id in y.keys()]))

        return  dot_product / norm_product

