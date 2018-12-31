#%%
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

import pathpy as pp

import pandas as pd
import numpy as np
import scipy.sparse as sp

from TradeFlow import TradeFlow
from Algorithms import cosine_similarity



"""
calculate the eigenvector centrality of the weighted differences in reported trade volume 
--> should result in more trusted countries receiving a higher centrality
"""

# def cosine_similarity(X, Y):
#     """
#     calculate the cosine similarity of two vectors X and Y
#     :param X: vector of shape (M, N)
#     :param Y: vector of shape (M, N)
#     :return : cosine similarity of X and Y 
#     """
#     assert X.shape == Y.shape
#     return np.sum(np.dot(X.T, Y)) / (np.linalg.norm(X) * np.linalg.norm(Y))





data = TradeFlow()
data.readType1('data/maize/56.2013 basicVal.csv')
data.removeIncompleteData()
data.calculateNewColumn(cosine_similarity, 'delta')
data.Eigenvalues()
print(data.eigvec[(56, 2013)])

plt.figure()
plt.plot(data.eigvec[(56, 2013)])
plt.savefig("eigenvectors.png")