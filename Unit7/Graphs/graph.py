"""
graph.py
Contains the Graph ADT and small test driver function
"""
import math
from typing import Generator

import pytest


class Graph:
    """
    Graph ADT. Contains Verticies that point to other Verticies

    Attributes:
    -----------
    vertex_num: (int): The number of verticies in the graph

    Methods:
    --------
    add_vertex(label): Adds a vertex with given label
    add_edge(src, dest, w): Adds a edge between two Vertex
    get_weight(src, dest): Return the weight of a given edge
    dfs(starting_vertex): Returns a genorator for Depth-first traversal
    bfs(starting_vertex): Returns a generator for breadth-first traversal
    dsp(src, dest): Return (lenght, List<Vertex>). The path between two Vertex
    dsp_all(src): Return the path from source to ALL Vertex
    """

    def __init__(self):
        """
        Constructor for Graph ADT
        """
        self.verticies = {}
        self.vertex_num = 0

    def add_vertex(self, label):
        """
        Adds a vertex

        Paramaters:
        -----------
        label : str
            The label of the new Vertex

        :return: self
        """
        if not isinstance(label, str):
            raise ValueError("Label for new vertex must be string!")

        self.vertex_num += 1
        self.verticies[label] = Vertex(label)

        return self

    def add_edge(self, src, dest, w):
        """
        Adds an edge between source Vertex and destination Vertex

        Paramaters:
        -----------
        src : str
            The source Vertex label
        dest : str
            The destination Vertex label
        w : float
            The weight of the edge
        """
        if not isinstance(w, float) and not isinstance(w, int):
            raise ValueError("Edge weight must be float")

        try:
            source = self.verticies[src]
            destination = self.verticies[dest]
            source.add_neighbor(destination, float(w))
        except KeyError:
            raise ValueError("src || dest not valid!")

        return self

    def get_weight(self, src, dest):
        """
        Returns the weight of an edge between source and destination

        Paramaters:
        -----------
        src : Vertex
            The source Vertex
        dest: Vertex
            The destination Vertex

        :return: float: The weight of the edge
        """
        src_vertex = self.verticies[src]
        dest_vertex = self.verticies[dest]
        return src_vertex.get_weight(dest_vertex)

    def bfs(self, starting_vertex):
        """
        Returns a generator for bredth-first traversal of the graph

        Paramaters:
        -----------
        starting_vertex : str
            The label of the starting vertex

        Returns:
        --------
        (Generator) : A generator for the traversal
        """
        # The list of verticies that have been visited before
        visited_verticies = []
        # The current level of verticies
        current_verticies = [self.verticies[starting_vertex]]

        # While there are still verticies to traverse
        while len(current_verticies):
            temp_list = []  # Temporary list used for storing verticies
            # For each vertex in the current level
            for vertex in current_verticies:
                # Add each neighbor of the vertex to the temp_list
                for neighbor in vertex.neighbors.keys():
                    # If the neighbor vertex has already been visited, pass over it
                    if neighbor not in visited_verticies:
                        temp_list.append(neighbor)

                # Mark the current vertex as visited
                visited_verticies.append(vertex)
                # Yield the current vertex
                yield vertex
            # Set the current level of verticies to the temp list
            current_verticies = temp_list

    def dfs(self, starting_vertex):
        """
        Returns a generator for traversing the graph in depth-first traversal

        Paramaters:
        -----------
        starting_vertex : str
            The label of the starting vertex

        Returns:
        --------
        (Generator) : A generator for the traversal
        """
        visited = []
        current_vertex = self.verticies[starting_vertex]
        vertex_stack = [current_vertex]

        while len(vertex_stack):
            # Pop the top vertex off the stack and return it
            current_vertex = vertex_stack.pop()
            visited.append(current_vertex)
            yield current_vertex

            # Push the current vertex's neighbors that have not been visited onto the stack
            neighbors = [v for v in current_vertex.neighbors.keys()
                         if v not in visited]
            for neighbor in neighbors:
                vertex_stack.append(neighbor)

    def dsp(self, src, dest):
        """

        """
        pass

    def __str__(self):
        output = 'digraph G {\n'
        for vertex in self.verticies.values():
            for neighbor in vertex.neighbors.keys():
                v_label = vertex.label
                n_label = neighbor.label
                weight = vertex.neighbors[neighbor]
                output += f"   {v_label} -> {n_label} [label=\"{weight}\",weight=\"{weight}\"];\n"

        output += "}\n"
        return output


class Vertex:
    """
    Node ADT. Contains data and points to other Nodes as part of the
    Graph ADT.

    Attributes:
    -----------
    label: (str) The label of the Vertex
    neighbors: (Dict<Vertex: float>) HashMap of Vertex's neighbors and edge weight
    neighbors_num: (int) The number of neighbors

    Methods:
    --------
    add_neighbor(vertex): Adds a pointer to another vertex
    get_weight(neighbor): Returns the weight of the edge pointing to neighbor
    """

    def __init__(self, label):
        """
        Constructor for Vertex ADT
        """
        self.label = label
        self.neighbors = {}
        self.neighbors_num = 0

    def add_neighbor(self, vertex, w):
        """
        Adds a pointer to another vertex

        Paramaters:
        -----------
        vertex : Vertex
            The vertex being pointed too
        w : float
            The weight of the connection
        """
        try:
            self.neighbors[vertex]
        except KeyError:
            self.neighbors[vertex] = w
            self.neighbors_num += 1

    def get_weight(self, neighbor):
        """
        Returns the weight of an edge to a neighbor

        Paramaters:
        -----------
        neighbor : Vertex
            The neighbor

        :return: float: The weight of the edge
        """
        try:
            return self.neighbors[neighbor]
        except KeyError:
            return math.inf

    def __str__(self):
        """
        String form of Vertex
        """
        return self.label

    def __repr__(self):
        """
        Representation of Vertex
        """
        return self.label

    def __eq__(self, other):
        """
        Overload of the equals operator.
        Compare to self.label

        Paramaters:
        -----------
        other : str || Vertex
        """
        if isinstance(other, Vertex):
            return self.label == other.label
        elif isinstance(other, str):
            return self.label == other
        else:
            raise ValueError(
                "Can only compare equality of Vertex to Vertex or String")

    def __hash__(self):
        """
        Overload of the builtin hash method
        """
        return hash(self.label)


def main():
    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')

    graph.add_edge('A', 'B', 1.0)
    graph.add_edge('B', 'D', 1.0)
    graph.add_edge('A', 'C', 1.0)
    graph.add_edge('C', 'E', 1.0)
    graph.add_edge('E', 'F', 1.0)

    print(graph)

    print("#"*44 + "\n")

    for vertex in graph.dfs("A"):
        print(vertex)


def pytest_finangling():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 1.0)
    g.add_edge("A", "C", 1.0)

    g.add_edge("B", "D", 1.0)

    g.add_edge("C", "E", 1.0)

    g.add_edge("E", "F", 1.0)

    expected = '''digraph G {
   A -> B [label="1.0",weight="1.0"];
   A -> C [label="1.0",weight="1.0"];
   B -> D [label="1.0",weight="1.0"];
   C -> E [label="1.0",weight="1.0"];
   E -> F [label="1.0",weight="1.0"];
}
'''
    output = str(g)
    # assert output == expected
    print(expected)
    print(output)
    print(expected == output)


if __name__ == "__main__":
    main()
