import re
import Graph

def readGraphFromFile(filename: str) -> Graph:
    graph = Graph.Graph()

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            try:
                line_name, data = line.split(":", 1)  # Split into line name and rest
            except ValueError:
                print(f"Invalid line format: {line}")
                continue

            dataFrameTokens = re.findall(r'"([^"]+)"\s*(\d+)?', data)  # Extract all station names and numbers
            tokens = [item for pair in dataFrameTokens for item in pair] # Used to remove brackets

            i = 0
            while i +2 < len(tokens):
                fromStation = tokens[i]

                try:
                    cost = int(tokens[i + 1])
                except ValueError:
                    break

                toStation = tokens[i + 2]
                graph.addEdge(fromStation, toStation, cost, line_name.strip())
                i += 2  # Move to the next token/ "station-cost" pair

    return graph
