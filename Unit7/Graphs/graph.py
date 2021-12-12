"""
graph.py
Contains the Graph ADT and small test driver function
"""


class Graph:
    """
    Graph ADT. Contains Verticies that point to other Verticies

    Attributes:
    -----------

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
        try:
            source = self.verticies[src]
            destination = self.verticies[dest]
            source.add_neighbor(destination, w)
        except KeyError:
            raise ValueError("src || dest || w not valid!")


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
