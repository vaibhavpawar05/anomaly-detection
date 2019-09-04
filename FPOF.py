# FPOF - Frequent Pattern Outlier Detection without Exhaustive Mining

import numpy as np
import pandas as pd
import pathlib
from joblib import Parallel, delayed

from sklearn.metrics import auc, roc_auc_score

base_dir = pathlib.Path('/Users/vaibhav/MiscProjects/anomaly-detection')

# laod data

df = pd.read_csv(base_dir/'datasets/agaricus-lepiota.data', header=None)

# convert all into int encoding
# create mapping, dict of dicts

mapping = {}
nval = 0
for col in list(df.columns):
    mapping[col] = {}
    col_unique_vals = np.unique(df[col])
    for val in col_unique_vals:
        mapping[col][val] = nval
        nval += 1
        
df2 = df.copy()
for col in list(df.columns):
    col_mapping = mapping[col]
    df2[col] = df2[col].apply(lambda x: col_mapping[x])
        
x = df2[list(range(1, df2.shape[1]))].values
        
nrec = x.shape[0]
        
# create list of sets from rows of x
rows = [set(x[i, :]) for i in range(0, nrec)]

# calcuate the distances - intersection based

dists = np.zeros((nrec, ))
for i in range(0, nrec):
    for j in range(i+1, nrec):
        dist = 2**(len(rows[i].intersection(rows[j])))
        dists[i] += dist
        dists[j] += dist
             
dists += 2**(x.shape[1])
max_dist = np.max(dists)
dists /= max_dist
        
print('auc', roc_auc_score(y_true=df2[0], y_score=-dists))

# distance calculation can be done using scipy hamming

from scipy.spatial.distance import pdist, squareform

hdists = pdist(x, metric='hamming')

dist_idx = 0
dists2 = np.zeros((nrec, ))
for i in range(0, nrec):
    for j in range(i+1, nrec):
        dist = 2**(x.shape[1] * (1 - hdists[dist_idx]))
        dists2[i] += dist
        dists2[j] += dist
        dist_idx += 1
        
dists2 += 2**(x.shape[1])
max_dist2 = np.max(dists2)
dists2 /= max_dist2
