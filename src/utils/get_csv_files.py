import pandas as pd


def get_csv_files(path, name_list):
    files = []
    for name in name_list:
        file_path = path + name + '.csv'
        files.append(pd.read_csv(file_path, sep=';'))
    files_dictionary = dict(zip(name_list, files))
    return files_dictionary
