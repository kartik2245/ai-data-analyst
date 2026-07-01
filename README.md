# AI Data Analyst

An intelligent data analysis application powered by Python and large language models. Upload datasets, ask questions in natural language, and receive automated insights, visualizations, and structured reports.

## Project Description

AI Data Analyst is designed to streamline the end-to-end data analysis workflow. Users provide raw data files, and the application handles loading, cleaning, exploratory analysis, chart generation, and narrative report creation — all orchestrated through an LLM-driven analyst interface.

## Folder Structure

```
ai-data-analyst/
│
├── app.py                  # Application entry point
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
├── .env.example            # Environment variable template
│
├── data/                   # Input datasets (CSV, Excel, etc.)
├── reports/                # Generated analysis reports
├── assets/                 # Static assets (images, templates)
├── prompts/                # LLM prompt templates
│   └── analyst_prompt.py
│
├── utils/                  # Core utility modules
│   ├── data_loader.py      # Dataset loading and validation
│   ├── data_cleaner.py     # Data cleaning and preprocessing
│   ├── visualizer.py       # Chart and plot generation
│   ├── llm.py              # LLM client and interaction layer
│   └── report_generator.py # Report assembly and export
│
└── models/                 # Data models and schemas
```

## Tech Stack

- **Language:** Python 3.10+
- **LLM Provider:** Google Generative AI (Gemini)
- **Data Processing:** pandas, numpy
- **Visualization:** matplotlib, seaborn, plotly
- **Environment Management:** python-dotenv

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd ai-data-analyst
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS / Linux
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and set your `GOOGLE_API_KEY`.

5. **Run the application**

   ```bash
   python app.py
   ```
