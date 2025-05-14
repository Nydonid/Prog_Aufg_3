import Node

class Edge:
    def __init__(self, toNode: Node, cost: int, line: str):
        self.toNode = toNode
        self.cost = cost
        self.line = line

    def __repr__(self):
        return f"Edge(to={self.to_node.name}, cost={self.cost}, line='{self.line}')"