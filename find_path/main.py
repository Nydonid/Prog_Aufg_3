# This is a sample Python script.
import sys
import re
import os
from Graph import Graph
from Node import Node

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# INFO:
# Um Programm zu bedienen, ist es nötig vorher lokal im Verzeichnis "pip install -e ." auszuführen, erst dann funktioniert der Programmaufruf
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():

    # argv‑handling
    if len(sys.argv) == 4:
        # prüft, ob Argument im Terminal zwei Ausdrücke sind (Baum einlesen, dann ausgeben)
        filename = sys.argv[1]
        graph = readGraphFromFile(filename)
        start = sys.argv[2]
        ziel = sys.argv[3]
        findPathDijkstra(graph, start, ziel)

    else:
        # usage‑hinweis wie Programm richtig bedient wird.
        print("ATTENTION, correct usage: find_path <filename_graph.txt> [start] [ziel]")
        sys.exit(1)


def readGraphFromFile(filename: str) -> Graph:
    graph = Graph()

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


def findPathDijkstra(graph: Graph, start: str, destination: str):
    if start not in graph.nodes or destination not in graph.nodes:
        print(f"Invalid start or destination node")
        return

    visited = {}
    distances = {}
    possibleHub = []
    usedStations = []
    shortestDistanceFromCurrent = 0

    for node in graph.nodes:
        distances[node] = float('inf')

    distances[start] = 0
    currentNode = start

    while currentNode != destination:
        visited[currentNode] = True

        if len(graph.nodes[currentNode].getNeighbors()) >= 3:
            possibleHub.append(currentNode)

        for neighbourNode in graph.nodes[currentNode].getNeighbors():
            if neighbourNode not in visited:
                shortestDistanceFromCurrent = distances[currentNode] + graph.nodes[currentNode].distance(neighbourNode)
                if shortestDistanceFromCurrent < distances[neighbourNode]:
                    distances[neighbourNode] = shortestDistanceFromCurrent

        minDistance = float('inf')
        nextNode = None

        for node in graph.nodes:
            if node not in visited and distances[node] < minDistance:
                minDistance = distances[node]
                nextNode = node

        currentNode = nextNode

    print(usedStations)
    # print(f"Edges which are beeing passed: {distances}")


if __name__ == '__main__':
    main()

