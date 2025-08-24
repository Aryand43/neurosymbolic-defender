from sympy import simplify, sympify, Eq, diff
import re

def check_symbolic(question, answer):
    cleaned_answer = answer.replace(" ", "").lower()

    # Handle derivatives
    if "derivative" in question.lower():
        try:
            expr_match = re.search(r"derivative of (.+)", question.lower())
            if expr_match:
                expr = sympify(expr_match.group(1))
                expected = str(diff(expr).simplify()).replace(" ", "").lower()
                if expected in cleaned_answer:
                    return f"Matches expected derivative ({expected})"
                else:
                    return f"[Symbolic Check Failed] Expected: {expected}, Neural said: {answer}"
        except:
            return "[Symbolic Check Failed]"

    # Simple factual logic
    elif "shark" in question.lower():
        return "False (sharks are not mammals)"

    # Handle basic arithmetic
    elif "*" in question or "+" in question:
        try:
            expr = re.search(r"what is (.+)\??", question.lower())
            if expr:
                result = str(eval(expr.group(1))).replace(" ", "").lower()
                if result in cleaned_answer:
                    return f"Matches expected arithmetic result ({result})"
                else:
                    return f"[Symbolic Math Check Failed] Expected: {result}, Neural said: {answer}"
        except:
            return "[Symbolic Math Check Failed]"

    return "No symbolic rule applied"
