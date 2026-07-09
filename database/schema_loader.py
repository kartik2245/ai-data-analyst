from functools import lru_cache

from utils.constants import SCHEMA_FILE


@lru_cache(maxsize=1)
def load_schema():
    """
    Load the database schema from the schema file.
    The result is cached after the first read.
    """

    try:
        with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
            return file.read().strip()

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Schema file not found: {SCHEMA_FILE}"
        )

    except Exception as error:
        raise RuntimeError(
            f"Unable to load database schema.\n{error}"
        )