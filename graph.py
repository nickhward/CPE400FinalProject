import networkx as nx
import matplotlib.pyplot as plt #for displaying graph
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List
from Dijkstra import Dijkstra
import time
from itertools import combinations, groupby
import networkx as nx
import random


import csv

def mainMenu(graph: nx.Graph, graph2: nx.Graph, failures: List) -> None:
    """controls the user input and directions of the 

    Args:
        graph (nx.Graph): graph for strategy 1
        graph2 (nx.Graph): graph for strategy 2
        failures (List): list of node failure values
    """
    
    #print("Hello!\n What would you like to do?")
    #print("Press 1 for Run simulation")
    #print("Press 2 for Exit")
    #user = input("Hello! What would you like to do?")
    while (True):
        print("Press 1 for Run simulation")
        print("Press 2 for Exit")
        user = input("Hello! What would you like to do?")

            #continue
        if user == "1":
            #call the simulation           
            print("User chose 1")
            simulation(graph, graph2, failures)
        elif user == "2":
            sys.exit("Bye!")

        else:
            print("Please enter 1 or 2")

    #user = input("Response: ")
    #spring_layout = a dictionary where the nodes are the keys and their positions are values
    
 
def simulation(graph: nx.Graph, graph2: nx.Graph, failures: List):
    """creates the simulation of the network

    Args:
        graph (nx.Graph): graph of strategy 1
        graph2 (nx.Graph) : graph of strategy 2
        failures (List): list of node failures
    """
    print("Inside of simulation")
    randomFailures = []
    i =0
    #Randomly Generating failures between 0 and 1 for each node
    #------------------------------------------
    while i < len(failures):
        fail = random.uniform(0,1)
        #print("Fail " , i , ": ", fail)
        randomFailures.append(fail)
        i += 1
    print("Random Failures array: ", randomFailures)

    #for each node in the passed in failures and randomly generated failures, check if the value is higher in the random failures
    #if so keep the index of the node and if there's multiple, check which value has the greatest; if equal delete the one with highest weighted edge
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    deleteIndex = []
    for x, y in zip(failures, randomFailures):
        #x = element in failures
        #y = element in randomFailures
        if y > x:
            deleteIndex.append(randomFailures.index(y))
            print("The element in failures: ", x)
            print("The element in random failures: ", y)

    print("List of indices of elements to delete: ", deleteIndex)
    #check if the size of the list of possible to be deleted nodes greater than 1, if so check which one has the largest difference
    differences = []
    if len(deleteIndex) > 1:
        for e in deleteIndex:
            diff = randomFailures[e] - failures[e]
            differences.append(diff)
    
        print("Differences: ", differences)
        #finding largest difference and storing its index to use to get node supposed to delete from graph
        idx = differences.index(max(differences))
        print("Want index of the largest difference: ", idx)

    else:
        #means there was only one node in the graph who's random failure was greater than their initital
        #then the element you want to delete is the index provided in the deleteIndex list
        idx = deleteIndex[0]
    
    #getting list of nodes to retrieve the node at the founded index that had the largest failure difference
    nodeList = list(graph.nodes)

    failed_node = nodeList[idx]
    print("Node want to delete: ", failed_node)
    #removing node
    #graph.remove_node(node)

    #printing new graph with removed node
    #***ADD HERE HOW TO RECONNECT GRAPH WITH DIJKSTRA and will print the graph with node removed and it being reconnected***

    run_dijkstras(graph, graph2, nodeList, failed_node)

def initial_dijkstras(graph: nx.Graph, graph2: nx.Graph, nodeList: List, firstNodes, firstNodesGraph2):
    dj1 = Dijkstra()
    dj2 = Dijkstra()
    
    nodeListGraph2 = list(graph2.nodes)
    

    for node in nodeList:
        firstNodes[node] = dj1.run(node, nodeList, graph)

    for node in nodeListGraph2:
        firstNodesGraph2[node] = dj2.run(node, nodeListGraph2, graph2)



