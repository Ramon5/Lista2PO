import random


class ChallengeOne:
    def __init__(self):
        self.matrix = [[4, 1, 2, 3], [5, 2, 1, 400], [2, 1, 3, 8], [7, 1, 2, 5]]

    def calculate(self):
        itinerary = int(input("Digite a quantidade de itinerários: "))
        city = int(input("Informe a quantidade de cidades: "))

        itineraries = []
        for i in range(itinerary):
            cities = []
            print(f"\nItinerário {i+1} ")
            for j in range(1, int(city) + 1):
                entry = input(f"Informe a {j}ª cidade: ")
                cities.append(int(entry))
            itineraries.append(cities)

        result = []
        for itinerary in itineraries:
            data = {}
            value = 0
            for index, obj in enumerate(itinerary):
                if index + 1 < len(itinerary):
                    value += self.matrix[obj][itinerary[index + 1]]

            data["itinerario"] = itinerary
            data["custo"] = value
            result.append(data)

        return result


class Vertice:
    def __init__(self, label):
        self._label = label
        self._visited = False
        self._exit_route = []
        self._entry_route = []

    @property
    def is_visited(self):
        return self._visited

    def mark_as_visited(self):
        self._visited = True

    @property
    def exit_route(self):
        return self._exit_route

    @exit_route.setter
    def exit_route(self, exit_route):
        self._exit_route.append(exit_route)

    @property
    def entry_route(self):
        return self._entry_route

    @entry_route.setter
    def entry_route(self, entry_route):
        self._entry_route.append(entry_route)

    @property
    def label(self):
        return self._label

    def is_possible(self, vertice):
        if int(vertice.label) in self.exit_route:
            return True
        return False

    def __repr__(self):
        return self.label


class ChallengeTwo:
    def __init__(self, length):
        self._length = length
        self._graph = []
        self._matrix = []
        self._build_graph()
        self._generate_adjacent_matrix()
        self._define_routes()

    def _build_graph(self):
        """ Create graph """
        for i in range(self._length):
            self._graph.append(Vertice(str(i)))

    def _generate_adjacent_matrix(self):
        for i in range(self._length):
            line = []
            for j in range(self._length):
                line.append(random.randint(0, 1))
            self._matrix.append(line)

    def _define_routes(self):
        """ define entry and exit roads to vertices"""
        for vertice in self._graph:
            self._entry_roads(vertice)
            self._exit_roads(vertice)

    def _exit_roads(self, vertice: Vertice):
        """ get exit roads of the vertice"""
        index = int(vertice.label)
        entries = self._matrix[index]

        for i, entry in enumerate(entries):
            if index != i:
                if entry == 1:
                    vertice.exit_route.append(i)

    def _entry_roads(self, vertice: Vertice):
        """ get entry roads of the vertice"""
        v = int(vertice.label)
        for i in range(self._length):
            if i != v:
                if self._matrix[i][v] == 1:
                    vertice.entry_route.append(i)

    def _search_vertice(self, number: int) -> Vertice:
        """ Get vertice by number"""
        for v in self._graph:
            if int(v.label) == number:
                return v
        return None

    # A)
    def get_roads(self):
        """ Retrieve entry and exit roads by city"""
        number = int(input("Informe uma cidade: "))
        vertice = self._search_vertice(number)
        if vertice:
            print(
                f"Estradas que saem: {len(vertice.exit_route)} - Estradas que entram: {len(vertice.entry_route)}"
            )

    # B)
    def get_city_max_entries(self):
        """ Get city with max entry roads"""
        maximum = 0
        city = None
        for v in self._graph:
            if len(v.entry_route) > maximum:
                maximum = len(v.entry_route)
                city = v
        return city

    # C)
    def exists_double_road(self):
        """ Verify if exists double roads on city"""
        number = int(input("Informe a cidade: "))
        vertice = self._search_vertice(number)
        if vertice:
            exits = vertice.exit_route
            entries = vertice.entry_route
            return exits == entries

        return False

    # D)
    def get_directly_exit_routes(self):
        number = int(input("Informe a cidade: "))
        vertice = self._search_vertice(number)
        if vertice:
            return vertice.entry_route

        return None

    # E)
    def general_information(self):
        data = {
            "isolated_cities": len(
                list(filter(lambda city: len(city.entry_route) == 0, self._graph))
            ),
            "cities_only_entries": len(
                list(
                    filter(
                        lambda city: len(city.entry_route) > 0
                        and len(city.exit_route) == 0,
                        self._graph,
                    )
                )
            ),
            "cities_only_exits": len(
                list(
                    filter(
                        lambda city: len(city.entry_route) == 0
                        and len(city.exit_route) > 0,
                        self._graph,
                    )
                )
            ),
        }
        return data

    # F)
    def execute_itinerary(self):
        number = int(input("Informe a quantidade de rotas: "))
        routes = []
        for i in range(number):
            city = int(input(f"Digite a {i+1}ª cidade: "))
            routes.append(self._search_vertice(city))

        for index, _ in enumerate(routes, 1):
            if index < len(routes):
                if not routes[index - 1].is_possible(routes[index]):
                    return False

        return True

    # G)
    def trace_route(self):
        source = int(input("Informe a cidade origem: "))
        target = int(input("Informe a cidade destino: "))

        cityA = self._search_vertice(source)
        cityB = self._search_vertice(target)

        if int(cityB.label) in cityA.exit_route:
            return True
        else:
            for index in cityA.exit_route:
                city = self._search_vertice(index)

                if int(cityB.label) in city.exit_route:
                    return True

        return False

    # H)
    def return_to_city(self):
        source = int(input("Informe a cidade origem: "))
        city = self._search_vertice(source)

        return self._is_hamiltonian(self._graph, city)

    def _is_hamiltonian(self, graph, source):
        if len(graph) > 2:
            vertice = source
            non_adjacents = []
            for v in graph:
                if (
                    not int(vertice.label) in v.exit_route
                    and not int(vertice.label) in v.entry_route
                ):
                    non_adjacents.append(v)
                    vertice = v

            sum_level = 0

            for v in non_adjacents:
                sum_level += len(v.exit_route)

            if sum_level >= len(graph):
                return True

        return False
