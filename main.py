import os.path
import load_assembly_graph_from_csv as fromcsv

def main_routine():

    graph_path = os.path.join("ecoli", "graph_1.csv")
    graph = fromcsv.load_graph(graph_path)
    print(graph)

if __name__ == '__main__':
    main_routine()

