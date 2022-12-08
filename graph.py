import networkx as nx
import matplotlib.pyplot as plt #for displaying graph
import sys
import random

def mainMenu(graph, failures):
    
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
            simulation(graph, failures)
        elif user == "2":
            sys.exit("Bye!")

        else:
            print("Please enter 1 or 2")

    #user = input("Response: ")
    #spring_layout = a dictionary where the nodes are the keys and their positions are values
    
    
    nx.draw(graph, pos=nx.spring_layout(graph), with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight') #defining edge labels to be the weights in the graph
    nx.draw_networkx_edge_labels(graph, pos=nx.spring_layout(graph), edge_labels=labels) #prints graph with weights
    nx.draw_networkx_edges(graph,pos=nx.spring_layout(graph),width=4, edge_color='g', arrows=False)

    plt.show()
def simulation(graph, failures):
    print("Inside of simulation")
    randomFailures = []
    i =0
    #Randomly Generating failures for each node
    #------------------------------------------
    while i < len(failures):
        fail = random.uniform(0,1)
        #print("Fail " , i , ": ", fail)
        randomFailures.append(fail)
        i += 1
    print("Random Failures array: ", randomFailures)
def main():
    print("In main")
    #creating an empty graph
    G = nx.Graph()
    #array of failure percentages
    failures = [.05, .2, .45, .5, .03, .18, .56, .63, .32, .11, .60, .23, .79, .85, 1.0, .39]
    #Base graph with added edges and weights--> P = destination for dijkstra
    G.add_edge("A", "B", weight=5)
    G.add_edge("B", "C", weight=15)
    G.add_edge("B", "E", weight=3)
    G.add_edge("E", "F", weight=9)
    G.add_edge("C", "F", weight=20)
    G.add_edge("F", "I", weight=1)
    G.add_edge("E", "D", weight=8)
    G.add_edge("D", "G", weight=12)
    G.add_edge("E", "H", weight=4)
    G.add_edge("G", "H", weight=9)
    G.add_edge("H", "J", weight=6)
    G.add_edge("J", "K", weight=7)
    G.add_edge("K", "L", weight=2)
    G.add_edge("L", "M", weight=1)
    G.add_edge("L", "N", weight=5)
    G.add_edge("K", "N", weight=1)
    G.add_edge("M", "O", weight=9)
    G.add_edge("N", "P", weight=6)
    G.add_edge("O", "P", weight=5)

    #call the main menu
    mainMenu(G, failures)


#calling main
if __name__ == '__main__':
    main() 


