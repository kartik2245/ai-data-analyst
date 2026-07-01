"""
Data Loader

This module is responsible for reading datasets from file uploads and returning
structured pandas DataFrames ready for analysis. It handles encoding detection,
parse errors, and empty-file validation.
"""

import pandas as pd


class DataLoadError(Exception):
    """Raised when a CSV file cannot be loaded or parsed."""


def load_csv(uploaded_file) -> pd.DataFrame:
    """
    Read a CSV file from a Streamlit UploadedFile or any file-like object.

    Attempts UTF-8 decoding first, then falls back to latin-1 for files with
    non-standard encodings.

    Args:
        uploaded_file: A file-like object with read/seek support
                       (e.g. a Streamlit UploadedFile).

    Returns:
        pd.DataFrame: The parsed CSV data.

    Raises:
        DataLoadError: If no file is provided, the file is empty, the CSV is
                       malformed, or the encoding cannot be determined.
    """
    if uploaded_file is None:
        raise DataLoadError("No file provided.")

    try:
        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file, encoding="utf-8")

    except UnicodeDecodeError:
        # Retry with latin-1 for files that use legacy encodings
        try:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding="latin-1")
        except Exception as exc:
            raise DataLoadError(
                "Unable to decode file. Please ensure the CSV uses a supported encoding."
            ) from exc

    except pd.errors.EmptyDataError as exc:
        raise DataLoadError("The CSV file is empty.") from exc

    except pd.errors.ParserError as exc:
        raise DataLoadError(f"Unable to parse CSV file: {exc}") from exc

    except Exception as exc:
        raise DataLoadError(
            f"An unexpected error occurred while reading the file: {exc}"
        ) from exc

    if df.empty and len(df.columns) == 0:
        raise DataLoadError("The CSV file contains no data or column headers.")

    return df
