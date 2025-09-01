from langchain.agents import Tool, initialize_agent
from langchain_community.chat_models import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from sympy import simplify, sympify
import re

search = DuckDuckGoSearchRun()

def check_math_equivalence(expr1: str, expr2: str) -> str:
    try:
        parsed_1 = sympify(expr1)
        parsed_2 = sympify(expr2)
        if simplify(parsed_1 - parsed_2) == 0:
            return "Math expressions are equivalent"
        else:
            return f"Not equivalent: {parsed_1} ≠ {parsed_2}"
    except:
        return "[Math Check Error]"


def fact_check(query: str) -> str:
    try:
        return search.run(query)
    except:
        return "[Fact Check Error]"

def create_agent():
    tools = [
        Tool(
            name="Math Equivalence Checker",
            func=lambda q: check_math_equivalence(q.split("==")[0], q.split("==")[1]),
            description="Use this tool to check if two math expressions are symbolically equivalent. Input format: <expr1>==<expr2>"
        ),
        Tool(
            name="Fact Checker",
            func=fact_check,
            description="Use this tool to verify factual claims about the real world"
        )
    ]

    llm = ChatOpenAI(temperature=0, model="gpt-4")
    return initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)


def main():
    agent = create_agent()
    print(agent.run("Check if x**2 == x*x"))
    print(agent.run("Are sharks mammals?"))


if __name__ == "__main__":
    main()