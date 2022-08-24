# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:59:30 2022

@author: a694772
"""

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from m2tpdm.utils import generate_subsequences_2D, generate_subsequences_1D

class my_shapelet(BaseEstimator, TransformerMixin):
    
    # The default parameter will be used by default in the benchmark script !
    def __init__(self, n_shapelets=100, shapelet_length=9):
        """
        Initalize the object parameters

        Parameters
        ----------
        n_shapelets : int, optional
            The number of shapelet to generate. The default is 100
        shapelet_length : int, optional
            The length of the shapelets. The default is 9.
            !!! You can modify this parameter to be an array of possible
            lengths to increase the diversity of your shapelet set, but you
            will have to modify some code below !!! 

        Returns
        -------
        None.

        """
        self.n_shapelets = n_shapelets
        self.shapelet_length = shapelet_length
    
    def __repr__(self):
        """
        Override base presentation method to ensure that the value of default 
        parameter are displayed.

        Returns
        -------
        str
            String description of the object

        """
        return "my_shapelet(n_shapelets={}, shapelet_length={})".format(self.n_shapelets, self.shapelet_length)
    
    def generate_shapelets(self, X, y):
        """
        This function should be used to generate the shapelet values from the input data
        Multiple way to approach this process have been described in the course.
        
        Parameters
        ----------
        X : array, shape=(n_samples, n_timestamps)
            A set of time series.
        y : array, shape=(n_samples)
            Class of each time series
            
        Returns
        -------
        values : array, shape=(n_shapelets, shapelet_length)
            The values of each shapelet

        """
        ###############################
        #                             #
        #         TO COMPLETE         #
        #                             #
        ###############################
        
        
        values = np.zeros((self.n_shapelets, self.shapelet_length))
        
        return values
    
    # You could also add a function that approximate all input time series to 
    # remove noise and reduce the search space ...
    
    def fit(self, X, y):
        """
        Fit method. It will call the generate_shapelets method to create the 
        shapelets

        Parameters
        ----------
        X : array, shape=(n_samples, n_timestamps)
            A set of time series.
        y : array, shape=(n_samples)
            Class of each time series

        Returns
        -------
        self

        """
        values = self.generate_shapelets(X, y)
        self.values_ = values
        return self
    
    def transform(self, X):
        """
        In this function, you should compute the distance vectors between your
        shapelets and the times series in X. Then, you will extract features
        from each distance vector to create the features that will be used as
        input of a classifier.

        Parameters
        ----------
        X : array, shape=(n_samples, n_timestamps)
            A set of time series to transform.

        Returns
        -------
        X_new : array, shape=(n_samples, n_shapelets*n_features)
            The features extracted from the distance vector between each shapelet
            and each time series.

        """
        
        n_features = 1 #The minimal number of features (i.e the minimum value of d(S,X))
        X_new = np.zeros((X.shape[0], self.n_shapelets*n_features))
    
        """
        I give you a first basic and slow but working implementation. If you 
        have time, once you are confident with your shapelet generate scheme
        you can modify this part to try to use normalized distance
        or gain time performance.
        """
        
        for i in range(X.shape[0]):
            for j in range(self.values_.shape[0]):
                dist = self._shapelet_distance_to_serie(
                    X[i], self.values_[j]
                )
                X_new[i,j] = dist.min()

        return X_new
    
    
    #############################################################################
    #                                                                           #
    #   Those are just helper functions, you could optimize them, notably to    #
    #   avoid recomputing the normalization multiple times or group operations  #
    #                                                                           #
    #############################################################################
    
    def _shapelet_distance_to_serie(self, X, S, normalize=False):
        """
        Compute the distance vector between a time series and a shapelet
        
        Parameters
        ----------
        X : array, shape=(n_timestamps)
            A time serie
            
        S : array, shape=(shapelet_length)
            A shapelet
            
        normalize : bool, optional
            Wether or not to use a z-normalized distance. The default is False.

        Returns
        -------
        array, shape=(n_timestamps - (shapelet_length-1))
            The distance vector between X and S (ie. d(S,X))
        """
        
        #This gives array, shape(n_timestamps - (shapelet_length-1), shapelet_length)
        subsequences = generate_subsequences_1D(X, self.shapelet_length, 1)
        if normalize:
            # we add 1e-8 to avoid division per 0 error and having to check for it
            subsequences = (subsequences - subsequences.mean(axis=1, keepdims=True))/(subsequences.std(axis=1, keepdims=True) + 1e-8)
            S = (S - S.mean()) / (S.std() + 1e-8)
        return np.abs(subsequences - S).sum(axis=1)

    
    def _shapelet_distance_to_dataset(self, X, S, normalize=False):
        """
        Compute the shapelet distance between a set of time series         
        
        Parameters
        ----------
        X : array, shape=(n_samples, n_timestamps)
            A time serie
            
        S : array, shape=(shapelet_length)
            A shapelet
    
        normalize : bool, optional
            Wether or not to use a z-normalized distance. The default is False.

        Returns
        -------
        array, shape=(n_samples, n_timestamps - (shapelet_length-1))
            The distance vector between each time series and S
        """

        #This gives array, shape(n_samples, n_timestamps - (shapelet_length-1), shapelet_length)
        subsequences = generate_subsequences_2D(X, self.shapelet_length, 1)
        if normalize:
            # we add 1e-8 to avoid division per 0 error and having to check for it
            subsequences = (subsequences - subsequences.mean(axis=2, keepdims=True))/(subsequences.std(axis=2,, keepdims=True) + 1e-8)
            S = (S - S.mean()) / (S.std() + 1e-8)
        
        return subsequences - S
