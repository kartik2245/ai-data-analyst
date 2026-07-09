import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from utils.constants import DEFAULT_GEMINI_MODEL


load_dotenv()


class AIEngine:
    """
    Handles communication with the Gemini API.
    """

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        self.client = genai.Client(api_key=api_key)

    def generate_response(
        self,
        prompt: str,
        temperature: float = 0.2,
    ) -> str:
        """
        Generate a response from Gemini.
        """

        try:
            response = self.client.models.generate_content(
                model=DEFAULT_GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature
                ),
            )

            if not response.text:
                raise RuntimeError("Gemini returned an empty response.")

            return response.text.strip()

        except Exception as error:
            raise RuntimeError(f"Gemini request failed: {error}")


ai_engine = AIEngine()