import numpy, sys
import networkx as nx
from fibonacci_heap_mod import *

class edge_obj:
	def __init__(self, u, v, wt):
		self.wt = wt
		self.u = u
		self.v = v

class vertex_obj:
	def __init__(self, is_discovered, parent, vertex):
		self.is_discovered = is_discovered
		self.parent = parent
		self.vertex = vertex

def min_wt_btwn_nodes(u, v, G):
	lst = list()
	# print u, v, G[u][v]
	if G.has_edge(u, v):
		for z in G[u][v]:
			lst.append(G[u][v][z]['w'])
		return min(lst)
	else:
		return float("inf")

def BFS_max_edge(s, d, G, root):
	#print "inside bfs"
	vertex_dict = dict()
	queue = list()
	max_edge = -1.0
	mst_adj_list = dict()
	for n in G.nodes():
		vertex_dict[n] = vertex_obj(False, None, n)
		mst_adj_list[n] = list()
	for n in G.nodes():
		if n!=root:
			mst_adj_list[n].append(G.node[n]['parent'])
			mst_adj_list[G.node[n]['parent']].append(n)
	
	# print mst_adj_list	
	vertex_dict[s].is_discovered = True
	queue.append(vertex_dict[s])
	while(len(queue)!=0):
		u = queue[0].vertex
		del queue[0]
		# print mst_adj_list[u]
		for v in mst_adj_list[u]:
			if vertex_dict[v].is_discovered == False:
				vertex_dict[v].is_discovered = True
				vertex_dict[v].parent = u
				queue.append(vertex_dict[v])
	while(1):
		if d==s:
			break
		#print d, vertex_dict[d].parent
		wt = min_wt_btwn_nodes(d, vertex_dict[d].parent, G)
		if max_edge<wt:
			max_edge = wt
			max_edge_u = d
			max_edge_v = vertex_dict[d].parent
		d = vertex_dict[d].parent
		#print [max_edge_v, max_edge_u, max_edge]	
	return [max_edge_v, max_edge_u, max_edge, mst_adj_list]	

def computeMST(G, r):
	G.node[r]['key'] = 0.0
	f = Fibonacci_heap()
	for node_number in G.nodes():
		vertex_data = G.node[node_number]
		vertex_data['inQueue'] = 1
		fib_vertex_entry = f.enqueue(vertex_data, node_number, vertex_data['key'])
		vertex_data['fib_entry'] = fib_vertex_entry
	while(f.__bool__()):
		fib_heap_entry = f.dequeue_min()
		u = fib_heap_entry.m_node_number
		u_data = fib_heap_entry.m_elem
		u_data['inQueue'] = 0
		# print 'u :' + str(u)
		# print u_data
		for v in G.neighbors(u):
			v_data = G.node[v]
			min_wt_btwn_uv = min_wt_btwn_nodes(u, v, G)
			if (int(v_data['inQueue']) == 1) and (min_wt_btwn_uv<v_data['key']):
				# print v
				# print v_data
				v_data['parent'] = u
				v_data['key'] = min_wt_btwn_uv
				f.decrease_key(v_data['fib_entry'], v_data['key'])

	mst = 0.0

	for node_number in G.nodes():
		vertex_data = G.node[node_number]
		# print node_number, vertex_data['parent']
		mst = mst + vertex_data['key']
	return mst

def recomputeMST(u, v, wt, G, root, mst):
	[max_u, max_v, max_edge, mst_adj_list] = BFS_max_edge(u, v, G, root)
	#print max_u, max_v, max_edge
	if max_edge>wt:
		mst_adj_list[max_u].remove(max_v)
		mst_adj_list[max_v].remove(max_u)
		mst_adj_list[u].append(v)
		mst_adj_list[v].append(u)
		for n in G.nodes():
			G.node[n]['parent']=None
		r = root
		rprime = [r]
		while(len(rprime)!=0):
			r = rprime[0]
			del rprime[0]
			for e in mst_adj_list[r]:
				if G.node[e]['parent'] is None and e!=root:
					G.node[e]['parent'] = r
					G.node[e]['key'] = min_wt_btwn_nodes(e, r, G)
					rprime.append(e)
		#print "printing final mst"	
		#for n in G.nodes():
			#print n, G.node[n]['parent'], G.node[n]['key']
		return mst - max_edge + wt
	else:	
		#print "printing final mst"
		#for n in G.nodes():
	     		#print n, G.node[n]['parent'], G.node[n]['key']   
		return mst

