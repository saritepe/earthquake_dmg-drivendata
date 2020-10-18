from src.utils.get_config import get_config


def sampling(df):
    random_state = get_config('global_parameters.yaml', 'random_state')
    sample_data_size = get_config('global_parameters.yaml', 'sample_data_size')
    return df.sample(n=sample_data_size, random_state=random_state)
