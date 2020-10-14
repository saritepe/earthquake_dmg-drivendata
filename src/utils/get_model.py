from sklearn.tree import DecisionTreeClassifier


from src.utils.get_config import get_config


random_state = get_config("global_parameters.yaml", "random_state")


def get_model(model_name):
    if model_name == 'dtc':
        # TODO global variable needs to change
        return DecisionTreeClassifier(random_state=random_state)
    else:
        # TODO other models should be added
        print("Model couldn't find.")
