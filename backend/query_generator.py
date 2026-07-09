import re
from pathlib import Path

from backend.ai_engine import ai_engine
from database.schema_loader import load_schema
from utils.constants import SQL_PROMPT_FILE


class QueryGenerator:
    """
    Generates PostgreSQL queries from natural language.
    """

    def __init__(self):
        self.schema = load_schema()
        self.prompt_template = self._load_prompt()

    @staticmethod
    def _load_prompt() -> str:
        """
        Load the SQL prompt template.
        """

        prompt_path = Path(SQL_PROMPT_FILE)

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt file not found: {prompt_path}"
            )

        return prompt_path.read_text(encoding="utf-8")

    def build_prompt(self, question: str) -> str:
        """
        Build the prompt sent to Gemini.
        """

        return self.prompt_template.format(
            schema=self.schema,
            question=question,
        )

    @staticmethod
    def clean_sql(sql: str) -> str:
        """
        Remove markdown formatting returned by Gemini.
        """

        sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
        sql = re.sub(r"```", "", sql)

        return sql.strip()

    def generate(self, question: str) -> str:
        """
        Generate PostgreSQL SQL.
        """

        prompt = self.build_prompt(question)

        sql = ai_engine.generate_response(prompt)

        return self.clean_sql(sql)


query_generator = QueryGenerator()