import re


def _columns_from_schema(schema: str) -> list[str]:
    columns = []

    for line in schema.splitlines():
        value = line.strip()

        if not value or value.lower() in {"columns", "schema"}:
            continue

        columns.append(value)

    return columns


def _find_column(question: str, schema: str) -> str | None:
    question_lower = question.lower()

    for column in _columns_from_schema(schema):
        if column.lower() in question_lower:
            return column

    return None


def generate_code(schema: str, question: str) -> str:
    """Generate simple pandas expressions for legacy tests and scripts."""

    text = question.lower()
    column = _find_column(question, schema)

    if column is None:
        match = re.search(r"\b(?:average|mean|sum|maximum|max|minimum|min|median)\s+(\w+)", text)
        if match:
            column = match.group(1).title()

    if column and ("average" in text or "mean" in text):
        return f'df["{column}"].mean()'

    if column and ("maximum" in text or "max" in text):
        return f'df["{column}"].max()'

    if column and ("minimum" in text or "min" in text):
        return f'df["{column}"].min()'

    if column and "sum" in text:
        return f'df["{column}"].sum()'

    if column and "median" in text:
        return f'df["{column}"].median()'

    if "count" in text:
        return "len(df)"

    return "df.head()"
