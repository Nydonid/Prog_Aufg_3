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

            tokens = re.findall(r'"([^"]+)"\s*(\d+)', data)  # Extract all station names and numbers

            i = 0
            while i < len(tokens) - 2:
                fromStation = tokens[i]

                try:
                    # cost = int(tokens[i + 1])
                    cost = 2
                except ValueError:
                    break

                toStation = tokens[i + 2]
                graph.addEdge(fromStation, toStation, cost, line_name.strip())
                i += 2  # Move to the next token/ "station-cost" pair

    return graph
