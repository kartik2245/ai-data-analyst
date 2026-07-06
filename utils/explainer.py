from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from utils.llm import get_llm
from prompts.explanation_prompt import SYSTEM_PROMPT


def explain_result(question: str, code: str, result) -> str:

    llm = get_llm()

    prompt = ChatPromptTemplate.from_template(
        SYSTEM_PROMPT +
        """

Question:
{question}

Generated Code:
{code}

Execution Result:
{result}
"""
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke(
        {
            "question": question,
            "code": code,
            "result": result
        }
    )

    return response.strip()