from sklearn import preprocessing


def select_scaler(scaler_name="StandardScaler"):
    return getattr(preprocessing, scaler_name)()
