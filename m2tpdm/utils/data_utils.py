# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:00:59 2022

@author: a694772
"""

import numpy as np
from sktime.datasets._data_io import load_UCR_UEA_dataset
from sklearn.preprocessing import LabelEncoder
from sktime.datatypes._panel._convert import from_nested_to_3d_numpy
from numpy.lib.stride_tricks import as_strided


def generate_subsequences_2D(X, window_size, dilation):
    """
    Generate subsequences from an ensemble of univariate time series with specified 
    length and dilation parameters.

    Parameters
    ----------
    X : array, shape = (n_samples, n_timestamps)
        An ensemble of univariate time series, in a 2 dimensional view.
    window_size : int
        Length of the subsequences to generate.
    dilation : int
        Dilation parameter to apply when generating the subsequences.

    Returns
    -------
    array, shape = (n_samples, n_subsequences, stride_len)
        All possible subsequences of length stride_len for each time series.
    """
    n_samples, n_timestamps = X.shape

    shape_new = (n_samples,
                 n_timestamps - (window_size-1)*dilation,
                 window_size)
    s0, s1 = X.strides
    strides_new = (s0, s1, dilation * s1)
    return as_strided(X, shape=shape_new, strides=strides_new)

def generate_subsequences_1D(X, window_size, dilation):
    """
    Generate subsequences from the input univariate time series with specified 
    length and dilation parameters.

    Parameters
    ----------
    X : array, shape = (n_timestamps)
        An univariate time series, in a 1 dimensional view.
    window_size : int
        Length of the subsequences to generate.
    dilation : int
        Dilation parameter to apply when generating the subsequences.

    Returns
    -------
    array, shape = (n_samples, n_subsequences, stride_len)
        All possible subsequences of length stride_len for each time series.
    """
    n_timestamps = X.shape[0]
    shape_new = (n_timestamps - (window_size-1)*dilation,
                 window_size)

    s0 = X.strides[0]
    strides_new = (s0, dilation * s0)
    return as_strided(X, shape=shape_new, strides=strides_new)

def load_sktime_dataset_split(name, normalize=True):
    """
    Load the original train and test splits of a dataset 
    from the UCR/UEA archive by name using sktime API.
    
    Parameters
    ----------
    name : string
        Name of the dataset to download.
    normalize : boolean, optional
        If True, time series will be z-normalized. The default is True.
        
    Returns
    -------
    X_train : array, shape=(n_samples_train, n_timestamps)
        Training data from the dataset specified by path.
    X_test : array, shape=(n_samples_test, n_timestamps)
        Testing data from the dataset specified by path.
    y_train : array, shape=(n_samples_train)
        Class of the training data.
    y_test : array, shape=(n_samples_test)
        Class of the testing data.
    le : LabelEncoder
        LabelEncoder object used to uniformize the class labels
    """
    #Load datasets
    X_train, y_train = load_UCR_UEA_dataset(
        name, return_X_y=True, split='train')
    X_test, y_test = load_UCR_UEA_dataset(name, return_X_y=True, split='test')

    #Convert pandas DataFrames to numpy arrays
    X_train = from_nested_to_3d_numpy(X_train)
    X_test = from_nested_to_3d_numpy(X_test)

    #Convert class labels to make sure they are between 0,n_classes
    le = LabelEncoder().fit(y_train)
    y_train = le.transform(y_train)
    y_test = le.transform(y_test)

    #Z-Normalize the data
    if normalize:
        X_train = (X_train - X_train.mean(axis=-1, keepdims=True)) / (
            X_train.std(axis=-1, keepdims=True) + 1e-8)
        X_test = (X_test - X_test.mean(axis=-1, keepdims=True)) / (
            X_test.std(axis=-1, keepdims=True) + 1e-8)

    return X_train[:,0,:], X_test[:,0,:], y_train, y_test, le
