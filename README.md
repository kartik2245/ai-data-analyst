# 📊 AI Data Analyst

An AI-powered data analysis application built with Streamlit, Pandas, LangChain, and Google's Gemini model. The application allows users to upload a CSV dataset, ask questions in natural language, generate charts, clean data, and receive AI-generated insights without writing Python code.

The goal of this project was to simplify exploratory data analysis by combining large language models with Python-based data processing into a single interactive application.

---

## Features

- Upload and analyze CSV datasets
- AI-powered natural language querying
- Automatic Pandas code generation
- Interactive data visualization
- AI-generated dataset insights
- Data cleaning using natural language
- Download cleaned datasets
- Export generated charts as PNG
- Generate downloadable PDF reports
- Dataset health summary
- Conversation memory during analysis

---

## Tech Stack

**Frontend**
- Streamlit

**Backend**
- Python

**Libraries**
- Pandas
- Matplotlib
- ReportLab
- LangChain
- Google Gemini API

---

## Project Structure

```
AI-Data-Analyst/
│
├── app.py
├── requirements.txt
├── assets/
├── data/
├── models/
├── prompts/
├── reports/
├── ui/
└── utils/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Data-Analyst.git
```

Move into the project

```bash
cd AI-Data-Analyst
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## Example Questions

You can ask questions such as:

- What is the average salary?
- Show a histogram of Amount.
- Remove duplicate rows.
- Fill missing values with median.
- Show the top 10 highest sales.
- Count employees older than 30.
- Generate AI insights for this dataset.

---

## Screenshots

Screenshots will be added here.

- Home Page
- AI Analysis
- Data Cleaning
- Charts
- AI Insights
- PDF Report

---

## What I Learned

While building this project, I learned how to:

- Build AI-powered applications using LangChain
- Work with Gemini for structured JSON responses
- Generate and execute dynamic Pandas code
- Build conversational data analysis workflows
- Handle AI-generated visualizations
- Generate PDF reports programmatically
- Design a modular Python project structure

---

## Future Improvements

Some ideas that can be added in future versions:

- Support for Excel files
- Multiple dataset analysis
- SQL database integration
- Interactive dashboards
- More visualization options
- User authentication
- Chat history export

---

## Author

**Kartik Marjara**

GitHub: https://github.com/kartik2245

LinkedIn: www.linkedin.com/in/kartik-marjara-11006017a
---

If you found this project interesting, feel free to fork it, raise an issue, or share your feedback.