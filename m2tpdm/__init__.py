# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:38:48 2022

@author: a694772
"""
__author__ = 'Antoine Guillaume antoine.guillaume45@gmail.com'
__version__ = "0.1.0"

from .student_method import my_shapelet
from .benchmark import run_benchmark_protocol, run_test_protocol

__all__ = ['utils','my_shapelet','run_benchmark_protocol','run_test_protocol']