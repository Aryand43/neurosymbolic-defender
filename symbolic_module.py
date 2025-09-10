from dotenv import load_dotenv
load_dotenv()

import re
import sys
from multiprocessing import freeze_support
from sympy import symbols, simplify, sympify
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)
from langchain.agents import Tool, initialize_agent
from langchain_community.chat_models import ChatOpenAI
from langchain_community.utilities import SerpAPIWrapper

# Init symbols and transformations
x, y, z = symbols("x y z")
transformations = standard_transformations + (implicit_multiplication_application, convert_xor)
search = SerpAPIWrapper()

# --- TOOL LOGIC ---

def check_math_equivalence(expr1: str, expr2: str) -> str:
    try:
        parsed_expr1 = simplify(sympify(expr1, transformations=transformations))
        parsed_expr2 = simplify(sympify(expr2, transformations=transformations))
        return "Equivalent" if parsed_expr1.equals(parsed_expr2) else "Not Equivalent"
    except Exception as e:
        return f"[SymPy Error: {e}]"

def _safe_equivalence_check(q: str) -> str:
    try:
        match = re.search(r"(.+)==(.+)", q)
        if not match:
            return "[Parse Error: Missing '==' separator]"

        expr1 = match.group(1).strip()
        expr2 = match.group(2).strip()

        return check_math_equivalence(expr1, expr2)
    except Exception as e:
        return f"[Tool Error: {e}]"

def fact_check(query: str) -> str:
    try:
        return search.run(query)
    except Exception as e:
        return f"[Fact Check Error: {e}]"

# --- AGENT ---

def create_agent():
    tools = [
        Tool(
            name="Math Equivalence Checker",
            func=_safe_equivalence_check,
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

# --- MAIN ---

def main():
    agent = create_agent()
    print(agent.run("Check if x**2 == x*x"))
    print(agent.run("Are sharks mammals?"))

if __name__ == "__main__":
    freeze_support()
    main()