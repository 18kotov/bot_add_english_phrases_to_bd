from settings import get_logger
from datetime import datetime
from database_functions.commucation_with_db import post_query

logger = get_logger(__name__)

@post_query
def add_phrases(english: str, russian: str, date=datetime.today()):
    query = f"INSERT INTO phrases (english, russian, date) VALUES('{english}','{russian}', '{date}');"
    return query









if __name__ == '__main__':
    pass


