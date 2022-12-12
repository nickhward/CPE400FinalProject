import networkx as nx
import matplotlib.pyplot as plt #for displaying graph
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from Dijkstra import Dijkstra

import csv

def mainMenu(graph, graph2, failures):
    
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
    
 
def simulation(graph, graph2, failures):
    """_summary_

    Args:
        graph (_type_): _description_
        failures (_type_): _description_
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

def run_dijkstras(graph, graph2, nodeList, failed_node):
    dj = Dijkstra()
    nodeList.remove(failed_node)
    nodeListGraph2 = list(graph2.nodes)
    firstNodes = dict.fromkeys(nodeList)

    firstNodesGraph2 = dict.fromkeys(nodeListGraph2)


    #graph_new = graph
    graph.remove_node(failed_node)

    ##testing strategy 1
    for node in nodeList:
        firstNodes[node] = dj.run(node, nodeList, graph)
    
    print(f'For Strat 1: {firstNodes}')
    print()

    firstNodes.clear()

    adjacent_nodes = nx.neighbors(graph2, failed_node)
    for node in adjacent_nodes:
        firstNodesGraph2[node] = dj.run(node, nodeListGraph2, graph2)
    
    print(f'For Strat 2: {firstNodesGraph2}')

def main():
    """_summary_"""
    print("In main")
    #creating an empty graph
    G = nx.Graph()
    graph2 = nx.Graph()
    #array of failure percentages
    failures = [.05, .2, .45, .5, .03, .18, .56, .63, .32, .11, .60, .23, .79, .85, 0.9, .39]
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    #nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #Base graph with added edges and weights--> P = destination for dijkstra

    for node in nodes:
        G.add_node(node)

    with open('graphVals.csv', 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            G.add_edge(row[0], row[1], weight=row[2])
            graph2.add_edge(row[0], row[1], weight=row[2])

    pos=nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.savefig("simulated_graph.png")

    #call the main menu
    mainMenu(G, graph2, failures)



#calling main
if __name__ == '__main__':
    main() 


