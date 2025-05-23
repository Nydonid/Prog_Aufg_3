from Edge import Edge

class Node:
    def __init__(self, name: str):
        self.name = name
        self.edges = []

    def addSingleEdge(self, edge: Edge):
      self.edges.append(edge)

    def distance(self, neighbor: str) -> int:
        for edge in self.edges:
            if edge.toNode.name == neighbor:
                return edge.cost
        return float('inf')  # Return infinity if no edge exists

    def getNeighbors(self):
        return [edge.toNode.name for edge in self.edges]

    def __repr__(self):
        return f"Node(name='{self.name}', edges={str(self.edges)})"