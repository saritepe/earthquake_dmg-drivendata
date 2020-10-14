import pandas as pd


def separated_initial_data_load(values_file_path='data/raw/train_values.csv',
                                labels_file_path='data/raw/train_labels.csv', sep=','):
    values = pd.read_csv(values_file_path, sep=sep)
    labels = pd.read_csv(labels_file_path, sep=sep)
    return values.merge(labels)
