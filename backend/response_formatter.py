import pandas as pd

from backend.ai_engine import ai_engine
from utils.constants import ANALYSIS_PROMPT_FILE


class ResponseFormatter:
    """
    Generates business-friendly insights from SQL query results.
    """

    def __init__(self):
        with open(
            ANALYSIS_PROMPT_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            self.prompt_template = file.read()

    def format_response(
        self,
        question: str,
        sql: str,
        dataframe: pd.DataFrame,
    ) -> str:
        """
        Generate an AI explanation for the SQL results.
        """

        if dataframe.empty:
            return "No records were found for your query."

        preview = dataframe.head(10).to_markdown(index=False)

        prompt = self.prompt_template.format(
            question=question,
            sql=sql,
            result=preview
        )

        return ai_engine.generate_response(prompt)
        

response_formatter = ResponseFormatter()