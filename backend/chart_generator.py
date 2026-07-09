import pandas as pd
import plotly.express as px


class ChartGenerator:
    """
    Automatically generates Plotly charts from query results.
    """

    def _detect_column_types(self, dataframe: pd.DataFrame):

        numeric_columns = dataframe.select_dtypes(
            include=["number"]
        ).columns.tolist()

        categorical_columns = dataframe.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        datetime_columns = dataframe.select_dtypes(
            include=["datetime64[ns]", "datetime64"]
        ).columns.tolist()

        return (
            numeric_columns,
            categorical_columns,
            datetime_columns,
        )

    def generate_chart(self, dataframe: pd.DataFrame):

        if dataframe.empty:
            return None

        (
            numeric_columns,
            categorical_columns,
            datetime_columns,
        ) = self._detect_column_types(dataframe)

        try:

            if datetime_columns and numeric_columns:

                return px.line(
                    dataframe,
                    x=datetime_columns[0],
                    y=numeric_columns[0],
                    title="Trend Analysis",
                    markers=True,
                )

            if categorical_columns and numeric_columns:

                chart_data = dataframe.head(20)

                return px.bar(
                    chart_data,
                    x=categorical_columns[0],
                    y=numeric_columns[0],
                    title="Comparison",
                    text_auto=True,
                )

            if len(numeric_columns) == 1:

                return px.histogram(
                    dataframe,
                    x=numeric_columns[0],
                    nbins=20,
                    title="Distribution",
                )

            if len(numeric_columns) >= 2:

                return px.scatter(
                    dataframe,
                    x=numeric_columns[0],
                    y=numeric_columns[1],
                    title="Relationship",
                )

        except Exception:
            return None

        return None


chart_generator = ChartGenerator()