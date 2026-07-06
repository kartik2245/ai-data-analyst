import json

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from utils.llm import get_llm
from prompts.agent_prompt import SYSTEM_PROMPT


def run_agent(schema: str, question: str, history=None):

    if history is None:
        history = []

    conversation = ""

    for message in history:

        conversation += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    llm = get_llm()

    prompt = ChatPromptTemplate.from_template(
        SYSTEM_PROMPT +
        """

Conversation History:

{history}

Current Question:

{question}
"""
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke(
        {
            "schema": schema,
            "history": conversation,
            "question": question
        }
    )

    cleaned = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned)