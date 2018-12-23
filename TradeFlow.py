import pandas as pd
import numpy as np


class TradeFlow(object):
    """
    Class which stores tradeflow data and allow manipulation on that data
    """

    """
    TODO:
        -- read from two types of input files
        -- read attributes (possibly write a config file)
        -- write to hdf5 for longterm storage and usage ??
        -- accessabilty
        -- export to edgelist
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
        :param key: key to identify row which are to be deleted
        :type key: str

        """
        for _key in self.data.keys():
            self.data[_key] = self.data[_key].replace(key, np.NaN)
            self.data[_key] = self.data[_key].dropna()


    def calculateNewColumn(self, func, newColumnName):
        """
        wrapper to write a new column from data
        :param func: function to be applied to the data
        :param newColumnName: name of the added Column
        :type newColumnName: str
        """
        for _key in self.data.keys():
            country_1 = self.data[_key][['NW_M', 'TV_M', 'UV_M']].values
            country_2 = self.data[_key][['NW_X', 'TV_X', 'UV_X']].values
        
            new_column = np.zeros(country_1.shape[0])
        
            # calculate the cosine similarity of the reported trade values
            for i in range(country_1.shape[0]):
                new_column[i] = func(country_1[i], country_2[i])
            self.data[_key][newColumnName] = new_column

    def asEdgeList(self, headers):
        pass