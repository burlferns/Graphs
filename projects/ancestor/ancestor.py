from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # Put the data in a vertices, edges format by using a dictionary, where
    # the child node are keys and the parent node are the sets
    relaGraph = Graph() # relaGraph is a graph of relationships

    for elem in ancestors:
        relaGraph.add_vertex(elem[0])
        relaGraph.add_vertex(elem[1])
        relaGraph.add_edge(elem[1],elem[0])

    # If the starting_node key has a set of 0 elements, then it has no
    # parents so return with -1
    if relaGraph.vertices[starting_node] == set():
        return -1

    # Do a DFT traversal and make a list of all the paths from starting_node 
    # to earliest ancestors. This will be a list of list. Lets call the 
    # outer list ancestorList.
    # We can do a DFT traversal and be sure to get all the paths and not
    # miss out because we have a tree that goes from a child node to its
    # ancestors. So since we do not have cyclical paths or more than one
    # path from one node to any other node we can be sure
    ancestorList = relaGraph.dfs(starting_node)

    # Find the length of the longest element in ancestorList. If there is
    # only one longest element, then the last member in that element is 
    # what should be returned. If there are more than one elements that are
    # the longest elements, then the last member of these elements that 
    # is the smallest should be returned  
    maxLength = 0
    elemIndex_maxLength = [] # List of elements in ancestorList with most
                             # elements. This is a list of indexes
    for index, elem in enumerate(ancestorList): # Find the max length elem
        if  len(elem) > maxLength:
            maxLength = len(elem)
            elemIndex_maxLength = [index]
        elif len(elem) == maxLength:
            elemIndex_maxLength.append(index)
    minValue = ancestorList[elemIndex_maxLength[0]][-1]
    # Find the min Integer in each max length elem
    for i in range(1,len(elemIndex_maxLength)):              
        if ancestorList[elemIndex_maxLength[i]][-1] < minValue:
            minValue = ancestorList[elemIndex_maxLength[i]][-1]

    return minValue

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 6))