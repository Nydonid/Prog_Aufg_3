# This is a sample Python script.
import sys
import re
import os
from Graph import Graph

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
        ziel = sys.argv[2]

    else:
        # usage‑hinweis wie Programm richtig bedient wird.
        print("ATTENTION, correct usage: find_path <filename_graph.txt> [start] [ziel]")
        sys.exit(1)

    print(graph)
    print(start, ziel)


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


if __name__ == '__main__':
    main()

