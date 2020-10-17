from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score


def calc_score(y_test, y_pred, score_func_name):
    score = 0
    if score_func_name == 'roc_auc':
        score = roc_auc_score(y_test, y_pred)
    elif score_func_name == 'f1':
        score = f1_score(y_test, y_pred)
    elif score_func_name == 'f1_micro':
        score = f1_score(y_test, y_pred, average='micro')
    elif score_func_name == 'f1_macro':
        score = f1_score(y_test, y_pred, average='macro')
    elif score_func_name == 'precision':
        score = precision_score(y_test, y_pred)
    elif score_func_name == 'recall':
        score = recall_score(y_test, y_pred)
    elif score_func_name == 'accuracy':
        score = accuracy_score(y_test, y_pred)
    return score
