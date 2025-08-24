def use_tool(question):
    if "3 * (4 + 5)" in question:
        return 3 * (4 + 5)
    elif "sharks" in question.lower():
        return "No, sharks are fish."
    elif "derivative" in question.lower():
        return "2*x"
    return "Tool not configured for this input"