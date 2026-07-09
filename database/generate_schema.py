import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

from utils.constants import SCHEMA_FILE


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found.")


engine = create_engine(DATABASE_URL)


def get_tables(connection):
    query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public'
    AND table_type='BASE TABLE'
    ORDER BY table_name;
    """

    return [row[0] for row in connection.execute(text(query))]


def get_columns(connection, table_name):
    query = """
    SELECT
        column_name,
        data_type
    FROM information_schema.columns
    WHERE table_schema='public'
    AND table_name=:table
    ORDER BY ordinal_position;
    """

    return connection.execute(
        text(query),
        {"table": table_name},
    ).fetchall()


def get_primary_keys(connection):
    query = """
    SELECT
        tc.table_name,
        kcu.column_name
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
      ON tc.constraint_name = kcu.constraint_name
    WHERE tc.constraint_type='PRIMARY KEY'
      AND tc.table_schema='public';
    """

    rows = connection.execute(text(query)).fetchall()

    return {
        (table, column)
        for table, column in rows
    }


def get_foreign_keys(connection):
    query = """
    SELECT
        tc.table_name,
        kcu.column_name,
        ccu.table_name AS foreign_table,
        ccu.column_name AS foreign_column
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
      ON tc.constraint_name = kcu.constraint_name
    JOIN information_schema.constraint_column_usage ccu
      ON ccu.constraint_name = tc.constraint_name
    WHERE tc.constraint_type='FOREIGN KEY'
      AND tc.table_schema='public';
    """

    rows = connection.execute(text(query)).fetchall()

    foreign_keys = {}

    for table, column, foreign_table, foreign_column in rows:

        foreign_keys[(table, column)] = (
            foreign_table,
            foreign_column,
        )

    return foreign_keys


def generate_schema():

    with engine.connect() as connection:

        tables = get_tables(connection)

        primary_keys = get_primary_keys(connection)

        foreign_keys = get_foreign_keys(connection)

        lines = []

        lines.append("DATABASE SCHEMA\n")
        lines.append("=" * 80)
        lines.append("\n")

        for table in tables:

            lines.append(f"\nTABLE: {table}")
            lines.append("-" * 80)

            columns = get_columns(
                connection,
                table,
            )

            for column_name, data_type in columns:

                description = f"{column_name} ({data_type})"

                if (table, column_name) in primary_keys:
                    description += " [PRIMARY KEY]"

                if (table, column_name) in foreign_keys:

                    fk_table, fk_column = foreign_keys[
                        (table, column_name)
                    ]

                    description += (
                        f" -> {fk_table}.{fk_column}"
                    )

                lines.append(description)

        with open(
            SCHEMA_FILE,
            "w",
            encoding="utf-8",
        ) as file:

            file.write("\n".join(lines))

        print(f"\nSchema written to:\n{SCHEMA_FILE}")


if __name__ == "__main__":
    generate_schema()