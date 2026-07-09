import pandas as pd

from backend.history_manager import history_manager
from backend.query_generator import query_generator
from backend.response_formatter import response_formatter

from database.execute_sql import execute_sql


class DatabaseAgent:
    """
    Coordinates the complete database query workflow.
    """

    def process_query(self, question: str) -> dict:
        """
        Process a natural language database query.
        """

        if not question.strip():
            raise ValueError("Question cannot be empty.")

        sql = query_generator.generate(question)

        dataframe = execute_sql(sql)

        summary = response_formatter.format_response(
            question=question,
            sql=sql,
            dataframe=dataframe,
        )

        history = history_manager.create_entry(
            question=question,
            sql=sql,
            row_count=len(dataframe),
            summary=summary,
        )

        return {
            "question": question,
            "sql": sql,
            "data": dataframe,
            "summary": summary,
            "history": history,
        }


db_agent = DatabaseAgent()