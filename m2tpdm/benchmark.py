# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:56:10 2022

@author: a694772
"""



import pandas as pd
from m2tpdm.utils import load_sktime_dataset_split
from m2tpdm import my_shapelet
from timeit import default_timer as timer
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def benchmark_pipe(pipeline, X_train, X_test, y_train, y_test):
    """
    A function used to train a pipeline using training data and output accuracy
    on test data. Will aslo record the time taken to run both operation.

    Parameters
    ----------
    pipeline : object
        A scikit-learn pipeline including the student method and a scikit-learn 
        compartible classifier (i.e which have fit and predict methods)
    X_train : array, shape=(n_samples, n_features, n_timestamps)
        Training data
    X_test : array, shape=(n_samples, n_features, n_timestamps)
        Testing data
    y_train : array, shape=(n_samples)
        Classes of training data samples
    y_test : array, shape=(n_samples)
        Classes of testing data samples

    Returns
    -------
    float
        Time spent to fit and predict the pipeline on the input data
    acc_score : float
        Accuracy score on testing data
    """
    t0 = timer()
    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)
    t1 = timer()
    acc_score = accuracy_score(y_test, preds)
    return t1-t0, acc_score


def _run_protocol(dataset_list):
    """
    Run an evaluation protocol using the datasets supplied as parameter

    Parameters
    ----------
    dataset_list : array, shape=(n_datasets)
        A list of dataset name compatible with the sktime API.

    Returns
    -------
    df_results : DataFrame
        A dataframe containing the results of the evaluation for each dataset

    """
    df_results = pd.DataFrame(index=dataset_list, columns=['timing','accuracy','shapelet','classifier'])

    for dataset_name in dataset_list:
        print("Processing dataset {}".format(dataset_name)) 
        
        ##########################################################################################
        #                                                                                        #
        #    If you wish to change the pipeline used after your shapelet model do it here !      #
        #                                                                                        #
        ##########################################################################################
        
        pipeline = make_pipeline(
            my_shapelet(n_shapelets=100, shapelet_length=7),
            RandomForestClassifier(ccp_alpha=0.01)
        )
        
        X_train, X_test, y_train, y_test, _ = load_sktime_dataset_split(dataset_name)
        timing, acc = benchmark_pipe(pipeline, X_train, X_test, y_train, y_test)
        df_results.loc[dataset_name, 'accuracy'] = acc
        df_results.loc[dataset_name, 'timing'] = timing
        df_results.loc[dataset_name, 'shapelet'] = pipeline[0].__repr__()
        df_results.loc[dataset_name, 'classifier'] = pipeline[-1].__repr__()
        
    return df_results

def run_test_protocol():
    dataset_list = ['SmoothSubspace']
    df_results = _run_protocol(dataset_list)
    df_results.to_csv('test_results.csv')

def run_benchmark_protocol():
    dataset_list = ['GunPoint','SmoothSubspace','ArrowHead','UMD','Coffee', 'Beef', 'Lightning7','Lightning2', 'Car']
    df_results = _run_protocol(dataset_list)
    df_results.to_csv('benchmark_results.csv')