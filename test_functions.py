import datetime

from src.utils.get_config import get_config
from src.utils.get_model import get_model
from src.data.load_data import separated_initial_data_load
from src.data.categorize_data import get_cat_cols
from src.features.drop_cols import drop_cols
from src.features.split_data import split_data
from src.features.encoding import select_encoder
from src.features.scaling import select_scaler
from src.features.feature_selector import feature_selector
from src.features.fitting import fitting
from src.features.transforming import transforming
from src.models.train_model import model_param_search
from src.utils.save_to_mongo import save_to_mongo
from src.utils.calc_score import calc_score


train_values_path = get_config('file_paths.yaml', 'train_values')
train_labels_path = get_config('file_paths.yaml', 'train_labels')
scoring_name = get_config('global_parameters.yaml', 'scoring_func')
encoder_name = get_config('global_parameters.yaml', 'encoder')
scaler_name = get_config('global_parameters.yaml', 'scaler')
feature_selector_name = get_config('global_parameters.yaml', 'feature_selector')
model_name = get_config('global_parameters.yaml', 'model')
search_type = get_config('global_parameters.yaml', 'search_type')
cat_cols = get_cat_cols()

# preparation
df = separated_initial_data_load(train_values_path, train_labels_path)
df_dropped = drop_cols(df)
X_train, X_test, y_train, y_test = split_data(df_dropped)
encoder = select_encoder(cat_cols, encoder_name)
encoder = fitting(encoder, X_train, y_train)
X_train_enc = transforming(encoder, X_train)
X_test_enc = transforming(encoder, X_test)
scaler = select_scaler(scaler_name)
scaler = fitting(scaler, X_train_enc, y_train)
X_train_sca = transforming(scaler, X_train_enc)
X_test_sca = transforming(scaler, X_test_enc)
model = get_model(model_name)
feature_selector = feature_selector(feature_selector_name, model)
feature_selector = fitting(feature_selector, X_train_sca, y_train)
X_train_fs = transforming(feature_selector, X_train_sca)
X_test_fs = transforming(feature_selector, X_test_sca)


# train
clf = model_param_search(search_type, model_name)
clf = fitting(clf, X_train_fs, y_train)

estimator = str(clf.best_estimator_)
score_func = scoring_name
score = clf.best_score_
y_pred = clf.predict(X_test_fs)
test_score = calc_score(y_test, y_pred, scoring_name)
current_time = datetime.datetime.now()

inserted_value = save_to_mongo(estimator, score_func, score, test_score, current_time)
