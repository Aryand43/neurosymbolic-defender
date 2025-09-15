import re
from neural_module import query_neural
from symbolic_module import check_math_equivalence, fact_check
from belief_graph import BeliefGraph
from multiprocessing import freeze_support 
from dotenv import load_dotenv
load_dotenv()
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default="gpt-4o-mini", help='Model key to use (see neural_module.py)')
args = parser.parse_args()

# Initialize belief graph
belief_graph = BeliefGraph()
belief_counter = 1

def pipeline(input_query):
    global belief_counter
    print(f"\nQuery: {input_query}")

    # 1. Neural response from LLM
    try:
        neural_response = query_neural(input_query, model_key=args.model)
        print(f"Neural Output: {neural_response}")
        belief_graph.add_belief(f"n{belief_counter}", neural_response, source="neural", certainty=0.9)
        belief_counter += 1
    except Exception as e:
        neural_response = "[Neural Error]"
        print(f"Neural Output: {neural_response} - {e}")

    # 2. Symbolic check (with math expression extraction)
    try:
        math_match = re.search(r"([a-zA-Z0-9\*\^\+\-/\(\)\s]+)==([a-zA-Z0-9\*\^\+\-/\(\)\s]+)", input_query)
        if math_match:
            raw_expr1 = math_match.group(1).strip()
            raw_expr2 = math_match.group(2).strip()
            symbolic_check = check_math_equivalence(raw_expr1, raw_expr2)
            print(f"Symbolic Check: {symbolic_check}")
            belief_graph.add_belief(f"n{belief_counter}", f"{raw_expr1} == {raw_expr2} → {symbolic_check}", source="symbolic", certainty=1.0)
            belief_counter += 1
        else:
            print("Symbolic Check: [Skipped – No symbolic expression detected]")
    except Exception as e:
        print(f"Symbolic Check: [Error] - {e}")

    # 3. Fact-checking with DuckDuckGo
    try:
        tool_result = fact_check(input_query)
        print(f"Tool Result: {tool_result}")
        belief_graph.add_belief(f"n{belief_counter}", tool_result, source="tool", certainty=0.8)
        belief_counter += 1
    except Exception as e:
        print(f"Tool Result: [Error] - {e}")

    # 4. Conflict detection
    conflicts = belief_graph.detect_conflicts()
    if conflicts:
        print(f"Contradictions Detected: {conflicts}")
    else:
        print("No Contradictions Detected")

if __name__ == "__main__":
    freeze_support()
    test_inputs = [
        "Check if x**2 == x*x",         # triggers symbolic check
        "Are sharks mammals?",          # factual query
        "Is 3 * (4 + 5) equal to 27?"   # factual/mixed query
    ]
    for q in test_inputs:
        pipeline(q)
