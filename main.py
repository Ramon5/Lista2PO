from exercicios import (BasicSum, CalculateSeries, Graph, MatrixNumbers,
                        VectorRecursion)


def menu():
    while True:
        try:
            choice = int(input(
                "\n0 - Sair \n6 - Exibir matriz de adjacência e os graus dos vértices\n7 - Exibir vértices adjacentes a K \n8 - Soma recursiva\n9 - Somatório\n10 - Multiplicação de matrizes\n11 - Valor série\n\n"
            ))
            if choice == 0:
                break
            elif choice == 6:
                graph = Graph()
                matrix = graph.generate_adjacent_matrix()
                Graph.show_matrix(matrix)
                print()
                graph.vertices_level()
            elif choice == 7:
                graph = Graph()
                print(graph.adjacent_vertices())
            elif choice == 8:
                vector = [10,8,9,12,35,2]
                recursive = VectorRecursion(vector)
                print(recursive.recursive_sum(0))
            elif choice == 9:
                basic = BasicSum()
                number = int(input("Informe um número inteiro maior que 0: "))
                basic.sum_values(number)
            elif choice == 10:
                operation = MatrixNumbers()
                operation.execute()
            elif choice == 11:
                serie = CalculateSeries()
                number = int(input("Informe um número inteiro maior que 0: "))
                serie.calculate(number)
        except ValueError:
            print("Informe um número inteiro")

if __name__ == "__main__":
    menu()
