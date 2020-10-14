from src.data.categorize_data import get_cat_cols
from src.data.categorize_data import get_drop_cols
from src.data.load_data import separated_initial_data_load
from src.utils.get_config import get_config


print(get_cat_cols())
print(get_drop_cols())

train_values_path = get_config('file_paths.yaml', 'train_values')
train_labels_path = get_config('file_paths.yaml', 'train_labels')
print(separated_initial_data_load(train_labels_path, train_labels_path))
