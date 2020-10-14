from sklearn import feature_selection


def feature_selector(feature_selector_name, model):
    # TODO design feature_selector parameters
    return getattr(feature_selection, feature_selector_name)(model)
