#!/usr/bin/python
##  CSE6140 HW1
##  This assignment requires installation of networkx package if you want to make use of available graph data structures or you can write your own!!
##  Please feel free to modify this code or write your own
import networkx as nx
import time
import sys
import scipy, numpy, math
from MST import computeMST, min_wt_btwn_nodes, recomputeMST

class RunExperiments:
    def read_graph(self, filename):
        #make sure to add to filename the directory where it is located and the extension .txt
        #G = nx.MultiGraph()
        #if you want to use networkx

        #Write code to add nodes and edges
        #Check out add_node, add_edge in networkx
        G = nx.MultiGraph()
        f = open(filename, "r")
        f.readline()
        for line in f:
        	lst = line.split()
        	G.add_nodes_from([int(lst[0]), int(lst[1])], key=float('inf'), parent=None, inQueue=0)
        	G.add_edge(int(lst[0]), int(lst[1]), w=float(lst[2]))
        f.close()
        return G

    def main(self):

        num_args = len(sys.argv)

        if num_args < 4:
            print "error: not enough input arguments"
            exit(1)

        graph_file = sys.argv[1]
        change_file = sys.argv[2]
        output_file = sys.argv[3]

        #Construct graph
        G = self.read_graph(graph_file)

        start_MST = time.time() #time in seconds
        root = 0
        MSTweight = computeMST(G, root) #call MST function to return total weight of MST
        total_time = (time.time() - start_MST) * 1000 #to convert to milliseconds
	print MSTweight
	#for n in G.nodes():
		#print n, G.node[n]['parent']

        #Write initial MST weight and time to file
        output = open(output_file, 'w')
        output.write(str(MSTweight) + " " + str(total_time) + "\n")
        

        # Changes file
        f = open(change_file, 'r')
        f.readline()
        for line in f:
        	print line
        	lst = line.split()
        	u = int(lst[0])
        	v = int(lst[1])
        	wt = float(lst[2])
        	if u in set(G.nodes()):
        		u_data = G.node[u]
        	else:
        		u_data = {}
        	if v in set(G.nodes()):
        		v_data = G.node[v]
        	else:
        		v_data = {}
        	# print u_data, v_data, min_wt_btwn_nodes(u, v, G)
		min_wt = min_wt_btwn_nodes(u, v, G)
		G.add_edge(u, v, w=wt)
		start_recompute = time.time()
		# check for self loops
		if len(u_data)!=0 and len(v_data)!=0:
			if u==v:
				MSTweight = MSTweight
			elif (v_data['parent']==u) and wt<min_wt:
				MSTweight = MSTweight - v_data['key'] + wt
				v_data['key'] = wt
			elif (u_data['parent']==v) and wt<min_wt:
				MSTweight = MSTweight - u_data['key'] + wt
				u_data['key'] = wt
			elif (u_data['parent']!=v and v_data['parent']!=u and wt<min_wt):
				MSTweight = recomputeMST(u, v, wt, G, root, MSTweight)
		if len(u_data)==0:
			G.add_nodes_from([u], key=wt, parent=v, inQueue=0)
			MSTweight = MSTweight + wt
		if len(v_data)==0:
			G.add_nodes_from([v], key=wt, parent=u, inQueue=0)
			MSTweight = MSTweight + wt
		print MSTweight
		total_recompute = (time.time() - start_recompute)*1000
		output.write(str(MSTweight) + " " + str(total_recompute) + "\n")
	f.close()
	output.close()

if __name__ == '__main__':
    # run the experiments
    runexp = RunExperiments()
    runexp.main()
