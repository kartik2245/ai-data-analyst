from pathlib import Path



APP_NAME = "AI Business Intelligence Platform"
APP_VERSION = "1.0.0"



BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = BASE_DIR / "assets"
PROMPTS_DIR = BASE_DIR / "prompts"
REPORTS_DIR = BASE_DIR / "reports"
DATABASE_DIR = BASE_DIR / "database"



DEFAULT_GEMINI_MODEL = "gemini-2.5-flash"



SUPPORTED_CSV_TYPES = [".csv"]



MAX_HISTORY = 20



DEFAULT_DB_SCHEMA = "public"



DEFAULT_CHART_HEIGHT = 500

DEFAULT_TEMPLATE = "plotly_white"



MAX_ROWS_DISPLAY = 1000

MAX_COLUMNS_DISPLAY = 50


MAX_SQL_RETRIES = 2

MAX_PROMPT_LENGTH = 25000



SQL_PROMPT_FILE = PROMPTS_DIR / "sql_prompt.txt"

ANALYSIS_PROMPT_FILE = PROMPTS_DIR / "analysis_prompt.txt"

CHART_PROMPT_FILE = PROMPTS_DIR / "chart_prompt.txt"



SCHEMA_FILE = DATABASE_DIR / "database_schema.txt"