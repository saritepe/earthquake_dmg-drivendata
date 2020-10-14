from sklearn.model_selection import train_test_split

from src.utils.get_config import get_config
from src.data.categorize_data import get_label_cols


def split_data(df):
    label_col = get_label_cols()
    X = df.drop(label_col, axis=1)
    y = df[label_col]

    random_state = get_config('global_parameters.yaml', 'random_state')
    test_size = get_config('global_parameters.yaml', 'test_size')
    stratify = get_config('global_parameters.yaml', 'stratify')
    if stratify:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state,
                                                            stratify=y)
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test

