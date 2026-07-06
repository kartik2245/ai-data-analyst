import pandas as pd


def clean_data(df, agent):

    operation = agent["operation"]

    cleaned_df = df.copy()

    if operation == "remove_duplicates":

        before = len(cleaned_df)

        cleaned_df = cleaned_df.drop_duplicates()

        after = len(cleaned_df)

        message = f"Removed {before-after} duplicate rows."

    elif operation == "drop_missing":

        before = len(cleaned_df)

        cleaned_df = cleaned_df.dropna()

        after = len(cleaned_df)

        message = f"Removed {before-after} rows containing missing values."

    elif operation == "fill_missing":

        method = agent["method"]

        for column in cleaned_df.columns:

            if cleaned_df[column].isnull().sum() == 0:
                continue

            if pd.api.types.is_numeric_dtype(cleaned_df[column]):

                if method == "mean":
                    cleaned_df[column] = cleaned_df[column].fillna(
                        cleaned_df[column].mean()
                    )

                elif method == "median":
                    cleaned_df[column] = cleaned_df[column].fillna(
                        cleaned_df[column].median()
                    )

            else:

                cleaned_df[column] = cleaned_df[column].fillna(
                    cleaned_df[column].mode()[0]
                )

        message = f"Filled missing values using {method}."

    else:

        return df, "Unsupported cleaning operation."

    return cleaned_df, message