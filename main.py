from neural_module import query_neural
from symbolic_module import check_symbolic
from tool_module import use_tool
from dotenv import load_dotenv
load_dotenv()

def pipeline(input_query):
    print(f"\nQuery: {input_query}")

    neural_response = query_neural(input_query, model_key="gpt-5") 
    print(f"Neural Output: {neural_response}")

    symbolic_check = check_symbolic(input_query, neural_response)
    print(f"Symbolic Check: {symbolic_check}")

    tool_result = use_tool(input_query)
    print(f"Tool Result: {tool_result}")

if __name__ == "__main__":
    test_inputs = [
        "What is the derivative of x**2?",
        "Is it true that sharks are mammals?",
        "What is 3 * (4 + 5)?"
    ]
    for q in test_inputs:
        pipeline(q)
