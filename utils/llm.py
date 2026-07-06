from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_llm():
    """
    Returns a configured Gemini model.
    """

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )