from src.utils.get_config import get_config


def get_cat_cols():
    return get_config('data_categorization.yaml', 'cat_cols')


def get_drop_cols():
    return get_config('data_categorization.yaml', 'drop_cols')


def get_label_cols():
    return get_config('data_categorization.yaml', 'label_cols')
