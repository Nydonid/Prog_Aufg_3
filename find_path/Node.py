import Edge

class Node:
    def __init__(self, name: str):
        self.name = name
        self.edges = []

    def addSingleEdge(self, edge: Edge):
      self.edges.append(edge)

    def __repr__(self):
        return f"Node(name='{self.name}', edges={str(self.edges)})"