import random


class Vertice:
    """
        This vertice representation
    """

    def __init__(self, label):
        self._label = label
        self._edges = []

    @property
    def label(self):
        return self._label

    @property
    def get_edges(self):
        return self._edges

    def add_edges(self, edges):
        self._edges.extend(edges)

    def __repr__(self):
        return str(self.label)


class Edge:
    """
        This edge representation
    """

    def __init__(self, weight: int):
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    def __repr__(self):
        return str(self.weight)


class Graph:
    """
        This graph representation
    """

    def __init__(self):
        self._graph = self._connect_vertices_and_edges()

    def _get_objects(self):
        """
            Read file and get values to vertices and edges
        """
        reading_vertices = True
        edges = []
        vertices = []
        with open("graph.txt") as source:
            for line in source:
                data = line.split(" ")
                if len(data) == 1:
                    reading_vertices = False
                    continue
                if reading_vertices:
                    vertices = list(map(int, data))
                else:
                    edges = list(map(int, data))

        return vertices, edges

    def _build_vertices_and_edges(self):
        """
            Create objects Vertices and Edges from values
        """
        data_vertices, data_edges = self._get_objects()
        vertices = [Vertice(label) for label in data_vertices]
        edges = [Edge(int(weight)) for weight in data_edges]

        return vertices, edges

    def _search_edges(self, values: list, collection: list) -> list:
        """
            Search the edges that will connect to vertice
        """
        edges = []
        for edge in collection:
            if edge.weight in values:
                edges.append(edge)
        return edges

    def _connect_vertices_and_edges(self):
        """
            Build graph connecting edges to vertices
        """
        vertices, edges = self._build_vertices_and_edges()

        vertices[0].add_edges(self._search_edges([2, 5, 15], edges))
        vertices[1].add_edges(self._search_edges([4, 5, 9, 22], edges))
        vertices[2].add_edges(self._search_edges([1, 12], edges))
        vertices[3].add_edges(self._search_edges([6, 9, 12], edges))
        vertices[4].add_edges(self._search_edges([1, 15, 22], edges))
        vertices[5].add_edges(self._search_edges([2, 4, 6], edges))

        return vertices

    def vertices_level(self):
        for vertice in self._graph:
            print(f"vertice: {vertice.label} -> grau: {len(vertice.get_edges)}")

    def generate_adjacent_matrix(self) -> list:
        matrix = []
        for v1 in self._graph:
            lines = []
            for v2 in self._graph:
                if v1 != v2:
                    lines.append(self._is_adjacent(v1, v2))
            matrix.append(lines)

        return matrix

    def _is_adjacent(self, v1: Vertice, v2: Vertice) -> int:
        for i in v1.get_edges:
            for j in v2.get_edges:
                if i.weight == j.weight:
                    return 1
        return 0

    def adjacent_vertices(self):
        print(f"Grafo: {self._graph}")
        number = input("Escolha um vértice: ")
        vertice = self._graph[int(number)]
        edges = [entry.weight for entry in vertice.get_edges]
        adjacents = []
        for v in self._graph:
            if v != vertice:
                for e in v.get_edges:
                    for f in edges:
                        if e.weight == f:
                            adjacents.append(v)
                            break

        return adjacents

    @classmethod
    def show_matrix(cls, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(f"{matrix[i][j]}\t", end="")
            print()


class VectorRecursion:
    def __init__(self, vector):
        self.vector = vector

    def recursive_sum(self, i):
        if i == len(self.vector):
            return 0

        return self.vector[i] + self.recursive_sum(i + 1)


class BasicSum:
    def sum_values(self, n):
        value = 0
        for i in range(1, n + 1):
            value += i * (i + 1)

        return value


class MatrixNumbers:
    """
        This class provide a read numbers and storage in matrix
    """

    def __init__(self):
        self._lines = 10
        self._columns = 10
        self._matrixA = self._generate_matrix()
        self._matrixB = self._generate_matrix()

    def _generate_matrix(self) -> list:
        matrix = []
        for i in range(self._lines):
            column = []
            for j in range(self._columns):
                number = random.randint(0, 50)
                column.append(int(number))
            matrix.append(column)

        return matrix

    def _product_matrix(self):
        matrix = []
        for i in range(self._lines):
            line = []
            for j in range(self._columns):
                sum_value = self._matrixA[i][j] * self._matrixB[i][j]
                line.append(sum_value)
            matrix.append(line)

        return matrix

    def _show(self):
        matrix = self._product_matrix()
        print("\nMatriz Resultante\n")
        for i in range(self._lines):
            for j in range(self._columns):
                print(f"{matrix[i][j]} \t", end="")
            print("\n")

    def execute(self):
        self._generate_matrix()
        self._show()


class CalculateSeries:
    def calculate(self, n):
        value = 0
        for i in range(1, n + 1):
            value += 2 * i - 1 / (-2) ** (i + 1)

        return value
