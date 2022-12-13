import networkx as nx
from typing import List
import time
class Dijkstra(object):
  def __init__(self):
    self.source = None
    self.unvisited = None
    self.shortest_nodes = None #the adjacent node to the source needed to take the shortest path to the destination
    self.shortest_paths = None
    self.packet_times = []
    
    
  def run(self, pSource: str, pUnvisited: List, graph: nx.Graph) -> dict:
    """runs the Dijkstra's algorithm

    Args:
        pSource (str): source node
        pUnvisited (List): list of unvisted nodes
        graph (nx.Graph): graph of nodes

    Returns:
        dict: Dictionary with nodes of the network with their respective values
    """

    self.source = None    #clear any previous data stored in the class members
    self.unvisited = None
    self.shortest_nodes = None
    self.shortest_paths = None
    
    self.source = pSource   #insert parameters' data in members
    self.unvisited = pUnvisited.copy()
    self.shortest_nodes = dict.fromkeys(pUnvisited)
    self.shortest_paths = dict.fromkeys(pUnvisited, float("inf"))
    self.shortest_nodes[self.source] = self.source
    self.shortest_paths[self.source] = 0
    current_node = self.source
    nodes_to_check = []
        
    while(len(self.unvisited) > 0):
      self.unvisited.remove(current_node)
      self.adjacent_nodes(current_node, graph)
      adjacencies = nx.neighbors(graph, current_node)
      for x in adjacencies:
        if x in self.unvisited:
          nodes_to_check.append(x)
      next_path = float("inf")
      next_node = 1
      for y in nodes_to_check:
        
        if(self.shortest_paths[y] < next_path and y in self.unvisited):
          next_path = self.shortest_paths[y]
          next_node = y
      
      if len(self.unvisited) != 0: nodes_to_check.remove(next_node)
      current_node = next_node
      
    #take a currently unvisited node whose path is the shortest and call adjacent_nodes, removes node from unvisited list
    return self.shortest_nodes #to save on memory, the algorithm only returns the first node in the path to any destination
      
  def adjacent_nodes(self, node, graph):
   
    #identify adacent nodes and the cost to travel to them, ignore source node
    adjacencies = nx.neighbors(graph, node)
    #add the current node's shortest_path and the cost to travel to the adjacent nodes and make that the 
    #adjacent node's shortest path only if it is set to 10000 (default) or shorter than its current value
    #update shortest_nodes if shortest path requires a different adjacent node from the source than the previous shortest path
    for x in adjacencies:
      if x in self.unvisited:
        self.compare_costs(node, x, graph)
    #if current node is adjacent to the source, set corresponding shortest_node to itself, otherwise set it to current node's shortest_node
    
  def compare_costs(self, source, neighbor, graph):
    #get the weights of the edge between nodes
    weight = graph.get_edge_data(source, neighbor)
    if(weight == None):
        weight = graph.get_edge_data(neighbor, source)

    #calculating added costs
    added_cost = self.shortest_paths[source] + int(weight['weight'])
    
    if( added_cost < self.shortest_paths[neighbor]):
      self.shortest_paths[neighbor] = added_cost
      
      self.packet_times.append(added_cost*0.01)
      
      if neighbor in nx.neighbors(graph, self.source):
        self.shortest_nodes[neighbor] = neighbor
      else:
        self.shortest_nodes[neighbor] = self.shortest_nodes[source]
    

