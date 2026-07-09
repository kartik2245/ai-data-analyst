import pandas as pd

from backend.ai_engine import ai_engine

from utils.constants import ANALYSIS_PROMPT_FILE


class CSVAgent:
    """
    Handles AI analysis for uploaded CSV datasets.
    """

    def __init__(self):
        with open(
            ANALYSIS_PROMPT_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            self.prompt_template = file.read()

    def analyze(
        self,
        dataframe: pd.DataFrame,
        question: str,
    ) -> str:
        """
        Analyze a CSV dataset using Gemini.
        """

        if dataframe.empty:
            return "The uploaded CSV file is empty."

        preview = dataframe.head(10).to_markdown(index=False)

        prompt = self.prompt_template.format(
            question=question,
            result=preview,
            sql="Not Applicable"
        )

        return ai_engine.generate_response(prompt)


csv_agent = CSVAgent()