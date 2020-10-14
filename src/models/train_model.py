from sklearn import model_selection


from src.utils.get_model_params import model_param_selector
from src.utils.get_model import get_model
from src.utils.get_config import get_config
from src.features.cross_validation import select_cv


def model_param_search(search_type, model_name):
    param_path = 'global_parameters.yaml'

    cv_name = get_config(param_path, 'cv')
    cv_n_split = get_config(param_path, 'cv_n_split')
    cv_n_repeats = get_config(param_path, 'cv_n_repeats')
    n_jobs = get_config(param_path, 'n_jobs')
    verbose = get_config(param_path, 'verbose')
    rnd_src_n_iter = get_config(param_path, 'rnd_src_n_iter')
    random_state = get_config(param_path, 'random_state')

    params = model_param_selector(model_name)
    model = get_model(model_name)

    cv = select_cv(cv_name, cv_n_split, cv_n_repeats, random_state)

    return getattr(model_selection, search_type)(model, params, cv=cv, verbose=verbose, n_jobs=n_jobs,
                                                 random_state=random_state, n_iter=rnd_src_n_iter)


#def model_train()