import json

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None


#############################################################################
# This is the algorithm I came up with for BFT
#############################################################################
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting vertex
        qq = Queue()
        qq.enqueue(starting_vertex)
        # Create a set of visited vertices
        ############################################################
        # The definition of a visited vertex is one whose neighbors
        # have been already entered in the queue before
        ############################################################
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue the vertex at the head of the queue
            current_vertex = qq.dequeue()
            if current_vertex not in visited:
                # mark as visited
                visited.add(current_vertex)
                # DO THE THING!!!!!!!
                #########################################################
                # Perform action on current_vertex once it is added to 
                # visited set for the frist time
                #########################################################
                print(current_vertex)
                # enqueue all neightbors
                for next_vert in self.get_neighbors(current_vertex):
                    qq.enqueue(next_vert)


#############################################################################
# This is the algorithm the instructor used in the guided lecture for BFT
#############################################################################
    def bftOFF2(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack and push starting vertex into it
        ss = Stack()
        ss.push(starting_vertex)
        # Create a set of visited vertices
        ############################################################
        # The definition of a visited vertex is one whose neighbors
        # have been already entered in the stack before
        ############################################################
        visited = set()
        # While stack is not empty:
        while ss.size() > 0:
            # pop the vertex at the top of the stack
            current_vertex = ss.pop()
            if current_vertex not in visited:
                # mark as visited
                visited.add(current_vertex)
                # DO THE THING!!!!!!!
                #########################################################
                # Perform action on current_vertex once it is added to 
                # visited set for the frist time
                #########################################################
                print(current_vertex)
                # push all neightbors into stack
                for next_vert in self.get_neighbors(current_vertex):
                    ss.push(next_vert)



    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create visited set if it does not exist
        if visited == None:
            visited = set()
            self.dft_recursive(starting_vertex,visited)
            return

        # Base case
        if starting_vertex in visited:
            return

        # Recursive case
        visited.add(starting_vertex)
        print(starting_vertex)
        for next_vert in self.get_neighbors(starting_vertex):
            self.dft_recursive(next_vert,visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue and enqueue a path (list) containing starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])

        # Create a set of visited vertices
        ############################################################
        # The definition of a visited vertex is one whose neighbors
        # have been already entered in the queue before. The 
        # neighbors are inside a path list
        ############################################################
        visited = set()

        # Create a flag to indicate when the shortest path is found
        pathFound = False

        # Create variable to hold the shortest path
        shortestPath = []

        # While queue is not empty AND path is not Found:
        while qq.size() > 0 and not pathFound:
            # dequeue the path (list) at the head of the queue
            current_path = qq.dequeue()
            
            # If the vertex at the end of the current path has not
            # been visited then continue building the path forward
            if current_path[-1] not in visited:
                # mark as visited
                visited.add(current_path[-1])
                # enqueue all neightbors and set pathFound and shortestPath if possible
                for next_vert in self.get_neighbors(current_path[-1]):
                    new_path = list(current_path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
                    if new_path[0] == starting_vertex and new_path[-1] == destination_vertex:
                        pathFound = True
                        shortestPath = new_path

        return shortestPath



#############################################################################
# This function returns all the possible paths without going through 
# a sub-path that is included in another path.
# However this is not required according to the test, which only one path
# So therefore I choose the first element in the list to return
#############################################################################
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack and push a path (list) containing starting vertex
        ss = Stack()
        ss.push([starting_vertex])

        # Create a set of visited vertices
        ############################################################
        # The definition of a visited vertex is one whose neighbors
        # have been already entered in the stack before. The 
        # neighbors are inside a path list
        ############################################################
        visited = set()

        # Create variable to hold the different paths
        pathList = []

        while ss.size() > 0:
            # pop the path (list) at the top of the stack
            current_path = ss.pop()

            # If the vertex at the end of the current path has not
            # been visited then continue building the path forward
            if current_path[-1] not in visited:
                # mark as visited
                visited.add(current_path[-1])
                # push all neightbors and add to pathList if possible
                for next_vert in self.get_neighbors(current_path[-1]):
                    new_path = list(current_path)
                    new_path.append(next_vert)
                    ss.push(new_path)
                    if new_path[0] == starting_vertex and new_path[-1] == destination_vertex:
                        pathList.append(new_path) 

        return pathList[0]


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None, desiredPath=None, firstRun=1):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Create visited set if it does not exist

        # print(f'Begin:{firstRun}')

        if visited == None:
            visited = set()
            desiredPath = []
            return self.dfs_recursive(starting_vertex, destination_vertex, visited, path, desiredPath, firstRun)

        # Base cases
        if starting_vertex in visited:
            return None
        
        # Recursive case
        visited.add(starting_vertex)
        if path == None:
            path_copy = [starting_vertex]
        else:
            path_copy = path.copy()
            path_copy.append(starting_vertex)
        if path_copy[-1] == destination_vertex:
            desiredPath.append(path_copy)

        # print(f'path_copy={path_copy}')
        # print(f'desiredPath={desiredPath}')

        for next_vert in self.get_neighbors(starting_vertex):
            self.dfs_recursive(next_vert,destination_vertex, visited, path_copy, desiredPath, firstRun+1)

        # print(f'End:{firstRun}')

        if firstRun == 1:
            return desiredPath[0]
    

if __name__ == '__main__':
    # graph = Graph()  # Instantiate your graph
    # # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    # graph.add_vertex(1)
    # graph.add_vertex(2)
    # graph.add_vertex(3)
    # graph.add_vertex(4)
    # graph.add_vertex(5)
    # graph.add_vertex(6)
    # graph.add_vertex(7)
    # graph.add_edge(5, 3)
    # graph.add_edge(6, 3)
    # graph.add_edge(7, 1)
    # graph.add_edge(4, 7)
    # graph.add_edge(1, 2)
    # graph.add_edge(7, 6)
    # graph.add_edge(2, 4)
    # graph.add_edge(3, 5)
    # graph.add_edge(2, 3)
    # graph.add_edge(4, 6)

    # '''
    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))


    #############################################################
    # My Stuff
    graph = Graph()

    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    print(graph.vertices)


    # dump = json.dumps(graph.vertices, sort_keys=True, indent=2)

    print(f'Return of function:{graph.dfs_recursive(1,6)}')