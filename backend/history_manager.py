from datetime import datetime

from utils.session_manager import add_history


class HistoryManager:
    """
    Manages application query history.
    """

    def create_entry(
        self,
        question: str,
        sql: str,
        row_count: int,
        summary: str,
    ) -> dict:
        """
        Create and store a history entry.
        """

        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "question": question,
            "sql": sql,
            "rows": row_count,
            "summary": summary,
        }

        add_history(
            question=question,
            sql=sql,
            response=summary,
        )

        return entry


history_manager = HistoryManager()