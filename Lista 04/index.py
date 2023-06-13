from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def print_graph(self):
        for row in self.graph:
            print(' '.join([str(i) for i in row]))

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        if vertex < self.num_vertices:
            for neighbor in range(self.num_vertices):
                if neighbor != vertex and self.graph[vertex][neighbor] != 0 and neighbor not in visited:
                    self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque()

        visited.add(start_vertex)
        queue.append(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            if vertex < self.num_vertices:
                for neighbor in range(self.num_vertices):
                    if neighbor != vertex and self.graph[vertex][neighbor] != 0 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)


def read_graph_from_file(file_name):
    with open(file_name, 'r') as file:
        num_vertices = int(file.readline())
        g = Graph(num_vertices)
        for i in range(num_vertices):
            values = file.readline().split()
            for j in range(num_vertices):
                if i != j and values[j] != '0':
                    g.add_edge(i, j)
        return g


def show_instance_menu():
    print("Selecione uma instância de grafo:")
    print("1. pcv4.txt")
    print("2. pcv10.txt")
    print("3. pcv50.txt")
    print("4. pcv177.txt")
    print("0. Voltar ao menu principal")


def show_menu():
    print("Selecione uma opção:")
    print("1. Adicionar aresta")
    print("2. Imprimir o grafo")
    print("3. Busca em Profundidade (DFS)")
    print("4. Busca em Largura (BFS)")
    print("0. Sair")


g = None

while True:
    show_instance_menu()
    instance_choice = input("Digite o número da instância de grafo desejada: ")

    if instance_choice == "1":
        g = read_graph_from_file("instncias_grafo/pcv4.txt")
        print("Grafo carregado: pcv4.txt")
        break
    elif instance_choice == "2":
        g = read_graph_from_file("instncias_grafo/pcv10.txt")
        print("Grafo carregado: pcv10.txt")
        break
    elif instance_choice == "3":
        g = read_graph_from_file("instncias_grafo/pcv50.txt")
        print("Grafo carregado: pcv50.txt")
        break
    elif instance_choice == "4":
        g = read_graph_from_file("instncias_grafo/pcv177.txt")
        print("Grafo carregado: pcv177.txt")
        break
    elif instance_choice == "0":
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

if g is not None:
    while True:
        show_menu()
        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            u = int(input("Digite o vértice de origem: "))
            v = int(input("Digite o vértice de destino: "))
            g.add_edge(u, v)
        elif choice == "2":
            print("Grafo:")
            g.print_graph()
        elif choice == "3":
            start_vertex = int(input("Digite o vértice inicial para a busca em profundidade (DFS): "))
            print("Busca em Profundidade (DFS):")
            g.dfs(start_vertex)
            print()
        elif choice == "4":
            start_vertex = int(input("Digite o vértice inicial para a busca em largura (BFS): "))
            print("Busca em Largura (BFS):")
            g.bfs(start_vertex)
            print()
        elif choice == "0":
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")
