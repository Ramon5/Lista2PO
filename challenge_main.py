from challenge import ChallengeOne, ChallengeTwo


class Execution:
    def __init__(self):
        self.graph = None

    def menu(self):
        while True:
            try:
                choice = int(
                    input(
                        "\n0 - Sair \n1 - Calcular custo de itinerário\n2 - Gerar grafo\n3 - Estradas de uma cidade (Entrada e Saída)\n4 - Cidade com maior nº de entradas\n5 - Verificar se todas as ligações são de mão dupla\n6 - Saídas diretas\n7 - Informações Gerais\n8 - Verificar roteiros\n9 - Caminho possível\n10 - Verificar se grafo é Hamilthoniano\n\n"
                    )
                )
                if choice == 0:
                    break
                elif choice == 1:
                    challenge = ChallengeOne()
                    for index, obj in enumerate(challenge.calculate()):
                        print(f"\nCusto do itinerário {index+1}: {obj['custo']}")
                elif choice == 2:
                    number = int(input("Informe o tamanho do grafo a ser gerado: "))
                    self.graph = ChallengeTwo(number)
                elif choice == 3:
                    if self.graph:
                        self.graph.get_roads()
                elif choice == 4:
                    if self.graph:
                        print(
                            f"\nCidade com maior número de entradas: {self.graph.get_city_max_entries()}"
                        )
                elif choice == 5:
                    if self.graph:
                        if self.graph.exists_double_road():
                            print("\nAs ligações são de mão dupla")
                        else:
                            print("\nAs ligações não são de mão dupla")
                elif choice == 6:
                    if self.graph:
                        exits = self.graph.get_directly_exit_routes()
                        if exits:
                            print(f"\nSaídas diretas: {exits}")
                elif choice == 7:
                    if self.graph:
                        data = self.graph.general_information()
                        print(f"Cidades Isoladas: {data['isolated_cities']}")
                        print(
                            f"Cidades que possuem somente entradas: {data['cities_only_entries']}"
                        )
                        print(
                            f"Cidade que possuem somente saídas: {data['cities_only_exits']}"
                        )
                elif choice == 8:
                    if self.graph:
                        if self.graph.execute_itinerary():
                            print("\nO roteiro é possível")
                        else:
                            print("\nO roteiro é impossível")
                elif choice == 9:
                    if self.graph:
                        if self.graph.trace_route():
                            print("\nExiste caminho possível")
                        else:
                            print("\nNão é possível chegar ao destino")
                elif choice == 10:
                    if self.graph:
                        if self.graph.return_to_city():
                            print("\nÉ possível")
                        else:
                            print("\nNão é possível")

            except ValueError:
                print("\nInforme um número inteiro")


if __name__ == "__main__":
    exercise = Execution()
    exercise.menu()