def recomputeMST_existing(u, v, G, root):
	print 'in recompute'
	mst = 0.0
	A = list()
	set_lst = list()
	for n in G.nodes():
		n_data = G.node[n]
		if(n_data['parent'] is not None):
			min_wt_btwn = min_wt_btwn_nodes(n, n_data['parent'], G)
			if(n!=u and n!=v and n not in set(G.neighbors(u)) and n not in set(G.neighbors(u)) and n_data['parent'] not in set(G.neighbors(u)) and n_data['parent'] not in set(G.neighbors(v))):
				if len(set_lst)==0:
					s = set()
					s.add(n)
					s.add(n_data['parent'])
					A.append(edge_obj(n, n_data['parent'], min_wt_btwn))
					mst = min_wt_btwn
					set_lst.append(s)
				else:
					flg=0
					multi=list()
					for i, s in enumerate(set_lst):
						if n in s or n_data['parent'] in s:
							multi.append(i)
							s.add(n)
							s.add(n_data['parent'])
							if flg==0:
								A.append(edge_obj(n, n_data['parent'], min_wt_btwn))
								mst = mst + min_wt_btwn
							flg=1
					# print 'multi'
					# print multi
					if len(multi)>1:
						for z in range(len(multi)-1):
							set_lst[multi[0]] |= set_lst[multi[z+1]]
							del set_lst[multi[z+1]]
					if flg==0:
						s = set()
						s.add(n)
						s.add(n_data['parent'])
						A.append(edge_obj(n, n_data['parent'], min_wt_btwn))
						mst = mst + min_wt_btwn
						set_lst.append(s)
	
	in_set = set()
	for s in set_lst:
		in_set |= s
	for n in list(set(G.nodes()) - in_set):
		set_lst.append(set([n]))

	print set_lst

	edge_lst = list()
	for n in G.neighbors(u):
		min_wt_btwn_un = min_wt_btwn_nodes(u, n, G)
		edge_lst.append(edge_obj(u, n, min_wt_btwn_un))
	for n in G.neighbors(v):
		min_wt_btwn_vn =  min_wt_btwn_nodes(v, n, G)
		if n!=u:
			edge_lst.append(edge_obj(v, n, min_wt_btwn_vn))
	edge_lst.sort(key=lambda x: x.wt)
	for elem in edge_lst:
		print elem.u, elem.v, elem.wt
		for i, s in enumerate(set_lst):
			if elem.u in s:
				flg_u = i
			if elem.v in s:
				flg_v = i
		if(flg_u!=flg_v):
			mst = mst + elem.wt
			A.append(elem)
			set_lst[flg_u] |= set_lst[flg_v]
			del set_lst[flg_v]
	print 'sd'
	for elem in A:
		print elem.u, elem.v, elem.wt
	for n in G.nodes():
		G.node[n]['parent']=None
	for i, elem in enumerate(A):
		if elem.u==root:
			G.node[elem.v]['parent'] = elem.u
			G.node[elem.v]['key'] = elem.wt
			nxt = elem.v
			del A[i]
			break
		elif elem.v==root:
			G.node[elem.u]['parent'] = elem.v
			G.node[elem.u]['key'] = elem.wt
			nxt = elem.u
			del A[i]
			break

	while(1):
		flg=0
		for i, elem in enumerate(A):
			if elem.u==nxt:
				flg=1
				if (G.node[elem.v]['parent'] is None):
					G.node[elem.v]['parent']=elem.u
					G.node[elem.v]['key'] = elem.wt
				else:
					G.node[elem.u]['parent']=elem.v					
					G.node[elem.u]['key']=elem.wt
				nxt = elem.v
				del A[i]
				break
			elif elem.v==nxt:
				flg=1
				if G.node[elem.u]['parent'] is None:
					G.node[elem.u]['parent']=elem.v
					G.node[elem.u]['key']=elem.wt
				else:
					G.node[elem.v]['parent']=elem.u
					G.node[elem.v]['key']=elem.wt
				nxt = elem.u
				del A[i]
				break
		if flg==0 and len(A)!=0:
			nxt = G.node[nxt]['parent']	
		elif len(A)==0:
			break
	
	for n in G.nodes():
		print n, G.node[n]['parent']
	return mst
	
