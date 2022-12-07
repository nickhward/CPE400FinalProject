class Dijkstra(object):
  def _init_(self):
    self.source = none
    self.unvisited = none
    self.edges = none
    self.shortest_nodes = none #the adjacent node to the source needed to take the shortest path to the destination
    self.shortest_paths = none
    
  def run(self, pSource, pUnvisited, pEdges):
    self.source = none    #clear any previous data stored in the class members
    self.unvisited.clear()
    self.edges.clear()
    self.shortest_nodes.clear()
    self.shortest_paths.clear()
    
    self.source = pSource   #insert parameters' data in members
    self.unvisited = pUnvisited
    self.edges = pEdges
    
    while(len(self.unvisited) > 0):
      #take a currently unvisited node whose path is the shortest and call adjacent_nodes, removes node from unvisited list
      
    return self.shortest_nodes #to save on memory, the algorithm only returns the first node in the path to any destination
      
  def adjacent_nodes(self, node):
    #identify adacent nodes and the cost to travel to them, ignore source node
    
    #add the current node's shortest_path and the cost to travel to the adjacent nodes and make that the 
    #adjacent node's shortest path only if it is set to zero (default) or shorter than its current value
    #update shortest_nodes if shortest path requires a different adjacent node from the source than the previous shortest path
    #if current node is adjacent to the source, set corresponding shortest_node to itself, otherwise set it to current node's shortest_node
    
    
    
