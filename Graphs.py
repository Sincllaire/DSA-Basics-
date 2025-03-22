class Graph:
    def __init__(self, directed=False):
        """
        Initialize the Graph as directed or undirected.
        """
        self.directed = directed
        self.adj_list = {}

    def add_edge(self, source, destination, weight=None):
        """
        Add an edge between source and destination.
        function( use the things given in the self quotes to help you in code)
        if source not in adj_list:
            return "error: no source in list"
        if destination not in adj_list:
            return "error: no destination node in list"
        if weight is None: (for unweighted graph)
            if destination not in adj_list[source]:
                append destination to sources('s adajecncy list)
            else:(for weighted graph)
            store destination in sources dict. with the weight
        if graph is undirected:
            repeat the same process for destination -> source

        -first we check to see if the source and the destination exists in the adj_list
        -if it does, then second we need to iterate through the giving data. else: return error
        -next we divide it based off of weighted and unweighted
        - if it is weighted we will store them in a list, append to the list. Lists are dynamic
        - if it is weighted, we will add them to a dictionary and do the same if it gets too full. (i forgot if a dictionary was or wasnt static)
        - to close out the if/else, else: say data is not in adj_list(return an error)
        """
        if source not in self.adj_list:
            return "error: no source in list"
        if destination not in self.adj_list:
            return "error: no destination node in list"
        if weight is None: 
            if destination not in self.adj_list[source]:
                self.adj_list[source].append(destination)
        else:
            self.adj_list[source][destination] = weight 
     

        if not self.directed:
            if weight is None: 
                self.adj_list[destination].append(source)
            else:
                self.adj_list[destination][source] = weight 
            

        pass

    def remove_edge(self, source, destination):
        """
        Remove an edge between source and destination.
        1. if source not in self.adj_list:
        return "error"
        2. if destination not in self.adj_list:
        return "error"
        3. if graph is unweighted:
        self.adj_list[source].remove(destination)
        4. else:
            del self.adj_list[source][destination]
       # 5. if not self.directed:
        6. if graph is unweighted:
        7. self.adj_list[destination].remove(source)
        8. else:
            del self.adj_list[destination][source]
        """
        if source not in self.adj_list:
            return "error: no source"
        if destination not in self.adj_list:
            return "error: no destination"
        if weight is None: 
            self.adj_list[source].remove(destination)
        else:
            del self.adj_list[source][destination]

        if not self.directed:
            self.adj_list[destination].remove(source)
        else:
            del self.adj_list[destination][source]


        pass

    def get_neighbors(self, vertex):
        """
        Retrieve the neighbors of a given vertex.
       1. if vertex is in self.adj_list:
       return self.adj_list[vetext]
       else:
       return "error no vertex exists"
        """
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else:
            return "error no vertex exists"
        pass

    def dfs(self, start_vertex):
        """
        Perform Depth-First Search starting from the given vertex.
        1. if start_vertex in self.adj_list:
        stack = [start_vertex]
        2. visited = set()
        3. while stack:
        4. current = stack.pop()
        5. visited.add(current)
        6. for neighbor in self.adj_list[current]
        7. if neighbor not in visited:
        8. stack.append(neighbor)

        """
        if start_vertex in self.adj_list:
            stack = [start_vertex]
            visited = set()
            while stack:
                current = stack.pop()
                visited.add(current)
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        pass

    def bfs(self, start_vertex):
        """
        Perform Breadth-First Search starting from the given vertex.
        1. if start_vertex in self.adj_list:
        2. queue = [start_vertex]
        3. visited = set()
        4. while queue:
        5. current = queue.pop(0) #pop the end not the beginning 
        6. visited.add(current)
        7. for neighbor in self.adj_list[current]:
        8. if neighbor not in visited:
        9.queue.append(neighbor)
        """
        if start_vertex in self.adj_list:
            queue = [start_vertex]
            visited = set()
            while queue:
                current = queue.pop(0) #pop the end not the beginning 
                visited.add(current)
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        pass

# Example Usage (for testing)
# graph = Graph(directed=True)
# graph.add_edge("A", "B")