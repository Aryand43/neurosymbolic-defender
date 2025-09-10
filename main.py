import re
from neural_module import query_neural
from symbolic_module import check_math_equivalence, fact_check
from multiprocessing import freeze_support 
from dotenv import load_dotenv
load_dotenv()

def pipeline(input_query):
    print(f"\nQuery: {input_query}")

    # 1. Neural response from LLM
    try:
        neural_response = query_neural(input_query, model_key="gpt-5")
        print(f"Neural Output: {neural_response}")
    except Exception as e:
        neural_response = "[Neural Error]"
        print(f"Neural Output: {neural_response} - {e}")

    # 2. Symbolic check (with math expression extraction)
    try:
        math_match = re.search(r"([a-zA-Z0-9\*\^\+\-/\(\)\s]+)==([a-zA-Z0-9\*\^\+\-/\(\)\s]+)", input_query)
        if math_match:
            raw_expr1 = math_match.group(1).strip()
            raw_expr2 = math_match.group(2).strip()
            expr1, _ = extract_expression_from_text(raw_expr1)
            expr2, _ = extract_expression_from_text(raw_expr2)
            symbolic_check = check_math_equivalence(expr1, expr2)
            print(f"Symbolic Check: {symbolic_check}")
        else:
            print("Symbolic Check: [Skipped – No symbolic expression detected]")
    except Exception as e:
        print(f"Symbolic Check: [Error] - {e}")

    # 3. Fact-checking with DuckDuckGo
    try:
        tool_result = fact_check(input_query)
        print(f"Tool Result: {tool_result}")
    except Exception as e:
        print(f"Tool Result: [Error] - {e}")

if __name__ == "__main__":
    freeze_support()
    test_inputs = [
        "Check if x**2 == x*x",         # triggers symbolic check
        "Are sharks mammals?",          # factual query
        "Is 3 * (4 + 5) equal to 27?"   # factual/mixed query
    ]
    for q in test_inputs:
        pipeline(q)
