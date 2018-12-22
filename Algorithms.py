import numpy as np
import pandas as pd

from TradeFlow import TradeFlow

def cosine_similarity(X, Y):
    """
    calculate the cosine similarity of two vectors X and Y
    :param X: vector of shape (M, N)
    :param Y: vector of shape (M, N)
    :return : cosine similarity of X and Y 
    """
    assert X.shape == Y.shape
    return np.sum(np.dot(X.T, Y)) / (np.linalg.norm(X) * np.linalg.norm(Y))