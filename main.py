import os.path
import load_assembly_graph_from_csv as fromcsv


print("Hello World")
graph_path = os.path.join("ecoli", "graph_1.csv")
graph = fromcsv.load_graph(graph_path)
print(graph)