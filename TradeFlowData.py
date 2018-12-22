import pandas as pd
import numpy as np
class TradeFlowData(object):
    """
    Class which stores tradeflow data and allow manipulation on that data
    """

    """
    TODO:
        -- read from two types of input files
        -- read attributes (possibly write a config file)
        -- write to hdf5 for longterm storage and usage ??
        -- accessabilty
    """

    def __init__(self):
        self.data = {} # safe data in a dictionary with a tuple as keys: key: (product, year)

    def readType1(self, filepath):
        """
        reads data from one file in a normalized table for a single year
        """
        _data = pd.read_csv(filepath)
        _key = filepath[:-4].split('/')[-1].split('.')
        product, year = int(_key[0]), int(_key[1].split(' ')[0])
        self.data[(product, year)] = _data
        
    
    @staticmethod
    def read_normalized_data(filename):
        country_1 = df[['NW_M', 'TV_M', 'UV_M']]
        country_2 = df[['NW_X', 'TV_X', 'UV_X']]
        
        deltas = np.zeros(country_1.shape[0])
        
        # calculate the cosine similarity of the reported trade values
        for i in range(country_1.shape[0]):
            # cos_theta = cosine_similarity(country_1.values[i], country_2.values[i])
            # deltas[i] = cos_theta
            pass
        df['delta'] = deltas

        return df
    
    def readType2(self, filepath):
        """
        reads data from a file (csv) for multiple years
        """
        pass

    def removeIncompleteData(self):
        """
        deletes rows with missing data
        """

        for _key in self.data.keys():
            self.data[_key] = self.data[_key].replace(0, np.NaN)
            self.data[_key] = self.data[_key].dropna(subset=['NW_M', 'NW_X', 'TV_M', 'TV_X', 'UV_M', 'UV_X'])


    def removeRowsByKey(self, key):
        """
        removes rows given a key string. Can be used to remove summarizing data such as "World" or "EU"
        """
        for _key in self.data.keys():
            self.data[_key] = self.data[_key].replace(key, np.NaN)
            self.data[_key] = self.data[_key].dropna()
