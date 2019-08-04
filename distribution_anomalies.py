#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:46:36 2019

@author: vaibhav
"""

from scipy.stats import wasserstein_distance
import numpy as np
from scipy.spatial import distance
import timeit

a1 = np.zeros((24,))

txn = 1000*np.random.uniform(size=(8,))

a1[9:17] = txn

a2 = np.zeros((24,))

a2[10:18] = txn
  
# input ndays*24 matrix

x = 1000*np.random.uniform(size=(260,24))
k = 5

d1 = distance.pdist(x, metric='jensenshannon')
d2 = distance.squareform(d1)

n = d2.shape[0]

avg_dist = np.zeros((n,))

for i in range(0, n):
    # for each record find top k distances
    # find average
    dist_i = d2[i, :]
    sort_idx = np.argsort(dist_i)
    avg_dist[i] = np.sum(dist_i[sort_idx[1:k+1]])/k
            
            
def anom_score(x, k):
    
    dist = distance.squareform(distance.pdist(x, metric='jensenshannon'))
    n = x.shape[0]
    avg_dist = np.zeros((n,))

    for i in range(0, n):
        # for each record find top k distances
        # find average
        dist_i = dist[i, :]
        sort_idx = np.argsort(dist_i)
        avg_dist[i] = np.sum(dist_i[sort_idx[1:k+1]])/k
           
    return avg_dist

st = timeit.default_timer()
ad = anom_score(x, k=5)
print('time taken', timeit.default_timer() - st)
                
    