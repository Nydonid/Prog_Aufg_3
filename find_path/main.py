# This is a sample Python script.
import sys
import myParser

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# INFO:
# Um Programm zu bedienen, ist es nötig vorher lokal im Verzeichnis "pip install -e ." auszuführen, erst dann funktioniert der Programmaufruf

def main():

    # argv‑handling
    if len(sys.argv) == 3:
        # prüft, ob Argument im Terminal zwei Ausdrücke sind (Baum einlesen, dann ausgeben)
        filename = sys.argv[1]
        graph = myParser.readGraphFromFile(filename)
        start = sys.argv[2]
        ziel = sys.argv[2]

    else:
        # usage‑hinweis wie Programm richtig bedient wird.
        print("usage: find_path <filename_graph.txt> [start] [ziel]")
        sys.exit(1)

    print(graph)
    print(start, ziel)


if __name__ == '__main__':
    main()

