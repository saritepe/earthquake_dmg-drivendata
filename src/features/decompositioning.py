from sklearn import decomposition


def decompositioning(n_components, decomposition_name='PCA'):
    return getattr(decomposition, decomposition_name)(n_components=n_components)
