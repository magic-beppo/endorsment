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

#%%
def read_normalized_data(filename):
    """
    reads trade data from a normalized csv file
    calculates the difference in reporting for complete sets of data
    --> use cosine similarity 
    returns an a dataframe with calculated similarity
    """
    # read the data in to a dataframe
    df = pd.read_csv(filename)
    # find bad row indices
    df = df.replace(0, np.NaN)
    df = df.dropna(subset=['NW_M', 'NW_X', 'TV_M', 'TV_X', 'UV_M', 'UV_X'])

    country_1 = df[['NW_M', 'TV_M', 'UV_M']]
    country_2 = df[['NW_X', 'TV_X', 'UV_X']]
    
    deltas = np.zeros(country_1.shape[0])
    
    # calculate the cosine similarity of the reported trade values
    for i in range(country_1.shape[0]):
        cos_theta = cosine_similarity(country_1.values[i], country_2.values[i])
        deltas[i] = cos_theta
    df['delta'] = deltas

    return df
#%%
def write_edge_list(df, edge_filename):
    """
    writes a given pandas dataframe and writes the required columns to an csv edgelist
    """
    df.to_csv(edge_filename, index = False, columns = ['rtCode', 'ptCode', 'delta'])
    return df[['rtCode', 'ptCode', 'delta']]




data = TradeFlow()
data.readType1('data/maize/56.2013 basicVal.csv')
data.removeIncompleteData()
data.calculateNewColumn(cosine_similarity, 'delta')

