import os
from settings import get_logger
from database_functions.commucation_with_db import post_query

logger = get_logger(__name__)

@post_query
def add_phrases(english: str, russian: str):
    table = os.environ.get('TABLE')
    query = f"INSERT INTO {table} (english, russian) VALUES('{english}','{russian}');"
    return query









if __name__ == '__main__':
    pass


