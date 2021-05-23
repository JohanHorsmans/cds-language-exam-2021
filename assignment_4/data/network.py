# Import module for specifying arguments from the terminal:
import argparse

# Import system tools
import os

# Import pandas for creating data-frames 
import pandas as pd

# Import modules for drawing and saving networks:
import networkx as nx
import matplotlib.pyplot as plt

# Set figure size:
plt.rcParams["figure.figsize"] = (20,20)

#Define function argument defaults and how to specify them from the terminal:
ap = argparse.ArgumentParser(description = "[DESCRIPTION]: A function designed to create networks and calculate metrics from a weighted edgelist with the following columns: (nodeA, nodeB, weight). The following parameters can be specified but you can also run the code with default parameters:")

ap.add_argument("-i", "--input", default = os.path.join("data", "weighted_edges_df.csv"), type = str, help = "string, path to input file and file name. [DEFAULT]: os.path.join(\"data\", \"weighted_edges_df.csv\")")

ap.add_argument("-t", "--threshold", default = 500, type = int, help = "integer, threshold for filtering (i.e. only include nodes with weights > threshold. [DEFAULT]: 500")

ap.add_argument("-p", "--plot_network", type = bool, default = True, nargs = "?", const = True, help = "boolean operator, Should the network be plotted or not? [DEFAULT]: TRUE")

ap.add_argument("-l", "--labels", default = True ,nargs = "?",const = True,type = bool, help = "boolean operator, should labels be included in the network or not. [DEFAULT]: TRUE")

ap.add_argument("-pf", "--plot_file", default = os.path.join("viz","network_visualization.png"), type = str, help = "str, where to save the plot output and file name [DEFAULT]: os.path.join(\"viz\", \"network_visualization.png\") ")

ap.add_argument("-o", "--output",default = os.path.join("output", "metrics.csv"), type = str, help = "str, path to output file and file name. [DEFAULT]: os.path.join(\"output\", \"metrics.csv\")")

args = vars(ap.parse_args())

# Define the function for the script:
def network( # Specify input arguments:
         input, 
         output,
         threshold, 
         labels,
         plot_network,
         plot_file):
    
    # Specify that if there does not exist a folder called "output", in the directory of the script, it is to be made:
    if not os.path.exists("output"):
            os.makedirs("output")
            
    # Specify that if there does not exist a folder called "out", in the directory of the script, it is to be made:
    if not os.path.exists("viz"):
            os.makedirs("viz")
    
    # Read the input .csv-file as a dataframe and save it as "data":
    data = pd.read_csv(input) 
    # Give a status update saying that the data has been loaded:
    print(f"[STATUS]: {input} has been loaded") 
    
    # Filter the data with the specified threshold and save the dataframe as "filtered_df":
    filtered_df = data[data["weight"] > threshold]
    
    # Calculate G:
    G = nx.from_pandas_edgelist(filtered_df, "nodeA", "nodeB", ["weight"])
    
    #Make the plot (unless "plot_network" == False):
    if plot_network == True: #If "plot_network" = True...
        pos = nx.nx_agraph.graphviz_layout(G, prog="neato") #... Create the plot ...
        nx.draw(G, pos, with_labels=labels, node_size=20, font_size=10) #... Draw the plot ...
        plt.savefig(plot_file, dpi=300, bbox_inches="tight") #... Save the plot in the specified "plot_file" location.
        
        # Give a status update saying that the plot has been saved:
        print(f"[STATUS]: {plot_file} has succesfully been saved") 
    
    # Calculate the various metrics:
    dg_metric = nx.degree_centrality(G) # Degrees
    bc_metric = nx.betweenness_centrality(G) # Betweennss
    ev_metric = nx.eigenvector_centrality(G) # Eigenvector
    
    # Creating dictionary with the various metrics:
    dictionary = {"node":dg_metric.keys(),"degrees":dg_metric.values(),"betweenness":bc_metric.values(),"eigenvector":ev_metric.values()}
    
    # Forming a data frame called "metrics_df" from the dictionary:
    metrics_df = pd.DataFrame(data = dictionary)
    
    # Saving the "metrics_df" dataframe as a .csv-file based on the specified output.
    metrics_df.to_csv(output)
    print(f"[STATUS]: {output} has succesfully been saved")
    
      # Define script arguments when it is run from the terminal.
if __name__ =="__main__":
    network(
      args["input"],
      args["output"],
      args["threshold"],
      args["labels"],
      args["plot_network"],
      args["plot_file"])