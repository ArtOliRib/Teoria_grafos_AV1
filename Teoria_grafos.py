import sys

class Grafo:
    def __init__(self):
        self.vertices = 0
        self.matriz = []
        self.lista = {}

    def ler_grafo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            self.vertices = int(arquivo.readline())
            self.matriz = [list(map(int, linha.split())) for linha in arquivo]

    def gerar_listaacencias(self):
        for i in range(self.vertices):
            vizinhos = [j for j in range(self.vertices) if self.matriz[i][j] == 1]
            self.lista[i] = vizinhos

    def imprimir_matrizacencias(self):
        for linha in self.matriz:
            print(' '.join(map(str, linha)))

    def imprimir_listaacencias(self):
        for vertice, vizinhos in self.lista.items():
            print(f'{vertice}: {", ".join(map(str, vizinhos))}')

    def calcular_graus(self):
        graus = [len(vizinhos) for vizinhos in self.lista.values()]
        grau_minimo = min(graus)
        grau_maximo = max(graus)
        return grau_minimo, grau_maximo
    
    def determinar_sequencia_de_graus(self):
        graus = [len(vizinhos) for vizinhos in self.lista.values()]
        graus.sort()
        return graus
    
    def determinar_vizinhanca(self, vertice):
        vizinhos = self.lista[vertice]
        vizinhanca_aberta = set(vizinhos)
        vizinhanca_fechada = set(v for v in self.lista.keys() if v != vertice and v not in vizinhos)
        grau = len(vizinhos)
        return grau, vizinhanca_aberta, vizinhanca_fechada
    
    def sao_vizinhos(self, u, v):
        return u in self.lista[v] and v in self.lista[u]

    def verificar_regularidade(self):
        graus = [len(vizinhos) for vizinhos in self.lista.values()]
        grau = graus[0]
        if all(grau == g for g in graus):
            return True, grau
        else:
            return False, None

    def verificar_completude(self):
        num_arestas = sum(len(vizinhos) for vizinhos in self.lista.values()) // 2
        num_max_arestas = self.vertices * (self.vertices - 1) // 2
        if num_arestas == num_max_arestas:
            print("O grafo é completo.")
        else:
            print("O grafo não é completo.")
        return 

    def encontrar_vertices_universais(self):
        vertices_universais = []
        for vertice in self.lista:
            vizinhos = set(self.lista[vertice])
            if len(vizinhos) == self.vertices - 1 and vertice not in vizinhos:
                vertices_universais.append(vertice)

        if vertices_universais:
            print("Vértices universais encontrados:")
            print(vertices_universais)
        else:
            print("Não há vértices universais no grafo.")
        return
    
    def encontrar_vertices_isolados(self):
        vertices_isolados = []
        for vertice in self.lista:
            if len(self.lista[vertice]) == 0:
                vertices_isolados.append(vertice)

        if vertices_isolados:
            print("Vértices isolados encontrados:")
            print(vertices_isolados)
        else:
            print("Não há vértices isolados no grafo.")
        return
    
    def verificar_subgrafo(self, vertices_H, arestas_H):
        vertices_H = set(vertices_H)
        arestas_H = set(arestas_H)

        if not vertices_H.issubset(self.conjunto_vertices):
            return False
        
        for aresta in arestas_H:
            if not aresta in self.conjunto_arestas:
                return False
            if not all(v in vertices_H for v in aresta):
                return False

        return True
    
    def subgrafo(self,vertices, arestas, subvertices, subarestas):
    
        if set(subvertices).issubset(set(vertices)) and set(subarestas).issubset(set(arestas)):
            for edge in subarestas:
                if edge[0] not in subvertices or edge[1] not in subvertices:
                    return False
        return True
        

    def verificar_passeio(self, sequencia):
        sequencia_bool = True
        for i in range(len(sequencia) - 1):
            if sequencia[i+1] not in self.lista[sequencia[i]]:
                sequencia_bool = False
        if sequencia_bool:
            print("A sequência é um passeio no grafo.")
        else:
            print("A sequência não é um passeio no grafo.")
        return 
    
    def verificar_caminho(self, sequencia):
        caminho_bool = True
        if len(set(sequencia)) != len(sequencia):
            caminho_bool = False # Verifica se há vértices repetidos

        for i in range(len(sequencia) - 1):
            if sequencia[i+1] not in self.lista[sequencia[i]]:
                caminho_bool = False  # Verifica se há uma aresta entre os vértices consecutivos
            
        if caminho_bool:
            print("A sequência é um caminho no grafo.")
        else:
            print("A sequência não é um caminho no grafo.")

        return

    def verificar_ciclo(self, sequencia):
        ciclo_bool = True
        if len(sequencia) < 3 or sequencia[0] != sequencia[-1]:
            ciclo_bool = False  

        if len(set(sequencia)) != len(sequencia) - 1:
            ciclo_bool = False 

        for i in range(len(sequencia) - 1):
            if sequencia[i+1] not in self.lista[sequencia[i]]:
                ciclo_bool = False
            
        if ciclo_bool:
            print("A sequência é um ciclo no grafo.")
        else:
            print("A sequência não é um ciclo no grafo.")  

        return

    def verificar_trilha(self, sequencia):
        trilha_bool = True

        if len(set(sequencia)) != len(sequencia):
            trilha_bool = False  

        arestas_visitadas = set()
        for i in range(len(sequencia) - 1):
            aresta = (sequencia[i], sequencia[i+1])
            if aresta in arestas_visitadas:
                trilha_bool = False  
            if sequencia[i+1] not in self.lista[sequencia[i]]:
                trilha_bool = False  
            arestas_visitadas.add(aresta)

        if trilha_bool:
            print("A sequência é uma trilha no grafo.")
        else:
            print("A sequência não é uma trilha no grafo.")

        return
    
    
    def verificar_clique(self, lista, conjunto_vertices):
        clique_bool = True

        for i in conjunto_vertices:
            for j in conjunto_vertices:
                if i != j and j not in lista[i]:
                    clique_bool = False
                    break
            if not clique_bool:
                break

        if clique_bool:
            print("O conjunto de vértices é um clique no grafo.")
            return True
        else:
            print("O conjunto de vértices não é um clique no grafo.")
            return False
    
    def verificar_clique_maximal(self, conjunto_vertices):
        clique_maximal_bool = True

        for i in self.lista:
            if i not in conjunto_vertices:
                clique_possivel = True
                for j in conjunto_vertices:
                    if j != i and j not in self.lista[i]:
                        clique_possivel = False
                        break
                if clique_possivel:
                    clique_maximal_bool = False
                    break

        if clique_maximal_bool:
            print("O conjunto de vértices é um clique maximal no grafo.")
        else:
            print("O conjunto de vértices não é um clique maximal no grafo.")

        return

    def complemento_grafo(self,matriz):
        vertices = len(matriz)
        complemento = [[0 for _ in range(vertices)] for _ in range(vertices)]

        for i in range(vertices):
            for j in range(vertices):
                if i != j and matriz[i][j] == 0:
                    complemento[i][j] = 1

        return complemento

    def conjunto_independente(self, conjunto_vertices):

        complemento = self.complemento_grafo(self.matriz)

        clique_no_complemento = self.verificar_clique(complemento, conjunto_vertices)

        if not clique_no_complemento:
       	    		
            print("Logo conjunto de vértices é um conjunto independente no grafo.")
        else:
            if clique_no_complemento:
            	print("Porem ")
            else:
            	print("Entao ")   
            print("o conjunto de vértices não é um conjunto independente no grafo.")

        return

