class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]
	def printSolution(self, dist):
		print()
		print("Starting pin point \t Time to reach from Source (mins)")
		for node in range(self.V):
			print(node, "\t\t\t", dist[node])
	def dijkstra(self, src):
		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V
		for cout in range(self.V):		
			min = 1e7
			for v in range(self.V):
				if dist[v] < min and sptSet[v] == False:
					min = dist[v]
					min_index = v
			u = min_index
			sptSet[u] = True
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]
		self.printSolution(dist)
y='y'
while(y=="y"):
	g = Graph(12)
	g.graph = [[0, 5, 5, 10, 10, 15, 30, 20, 20,10,15,10,25,30],
			[10, 0, 1, 15,10, 9, 30, 10, 10,20,10,20,20,30],
			[0, 5, 0, 10, 10, 15, 30, 20, 20,10,15,10,25,30],
			[15, 5, 0, 0, 10, 15, 30, 20, 20,10,15,10,25,30],
			[15, 5, 5, 1, 0, 15, 30, 20, 20,10,15,10,25,30],
			[25, 5, 5, 10, 0, 11, 30, 20, 20,10,15,10,25,30],
			[20, 5, 5, 10, 10, 1, 0, 20, 20,10,15,10,25,30],
			[4, 5, 5, 10, 10, 15, 0, 1, 20,10,15,10,25,30],
			[5, 5, 5, 10, 10, 15, 30, 0, 0,10,15,10,25,30],
			[10, 5, 5, 10, 10, 15, 30, 20, 20,0,15,10,25,30],
			[12, 5, 5, 10, 10, 15, 30, 20, 20,10,0,10,25,30],
			[3, 5, 5, 10, 10, 15, 30, 20, 20,10,15,0,25,30],
			[2, 5, 5, 10, 10, 15, 30, 20, 20,10,15,10,25,1]
			]
	print("\n\t\t\tLocations:")
	print()
	print("0.Clock tower")
	print("1.Rishab")
	print("2.Snow cube")
	print("3.Canteen")
	print("4.IT DEPT")
	print("5.Mechanical dept")
	print("6.CHemical")
	print("7.ECE Dept")
	print("8.EEE Dept")
	print("9.CS DEPT")
	print("10.Main auditoriam")
	print("11.Mini auditoriam")
	v=int (input("Enter a destination location (1,2,3...):="))
	g.dijkstra(v)
	y=input("Do u want to continue (y/n):")
