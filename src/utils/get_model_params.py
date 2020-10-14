import numpy as np


param_criterion = ['gini', 'entropy']
param_splitter = ['best', 'random']
param_max_depth = [int(x) for x in np.linspace(10, 200, num=40)]
param_min_samples_split = [int(x) for x in np.linspace(2, 30, num=10)]
param_min_samples_leaf = [int(x) for x in np.linspace(1, 30, num=10)]
param_max_features = ['auto', 'sqrt', 'log2']
param_bootstrap = [True, False]

rfc_param_grid = dict()
rfc_param_grid['criterion'] = param_criterion
rfc_param_grid['max_depth'] = param_max_depth
rfc_param_grid['min_samples_split'] = param_min_samples_split
rfc_param_grid['min_samples_leaf'] = param_min_samples_leaf
rfc_param_grid['max_features'] = param_max_features
rfc_param_grid['bootstrap'] = param_bootstrap


dtc_param_grid = dict()

dtc_param_grid['criterion'] = param_criterion
dtc_param_grid['splitter'] = param_splitter
dtc_param_grid['max_depth'] = param_max_depth
dtc_param_grid['min_samples_leaf'] = param_min_samples_leaf
dtc_param_grid['min_samples_split'] = param_min_samples_split
dtc_param_grid['max_features'] = param_max_features


def model_param_selector(model_name):
    # TODO Other then rfc and dtc should be added
    if model_name == 'dtc':
        return dtc_param_grid
    elif model_name == 'rfc':
        # TODO global değişkenler içeri alınabilir ya da bir başka python dosyası ile üretilip buraya getirilebilir
        return rfc_param_grid
    else:
        print("Model couldn't find.")
