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
        self.vertices[vertex_id] = set()  #

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:  # I add edge from v1 to v2. However, I first check if they are both in the graph
            self.vertices[v1].add(v2)  # add v2 to v1 set of edges
        else:
            raise IndexError("Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]  # Return the whole set

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex
        bft_queue = Queue()
        bft_queue.enqueue(starting_vertex)
        # Create a set where the visited vertices are kept
        visited = set()
        # If there is something on the queue, we want to check each vertex and add it to visited set
        while bft_queue.size() > 0:
            # remove the first item from the queue
            queue_item = bft_queue.dequeue()
            # I check if queue_item is part of the visited set
            if queue_item not in visited:
                # Add it to the visited
                print(queue_item)
                visited.add(queue_item)
                for next_visited in self.get_neighbors(queue_item):
                    # add all its neighbors to the queue
                    bft_queue.enqueue(next_visited)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex
        dft_stack = Stack()
        dft_stack.push(starting_vertex)
        # Create a set where the visited vertices are kept
        visited = set()
        # If there is something on the stack, we want to check each vertex and add it to visited set
        while dft_stack.size() > 0:
            # remove the first item from the stack
            stack_item = dft_stack.pop()
            # I check if stack_item is part of the visited set
            if stack_item not in visited:
                # Add it to the visited
                print(stack_item)
                visited.add(stack_item)
                for next_visited in self.get_neighbors(stack_item):
                    dft_stack.push(next_visited)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for vert in self.vertices[starting_vertex]:
            if vert not in visited:
                self.dft_recursive(vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        bfs_search = Queue()
        bfs_search.enqueue([starting_vertex])
        # Create a set
        visited = set()
        while bfs_search.size() > 0:
            # remove the first item from the queue
            bfs_item = bfs_search.dequeue()
            v = bfs_item[-1]
            if v not in visited:
                if v == destination_vertex:
                    return bfs_item
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    new_path = list(bfs_item)
                    new_path.append(next_vert)
                    bfs_search.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        dfs_search = Stack()
        dfs_search.push([starting_vertex])
        # Create a set
        visited = set()
        while dfs_search.size() > 0:
            # remove the first item from the stack
            dfs_item = dfs_search.pop()
            v = dfs_item[-1]
            if v not in visited:
                if v == destination_vertex:
                    return dfs_item
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    new_path = list(dfs_item)
                    new_path.append(next_vert)
                    dfs_search.push(new_path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()  # Create a set
        if path is None:
            path = []  # Create a list
        # Include the first vertex to the visited set
        visited.add(starting_vertex)
        # Concatenate the path of the starting vertex to the current path
        path = path + [starting_vertex]
        # Check to see if the starting vertex is the destination_vertex
        if starting_vertex == destination_vertex:
            return path
        for child_vertex in self.get_neighbors(starting_vertex):
            if child_vertex not in visited:
                new_path = self.dfs_recursive(
                    child_vertex, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
