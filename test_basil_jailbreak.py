def test_contradiction_detection():
    from belief_graph import BeliefGraph
    g = BeliefGraph()
    g.add_belief("a", "Paris is the capital of France", source="neural")
    g.add_belief("b", "not Paris is the capital of France", source="tool")
    assert g.detect_conflicts() == [("a", "b")]