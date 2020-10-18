from sklearn.pipeline import Pipeline
import datetime

from src.utils.get_config import get_config
from src.utils.get_model import get_model
from src.utils.save_to_mongo import save_to_mongo
from src.utils.calc_score import calc_score
from src.utils.get_sample import sampling
from src.data.load_data import separated_initial_data_load
from src.data.categorize_data import get_cat_cols
from src.features.drop_cols import drop_cols
from src.features.split_data import split_data
from src.features.encoding import select_encoder
from src.features.scaling import select_scaler
from src.features.feature_selector import feature_selector
from src.features.fitting import fitting
from src.features.transforming import transforming
from src.features.decompositioning import decompositioning
from src.models.train_model import model_param_search


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
sample_data = sampling(df_dropped)

X_train, X_test, y_train, y_test = split_data(sample_data)
encoder = select_encoder(cat_cols, encoder_name)


scaler = select_scaler(scaler_name)
pca = decompositioning(2, 'PCA')
model = get_model(model_name)
feature_selector = feature_selector(feature_selector_name, model)

# train
clf = model_param_search(search_type, model_name)

steps = [('encoder', encoder), ('scaler', scaler), ('pca', pca), ('feature_selector_name', feature_selector),
         (model_name, clf)]

pipe = Pipeline(steps)

pipe.fit(X_train, y_train)

estimator = 'deneme'
# str(clf.best_estimator_)
score_func = scoring_name
score = pipe.score(X_train, y_train)
y_pred = pipe.predict(X_test)
test_score = calc_score(y_test, y_pred, scoring_name)
current_time = datetime.datetime.now()

inserted_value = save_to_mongo(estimator, score_func, score, test_score, current_time)
