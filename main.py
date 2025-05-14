# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import parser

def main():
    graph = parser.readGraphFromFile("ADS_Programmieraufgabe3_WienerVerkehrsNetz.txt")
    print(graph)

if __name__ == '__main__':
    main()

