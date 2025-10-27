class Graph:
    def __init__(self, num_vertices, is_directed=False):
        """
        Cria uma nova instância do grafo
        :param num_vertices: quantidade total de vértices
        :param is_directed: indica se o grafo é direcionado (default=False)
        """
        self.vertices = num_vertices
        self.directed = is_directed
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v):
        """
        Adiciona uma aresta entre os vértices u e v
        :param u: vértice de origem
        :param v: vértice de destino
        """
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = 1
            self.adj_list[u].append(v)
            if not self.directed:
                self.adj_matrix[v][u] = 1
                self.adj_list[v].append(u)
    
    def hamiltonian_path(self):
        """
        Encontra um caminho hamiltoniano no grafo
        :return: lista com a ordem dos vértices no caminho ou None se não existir
        """
        path = []
        
        # Função auxiliar para verificar se o vértice pode ser adicionado ao caminho
        def pode_adicionar_vertice(v, posicao, caminho_atual):
            # Verifica se existe uma aresta entre o vértice atual e o anterior
            if self.adj_matrix[caminho_atual[posicao-1]][v] == 0:
                return False
            
            # Verifica se o vértice ainda não foi visitado
            if v in caminho_atual:
                return False
                
            return True
        
        # Função recursiva para encontrar o caminho
        def hamiltonian_path_util(path):
            # Caso base: todos os vértices estão no caminho
            if len(path) == self.vertices:
                return True
                
            # Tenta adicionar cada vértice ao caminho atual
            for v in range(self.vertices):
                if pode_adicionar_vertice(v, len(path), path):
                    path.append(v)
                    
                    if hamiltonian_path_util(path):
                        return True
                        
                    # Backtracking
                    path.pop()
            
            return False
        
        # Tenta iniciar o caminho de cada vértice
        for start_vertex in range(self.vertices):
            path = [start_vertex]
            
            if hamiltonian_path_util(path):
                return path
                
        return None
    
    def print_hamiltonian_path(self):
        """
        Imprime um caminho hamiltoniano se existir
        """
        path = self.hamiltonian_path()
        
        if path:
            print("Caminho Hamiltoniano encontrado:")
            print(" -> ".join(map(str, path)))
        else:
            print("Nenhum Caminho Hamiltoniano encontrado no grafo.")


# Cria uma nova instância do grafo baseada na entrada do usuário
def ler_grafo_do_usuario():
    print("Criando um grafo:")
    eh_direcionado = input("O grafo é orientado? (s/n): ").lower() == 's'
    quantidade_vertices = int(input("Número de vértices: "))
    
    graph = Graph(quantidade_vertices, eh_direcionado)
    
    print("Digite as arestas (formato: origem destino)")
    print("Digite 'fim' para terminar)")
    
    while True:
        edge = input("Aresta: ").strip()
        if edge.lower() == 'fim':
            break
        
        try:
            u, v = map(int, edge.split())
            graph.add_edge(u, v)
        except ValueError:
            print("Formato inválido. Use: origem destino (Ex: 0 1)")
    
    return graph


# Menu interativo
def main_menu():
    print("\nMenu:")
    print("1. Criar grafo manualmente")
    print("2. Usar grafo de exemplo (não orientado)")
    print("3. Usar grafo de exemplo (orientado)")
    print("4. Sair")
    
    choice = input("Escolha uma opção: ")
    return choice


# Exemplos pré-definidos de grafos
def criar_grafo_exemplo_nao_direcionado():
    """Cria um grafo não direcionado que possui um caminho hamiltoniano"""
    grafo = Graph(5, is_directed=False)
    grafo.add_edge(0, 1)
    grafo.add_edge(0, 3)
    grafo.add_edge(1, 2)
    grafo.add_edge(1, 3)
    grafo.add_edge(1, 4)
    grafo.add_edge(2, 4)
    grafo.add_edge(3, 4)
    return grafo

def criar_grafo_exemplo_direcionado():
    """Cria um grafo direcionado que possui um caminho hamiltoniano"""
    grafo = Graph(5, is_directed=True)
    grafo.add_edge(0, 1)
    grafo.add_edge(1, 2)
    grafo.add_edge(2, 3)
    grafo.add_edge(3, 4)
    grafo.add_edge(1, 4)
    grafo.add_edge(1, 3)
    return grafo


# Programa principal
if __name__ == "__main__":
    print("Implementação do Algoritmo para Caminho Hamiltoniano")
    
    graph = None
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            graph = ler_grafo_do_usuario()
            graph.print_hamiltonian_path()
        elif choice == '2':
            graph = criar_grafo_exemplo_nao_direcionado()
            print("\nGrafo de exemplo não orientado criado:")
            graph.print_hamiltonian_path()
        elif choice == '3':
            graph = criar_grafo_exemplo_direcionado()
            print("\nGrafo de exemplo orientado criado:")
            graph.print_hamiltonian_path()
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")