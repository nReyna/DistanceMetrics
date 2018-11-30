# Last modified by N. Reyna
# 11:55 AM 11/25/2018

import numpy as np
from scipy.spatial import distance

# -----------------------------------------------------------------------------

class dist_metrics():

    def __init__(self): #******************************************************
        self.d={'sqr_res_avg':  self.d0,
                'euclidean':    self.d1,
                'cosine':       self.d2,
                'minkowski:p1': self.d3,
                'minkowski:p3': self.d4,
                'correlation':  self.d5,
                'jaccard':      self.d6,
                'hamming':      self.d7,
                'chebyshev':    self.d8,
                'canberra':     self.d9,
                'braycurtis':   self.d10,
                'mahalanobis':  self.d11,
                'sokalsneath':  self.d12,
                'minkowski:p5': self.d13 }


    def test(self): #**********************************************************
        
        # euclidean: sqrt(3), 0, sqrt(5) 
        x = np.array([[0,0,0], [1,1,1], [1,2,3]])
        y = np.array([[1,1,1]])

        print(x, y)

        i = 0
        for k, f in self.d.items():
            i += 1
            print(i, k, '\n', f(x, y))


    # METRICS
    # -------------------------------------------------------------------------

    def d0(self, x, y):
        res = np.mean((x-y)**2, axis=1)
        return res


    def d1(self, x, y):
        res = distance.cdist(x, y, 'euclidean')
        return res

    def d2(self, x, y):
        res = distance.cdist(x, y, 'cosine')
        return res

    def d3(self, x, y):
        res = distance.cdist(x, y, 'minkowski', p=1)
        return res

    def d4(self, x, y):
        res = distance.cdist(x, y, 'minkowski', p=3)
        return res

    def d5(self, x, y):
        res = distance.cdist(x, y, 'correlation')
        return res

    def d6(self, x, y):
        res = distance.cdist(x, y, 'jaccard')
        return res

    def d7(self, x, y):
        res = distance.cdist(x, y, 'hamming')
        return res

    def d8(self, x, y):
        res = distance.cdist(x, y, 'chebyshev')
        return res

    def d9(self, x, y):
        res = distance.cdist(x, y, 'canberra')
        return res

    def d10(self, x, y):
        res = distance.cdist(x, y, 'braycurtis')
        return res

    def d11(self, x, y):
        res = distance.cdist(x, y, 'mahalanobis', VI=4)
        return res

    def d12(self, x, y):
        res = distance.cdist(x, y, 'sokalsneath')
        return res

    def d13(self, x, y):
        res = distance.cdist(x, y, 'minkowski', p=5)
        return res


############### END ############### END ############### END ############### END


if __name__ == "__main__": # ======================= MAIN =====================

    p = dist_metrics().test()
    

# *****************************************************************************
