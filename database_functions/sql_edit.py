from settings import get_logger
from database_functions.commucation_with_db import post_query


logger = get_logger(__name__)


@post_query
def delete_phrase(english: str)->str:
    query = f"DELETE FROM phrases WHERE english = '{english}';"
    return query

