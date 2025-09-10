import networkx as nx
import time

class BeliefGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_belief(self, node_id, content, source, certainty=1.0):
        timestamp = time.time()
        self.graph.add_node(node_id, content=content, source=source,
                            certainty=certainty, timestamp=timestamp)

    def add_dependency(self, src_id, dest_id, reason=None):
        self.graph.add_edge(src_id, dest_id, reason=reason)

    def detect_conflicts(self):
        conflicts = []
        for node1 in self.graph.nodes(data=True):
            for node2 in self.graph.nodes(data=True):
                if node1[0] != node2[0]:
                    if self._is_conflict(node1[1]['content'], node2[1]['content']):
                        conflicts.append((node1[0], node2[0]))
        return conflicts

    def _is_conflict(self, content1, content2):
        return content1.strip().lower() == f"not {content2.strip().lower()}"

    def visualize(self):
        try:
            import matplotlib.pyplot as plt
            nx.draw(self.graph, with_labels=True, node_color='lightblue')
            plt.show()
        except ImportError:
            print("Install matplotlib to visualize the graph.")