def run_dijkstras(graph: nx.Graph, graph2: nx.Graph, nodeList: List, failed_node: str) -> None:
    """Run the dijkstras algorithm on:
       Strategy 1: If all nodes of the network rework their routes
       Strategy 2: If adjacent nodes rework their routes

    Args:
        graph (nx.Graph): graph of strategy 1
        graph2 (nx.Graph): graph of strategy 2
        nodeList (List): list of all the node names in the graphs [A, B, C, D, .... , P]
        failed_node (str): node that failed in the simulated network
    """
    #calling dijkstra class
    dj1 = Dijkstra()
    dj2 = Dijkstra()

    #removing the node that failed in this simulated network
    nodeListGraph2 = list(graph2.nodes)
    firstNodes = dict.fromkeys(nodeList)
    
    firstNodesGraph2 = dict.fromkeys(nodeListGraph2)
    initial_dijkstras(graph, graph2, nodeList, firstNodes, firstNodesGraph2)

    
    nodeList.remove(failed_node)
    nodeListGraph2.remove(failed_node)
    nodeListUnchanged = nodeList.copy()
    nodeListUnchanged2 = nodeListGraph2.copy()
    
    

    
    
    start_time = time.time()
    #removing the failed node from the graph
    graph.remove_node(failed_node)

    ##testing strategy 1
    for node in nodeList:
        firstNodes[node] = dj1.run(node, nodeList, graph)
    end_time = time.time()
    elapsed_time1 = end_time - start_time
    print(f'For Strat 1: {firstNodes}')
    print(f'Elapsed Time: {elapsed_time1}')
    print('--------------------------------------')
   # print(time_lists1)
    
    #firstNodes.clear()
    #testing strategy 2
    #get adjacent nodes to that failed node
    
    start_time = time.time()
    
    adjacent_nodes = nx.neighbors(graph2, failed_node)
    graph2.remove_node(failed_node)
    for node in adjacent_nodes:
        firstNodesGraph2[node] = dj2.run(node, nodeListGraph2, graph2)
    end_time = time.time()
    elapsed_time2 = end_time - start_time
    print(f'For Strat 2: {firstNodesGraph2}')
    print(f'Elapsed Time: {elapsed_time2}')
    
    

    time_lists1 = []
    time_lists2 = []
    source = random.choice(nodeListUnchanged)
    destination = random.choice(nodeListUnchanged)
    print(source, destination)
    start_time = time.time()
    current_node = source
    weight_total = 0
    print(firstNodes)
    while(current_node != destination):
        if firstNodes[source] != None:
            print(current_node)
            next_node = firstNodes[current_node][destination]
            print(next_node)
            weight = graph.get_edge_data(current_node, next_node)
            print(weight)
            weight_total += int(weight['weight'])
            time_lists1.append(int(weight['weight']))
            current_node = next_node
            print(weight_total)
    time.sleep(weight_total*0.01)
    print(weight_total)
    end_time = time.time()

    elapsed_time1 = end_time - start_time

    
    print(source, destination)
    start_time = time.time()
    current_node = source
    weight_total = 0
    print(firstNodesGraph2)
    while(current_node != destination):
        if firstNodesGraph2[source] != None:
            print(current_node)
            next_node = firstNodesGraph2[current_node][destination]
            print(next_node)
            weight = graph2.get_edge_data(current_node, next_node)
            print(weight)
            weight_total += int(weight['weight'])
            time_lists2.append(int(weight['weight']))
            current_node = next_node
            print(weight_total)
    time.sleep(weight_total*0.01)
    print(weight_total)
    end_time = time.time()

    elapsed_time2 = end_time - start_time
    print(f'Elapsed first strategy time: {elapsed_time1}')
    print(f'Elapsed second strategy time: {elapsed_time2}')

    print(time_lists1)
    print()
    print(time_lists2)

    plt.figure()
    plt.plot(time_lists1, label='Strategy 1')
    plt.plot(time_lists2, label='Strategy 2')
    plt.ylabel('Packet Times')
    plt.title('Packet Time Simulator')
    plt.legend(['Strategy 1', 'Strategy 2'])
    plt.savefig("simulated_packet_times.png")
    plt.show()


def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge, weight=random.uniform(1,50))
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e, weight=random.uniform(1,50))
    return G








def main():
    """Create graphs by pulling node and weight data from csv, save graph to png"""
    print("In main")
    #creating an empty graph
    G = nx.Graph()
    graph2 = nx.Graph()
    #array of failure percentages
    #failures = [.05, .2, .45, .5, .03, .18, .56, .63, .32, .11, .60, .23, .79, .85, 0.9, .39,.44, .33, .67,.71,.13,.26,.79,.82,.51,.61]
    #nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q','R','S','T','U','V','W','X','Y','Z']
    
    nodes = 200
    failures = [random.uniform(0.1, 1.0) for _ in range(nodes)]

    
    seed = random.randint(1,10)
    probability = 0.1
    G = gnp_random_connected_graph(nodes,probability)
    graph2 = gnp_random_connected_graph(nodes,probability)

    plt.figure(figsize=(8,5))
    nx.draw(G, node_color='lightblue', 
        with_labels=True, 
        node_size=500)
    #Base graph with added edges and weights--> P = destination for dijkstra

    #for node in nodes:
     #   G.add_node(node)
    #get node data from csv file
    #with open('graphVals.csv', 'r') as file:
     #   csvreader = csv.reader(file)
      #  for row in csvreader:
       #     G.add_edge(row[0], row[1], weight=row[2])
        #    graph2.add_edge(row[0], row[1], weight=row[2])

    #drawing a graph using the networkx library from the pulled csv file
    pos=nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    
    #saving graph image to project directory
    plt.savefig("simulated_graph.png")

    #call the main menu
    mainMenu(G, graph2, failures)



#calling main
if __name__ == '__main__':
    main() 


