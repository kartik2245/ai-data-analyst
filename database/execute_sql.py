import re

import pandas as pd

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from database.connection import database


FORBIDDEN_KEYWORDS = {
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE",
    "GRANT",
    "REVOKE",
}


MAX_RESULT_ROWS = 10000


def validate_query(sql: str):
    """
    Validate that the SQL query is safe to execute.
    Only read-only SELECT/CTE queries are permitted.
    """

    if not sql or not sql.strip():
        raise ValueError("SQL query cannot be empty.")

    query = sql.strip().upper()

    if not (
        query.startswith("SELECT")
        or query.startswith("WITH")
    ):
        raise PermissionError(
            "Only SELECT queries are allowed."
        )

    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", query):
            raise PermissionError(
                f"Forbidden SQL keyword detected: {keyword}"
            )


def execute_sql(sql: str) -> pd.DataFrame:
    """
    Execute a validated SQL query and return the results
    as a Pandas DataFrame.
    """

    validate_query(sql)

    engine = database.connect()

    try:

        with engine.connect() as connection:

            dataframe = pd.read_sql(
                text(sql),
                connection,
            )

        if len(dataframe) > MAX_RESULT_ROWS:
            dataframe = dataframe.head(MAX_RESULT_ROWS)

        return dataframe

    except SQLAlchemyError as error:

        raise RuntimeError(
            f"Database execution failed.\n{error}"
        )