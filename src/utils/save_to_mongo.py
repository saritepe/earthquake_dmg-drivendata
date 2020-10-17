from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv
from src.utils.get_config import get_config

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

database_url = os.environ.get("MONGO_DB_URL")


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient(database_url)


def save_to_mongo(estimator, score_func, score, test_score, created_on):
    connection = Connect.get_connection()
    project_name = get_config('project_information.yaml', 'project_name')
    project_type = get_config('project_information.yaml', 'project_type')
    col_name = get_config('project_information.yaml', 'col_name')

    db = getattr(connection, project_name)
    col = getattr(db, col_name)

    log_dict = dict()
    log_dict['project_name'] = project_name
    log_dict['project_type'] = project_type
    log_dict['estimator'] = estimator
    log_dict['score_func'] = score_func
    log_dict['score'] = score
    log_dict['test_score'] = test_score
    log_dict['created_on'] = created_on

    return col.insert_one(log_dict)
