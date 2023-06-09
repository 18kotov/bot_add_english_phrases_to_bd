import os
from settings import get_logger
from database_functions.commucation_with_db import post_query


logger = get_logger(__name__)


@post_query
def delete_phrase(english: str)->str:
    table = os.environ.get('TABLE')
    query = f"DELETE FROM {table} WHERE english = '{english}';"
    return query

