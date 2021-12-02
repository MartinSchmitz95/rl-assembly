import pandas as pd
import torch
from torch_geometric.data import Data

def load_graph(graph_path):
    node_dict, edge_dict = create_graph_from_csv(graph_path)
    print(len(node_dict), len(edge_dict))
    return None

def create_graph_from_csv(graph_path):
    df = pd.read_csv(graph_path, delimiter=" ", names=list(range(10)))
    node_dict = {}
    edge_dict = {}

    for index, row in df.iterrows():
        if (row[6][7] == "0"): # has 0 for node row, and 1 for edge row
            length = int(row[5][5:])
            node_dict[index] = length
            node_amount = index+1
        else: # edge row
            #(source_node_id, target_node_id, target_node_length, prefix len, similarity)
            edge_dict[index-node_amount] = (int(row[1][1:-1]), int(row[4][1:-1]), int(row[5][5:]), int(row[7]), int(row[9]))

    return node_dict, edge_dict
