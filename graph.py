# graph.py

# class Graph:
# 	def __init__(self, )

class Graph:

	def __init__(self, nodes={}, size=0):		
		self.nodes = nodes
		self.size = size

	def get_node(self, key):
		nodes = self.nodes
		if key in nodes:
			node = nodes[key]
			return node
		return None

	def print_all_nodes(self, detail=False):

		if not detail:
			print "\ndisplaying all nodes of this graph:"
			for key in self.nodes:
				self.print_node(key)
			return True
		# detailed version:
		print "\ndisplaying all nodes of this graph in detail:"
		for key in self.nodes:
			self.print_node(key)
		return True		

	def print_node(self, key):
		node = self.get_node(key)
		if node:
			print "key: " + str(node.key)
			print "value: " + str(node.value)
			print "neighbours: " + str(node.edges)
			print ""

			return True
		return False

	def get_neighbours(self, key):
		if key not in self.nodes:
			print "key " + key + " belongs to no node in graph"
			return False

		node = self.nodes[key]
		edges = node.edges
		neighbours = []
		for key in edges:
			neighbour = self.get_node(key)
			neighbours.append(neighbour)

		return neighbours

	def get_path(self, start, end, path=[]):
		path.append(start)
		current_node = self.get_node(start)

		if start == end:
			return path		

		if len(current_node.edges) == 0:
			path.remove(start)
			return None

		for edge in current_node.edges:
			newpath = self.get_path(edge, end, path)
			if newpath:
				# print newpath
				return newpath

		# path does not exist
		return None



class Node:

	def __init__(self, key, value, edges=[]):
		self.key = key
		self.value = value
		self.edges = edges

	def get_neighbour(neighbour_key):
		edges = self.edges
		if neighbour_key in edges:
			neighbour_node = edges[neighbour_key]
			return neighbour_node

		return None

# example graph

graph = Graph( {	
	0 : Node(0, 'value0', [1,2,3,4]),
	1 : Node(1, 'value1', [2,3]),
	2 : Node(2, 'value2'),
	3 : Node(3, 'value3'),
	4 : Node(4, 'value4', [5]),
	5 : Node(5, 'value5')
	} )

graph.print_all_nodes()

print "find_path (0, 5):"
print graph.get_path(0, 5)
