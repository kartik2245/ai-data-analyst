from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from utils.llm import get_llm
from prompts.insights_prompt import SYSTEM_PROMPT


def generate_insights(summary):

    llm = get_llm()

    prompt = ChatPromptTemplate.from_template(
        SYSTEM_PROMPT
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke(
        {
            "summary": summary
        }
    )

    return response.strip()