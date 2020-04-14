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
        # Only add vertex if not already there
        if  vertex_id not in self.vertices:
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
# This function returns all the possible paths without going through 
# a sub-path that is included in another path.
# It starts at the starting_vertex and goes forward till it reaches a
# node with no neighbors and then it stops and put that path in a list 
# called pathList
#############################################################################
    def dfs(self, starting_vertex):
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
            # if possible
            if current_path[-1] not in visited:
                # mark as visited
                visited.add(current_path[-1])
                
                if self.vertices[current_path[-1]] == set():
                    # if there are no more neighbors then add the 
                    # current path to pathList
                    pathList.append(current_path)
                else:
                    # else continue exploring forward
                    # push all neightbors
                    for next_vert in self.get_neighbors(current_path[-1]):
                        new_path = list(current_path)
                        new_path.append(next_vert)
                        ss.push(new_path)

        return pathList


       

# if __name__ == '__main__':
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
    # graph = Graph()

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

    # print(graph.vertices)


    # # dump = json.dumps(graph.vertices, sort_keys=True, indent=2)

    # print(f'Return of function:{graph.dfs_recursive(1,6)}')