if len(sys.argv) != 2:
    print("Uso: python meu_programa.py arquivo_grafo.txt")
    sys.exit(1)

nome_arquivo = sys.argv[1]


grafo = Grafo()


grafo.ler_grafo(nome_arquivo)
grafo.gerar_listaacencias()

print("\n------Matriz de adjacencias ------\n")
grafo.imprimir_matrizacencias()
print("\n------Lista de adjacencias ------\n")
grafo.imprimir_listaacencias()

print("\n------Graus do Grafo ------\n")
grau_minimo, grau_maximo = grafo.calcular_graus()

print(f"Graumaximo:{grau_maximo}")
print(f"Grau minimo: {grau_minimo}")

print("\n------Sequencia de Graus ------\n")
sequencia_de_graus = grafo.determinar_sequencia_de_graus()

print(f"Sequência de graus: {sequencia_de_graus}")

print("\n------Vizinança de cada vertice do Grafo------\n")
for i in grafo.lista:
    vertice = i
    grau, vizinhanca_aberta, vizinhanca_fechada = grafo.determinar_vizinhanca(vertice)

    print(f"Grau do vértice {vertice}: {grau}")
    print(f"Vizinhança aberta do vértice {vertice}: {vizinhanca_aberta}")
    print(f"Vizinhança fechada do vértice {vertice}: {vizinhanca_fechada}")

for i in grafo.lista:
    for j in grafo.lista:
        if i == j:
            continue
        else:
            if grafo.sao_vizinhos(i, j):
                print(f"Os vértices {i} e {j} são vizinhos.")
            else:
                print(f"Os vértices {i} e {j} não são vizinhos.")



print("\n------ Regularidade do Grafo ------\n")
regular, grau = grafo.verificar_regularidade()

if regular:
    print(f"O grafo é {grau}-regular.")
else:
    print("O grafo não é regular.")

print("\n------ Completude do Grafo ------\n")

grafo.verificar_completude()

print("\n------ Vertices Universais ------\n")

grafo.encontrar_vertices_universais()

print("\n------ Vertices Isolados ------\n")

grafo.encontrar_vertices_isolados()

print("\n------Passeio ------\n")

sequencia = [1,2,3]
grafo.verificar_passeio(sequencia)

print("\n------Caminho ------\n")

sequencia = [1, 2, 3, 4]
grafo.verificar_caminho(sequencia)

print("\n------Ciclo ------\n")

sequencia = [1, 2, 4, 3, 1]
grafo.verificar_ciclo(sequencia)

print("\n------Trilha ------\n")

sequencia = [1, 2, 3, 4]
grafo.verificar_trilha(sequencia) 

print("\n------Clique ------\n")

conjunto_vertices = {0,1}
grafo.verificar_clique(grafo.lista,conjunto_vertices)

print("\n------Clique Maximal------\n")

conjunto_vertices = {0,1,2,3}
grafo.verificar_clique_maximal(conjunto_vertices)

print("\n------Complemento do Grafo ------\n")
mtx = grafo.matriz
complemento = grafo.complemento_grafo(mtx)

for linha in complemento:
    print(linha)


print("\n------Conjunto Independente ------\n")

conjunto_vertices = {4,1,3}
grafo.conjunto_independente(conjunto_vertices)

print("\n------Subgrafo ------\n")

vertices = [0,1,2,3,4]
arestas = [(0, 1), (0, 2), (1, 0), (1, 3), (1,4), (2,0), (2,4), (3,1), (3,4), (4,1),(4,2),(4,3)]
subvertices = [0,1,2,3]
subarestas = [(0,1),(0,2),(1,0),(1, 3)]

if grafo.subgrafo(vertices, arestas, subvertices, subarestas):
    print("O subgrafo é um subgrafo do grafo original.")
else:
    print("O subgrafo não é um subgrafo do grafo original.")
