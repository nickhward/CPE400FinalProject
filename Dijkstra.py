import networkx as nx

class Dijkstra(object):
  def __init__(self):
    self.source = None
    self.unvisited = None
    self.shortest_nodes = None #the adjacent node to the source needed to take the shortest path to the destination
    self.shortest_paths = None
    
  def run(self, pSource, pUnvisited, graph):
    """_summary_

    Args:
        pSource (_type_): _description_
        pUnvisited (_type_): _description_
        graph (_type_): _description_

    Returns:
        _type_: _description_
    """
    self.source = None    #clear any previous data stored in the class members
    self.unvisited = None
    self.shortest_nodes = None
    self.shortest_paths = None
    
    
    self.source = pSource   #insert parameters' data in members
    self.unvisited = pUnvisited
    self.shortest_nodes = dict.fromkeys(pUnvisited)
    self.shortest_paths = dict.fromkeys(pUnvisited, float("inf")) #10000 is infinity for our purposes
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
      next_node = 'A'
      for y in nodes_to_check:
        
        if(self.shortest_paths[y] < next_path and y in self.unvisited):
          next_path = self.shortest_paths[y]
          next_node = y
      
      if len(self.unvisited) != 0: nodes_to_check.remove(next_node)
      current_node = next_node
      
      #take a currently unvisited node whose path is the shortest and call adjacent_nodes, removes node from unvisited list
      
    return self.shortest_nodes #to save on memory, the algorithm only returns the first node in the path to any destination
      
  def adjacent_nodes(self, node, graph):
    """_summary_

    Args:
        node (_type_): _description_
        graph (_type_): _description_
    """
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
    """_summary_

    Args:
        source (_type_): _description_
        neighbor (_type_): _description_
        graph (_type_): _description_
    """
    weight = graph.get_edge_data(source, neighbor)

    added_cost = self.shortest_paths[source] + int(weight['weight'])
    
    if( added_cost < self.shortest_paths[neighbor]):
      self.shortest_paths[neighbor] = added_cost
      if neighbor in nx.neighbors(graph, self.source):
        self.shortest_nodes[neighbor] = neighbor
      else:
        self.shortest_nodes[neighbor] = self.shortest_paths[source]
    
