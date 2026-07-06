import re


def _extract_column(question: str) -> str | None:
    match = re.search(r"\b(?:of|for|by)\s+([A-Za-z_][\w\s]*)", question, re.IGNORECASE)
    if not match:
        return None

    return match.group(1).strip().rstrip("?.")


def detect_chart(question: str) -> dict:
    """Detect a simple chart request from natural language."""

    text = question.lower()

    if "histogram" in text or "distribution" in text:
        return {
            "task": "chart",
            "chart": "histogram",
            "column": _extract_column(question),
        }

    if "bar" in text:
        return {
            "task": "chart",
            "chart": "bar",
            "column": _extract_column(question),
        }

    if "pie" in text:
        return {
            "task": "chart",
            "chart": "pie",
            "column": _extract_column(question),
        }

    if "scatter" in text:
        return {
            "task": "chart",
            "chart": "scatter",
        }

    if "line" in text:
        return {
            "task": "chart",
            "chart": "line",
        }

    return {
        "task": "unknown",
    }
