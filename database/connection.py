import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


load_dotenv()


class DatabaseConnection:
    """
    Handles the PostgreSQL connection using SQLAlchemy.
    """

    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")

        if not self.database_url:
            raise ValueError("DATABASE_URL not found in environment variables.")

        self.engine = None

    def connect(self):
        """
        Create a SQLAlchemy engine.
        """

        if self.engine is None:
            self.engine = create_engine(
                self.database_url,
                pool_pre_ping=True,
                pool_size=5,
                max_overflow=10,
                pool_recycle=3600,
                future=True,
            )

        return self.engine

    def test_connection(self):
        """
        Verify database connectivity.
        """

        try:
            engine = self.connect()

            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))

            return True, "Database connected successfully."

        except SQLAlchemyError as error:
            return False, str(error)

    def dispose(self):
        """
        Close all pooled database connections.
        """

        if self.engine is not None:
            self.engine.dispose()
            self.engine = None


database = DatabaseConnection()