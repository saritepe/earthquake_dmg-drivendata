from sklearn import model_selection


def select_cv(cv_name, n_splits=5, n_repeats=3, random_state=42):
    return getattr(model_selection, cv_name)(n_splits=n_splits, n_repeats=n_repeats, random_state=random_state)
    # TODO select_cv func should be redesigned with other cv options
