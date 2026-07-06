import pandas as pd


def get_schema(df: pd.DataFrame) -> str:
    """
    Returns a text description of the dataframe.
    This will be sent to Gemini so it understands
    the dataset before answering questions.
    """

    schema = []

    schema.append(f"Rows: {df.shape[0]}")
    schema.append(f"Columns: {df.shape[1]}")
    schema.append("")

    schema.append("Column Information:")

    for column in df.columns:
        schema.append(f"- {column} ({df[column].dtype})")

    return "\n".join(schema)