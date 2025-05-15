import Edge
import Node


class Graph:
    def __init__(self):
        self.nodes = {}

    def getOrCreateNode(self, name: str) -> Node: # Returns the Node with the given name, creating it if necessary.
        if name not in self.nodes:
            self.nodes[name] = Node.Node(name)
        return self.nodes[name]

    def addEdge(self, from_name: str, to_name: str, cost: int, line: str): # Adds a bidirectional connection between two stations.
        from_node = self.getOrCreateNode(from_name)
        to_node = self.getOrCreateNode(to_name)

        from_node.addSingleEdge(Edge.Edge(to_node, cost, line)) # Add edges to both directions, as it is bidirectional
        to_node.addSingleEdge(Edge.Edge(from_node, cost, line))

        # print("new EDGE direction 1: \n" + " " + str(from_node) + "\n" + " " + str(to_node))
        # print("new EDGE direction 2: \n" + " " + str(to_node) + "\n" + " " + str(from_node))

    def __repr__(self) -> str:
        return f"Graph({len(self.nodes)} stations)"
