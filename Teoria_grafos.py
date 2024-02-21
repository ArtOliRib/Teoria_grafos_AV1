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

    def gerar_lista_adjacencias(self):
        for i in range(self.vertices):
            vizinhos = [j for j in range(self.vertices) if self.matriz[i][j] == 1] #Salva o valor da posição do valor 1 da matriz de
            self.lista[i] = vizinhos                                               #adjacencias, este sera o valor do vertice vizinho de i

    def imprimir_matriz_adjacencias(self):
        for linha in self.matriz:
            print(' '.join(map(str, linha)))


    def imprimir_lista_adjacencias(self):
        for vertice, vizinhos in self.lista.items():
            print(f'{vertice}: [{", ".join(map(str, vizinhos))}]')

    def calcular_graus(self):
        graus = [len(vizinhos) for vizinhos in self.lista.values()] #Armazena o numero de valores que estao presentes
        grau_minimo = min(graus)                                    #em cada lista de adjacencia de cada vertice.
        grau_maximo = max(graus)
        return grau_minimo, grau_maximo
    
    def determinar_sequencia_de_graus(self):
        graus = [len(vizinhos) for vizinhos in self.lista.values()] #conta o numero de valores que estao na lista de adjacencias do vertice
        graus.sort()                                                
        return graus
    
    def determinar_vizinhanca(self, vertice):
        vizinhos = self.lista[vertice]
        vizinhanca_aberta = set(vizinhos)
        vizinhanca_fechada_1 = set(vizinhos)
        vizinhanca_fechada_1.add(vertice)
        grau = len(vizinhos)
        return grau, vizinhanca_aberta, vizinhanca_fechada_1
    
    def sao_vizinhos(self, u, v):
        return u in self.lista[v] and v in self.lista[u] #Procura o valor do vertice "u" na lista do vertice de "v" e o valor do vertice "v" na lista ddo vertice de "u" e retorna
                                                         #verdadeiro caso eles sejam encontrados e falso caso no minimo 1 n seja encontrado.   
    def verificar_regularidade(self):
        graus = [len(vizinhos) for vizinhos in self.lista.values()]
        grau = graus[0]
        if all(grau == g for g in graus): #Testa se o grau de um vertice é igual ao grau de todos os outros do grafo.
            return True, grau
        else:
            return False, None

    def verificar_completude(self):
        num_arestas = sum(len(vizinhos) for vizinhos in self.lista.values()) // 2 #Obtem o numero de arestas que cada vertice possue e o salva.
        num_max_arestas = self.vertices * (self.vertices - 1) // 2 # Calculo da completude do grafo que foi dado.
        if num_arestas == num_max_arestas: #compara os valores do numero de arestas com o valor do grafo completo.
            print("O grafo é completo.")
        else:
            print("O grafo não é completo.")
        return 

    def encontrar_vertices_universais(self):
        vertices_universais = []
        for vertice in self.lista:
            vizinhos = set(self.lista[vertice]) #Salva a lista de um determinado vertice
            if len(vizinhos) == self.vertices - 1 and vertice not in vizinhos: # Se o valor dos vizinhos abertos de um vertice for n-1
                vertices_universais.append(vertice)                            # entao ele é universal

        if vertices_universais: #Se existir no minimo 1 vertice universal entao esse if sera verdadeiro.
            print("Vértices universais encontrados:")
            print(vertices_universais)
        else:
            print("Não há vértices universais no grafo.")
        return
    
    def encontrar_vertices_isolados(self):
        vertices_isolados = []
        for vertice in self.lista:
            if len(self.lista[vertice]) == 0:  #Verifica um vertice, se ele tiver 0 valores na sua lista de adjacencia, entao ele é isolado.
                vertices_isolados.append(vertice)

        if vertices_isolados:
            print("Vértices isolados encontrados:")
            print(vertices_isolados)
        else:
            print("Não há vértices isolados no grafo.")
        return
    
    
    def subgrafo(self,vertices, arestas, subvertices, subarestas):
    
        if set(subvertices).issubset(set(vertices)) and set(subarestas).issubset(set(arestas)): #se "vertices" contiver o "subvertices" e "arestas" contiver o "subarestas".
            for edge in subarestas:
                if edge[0] not in subvertices or edge[1] not in subvertices: #Verifica se o primeiro e o segundo valor (i,j) da aresta
                    return False                                             #nao estao presentes nos subvertices.
        return True
        

    def verificar_passeio(self, sequencia):
        sequencia_bool = True
        for i in range(len(sequencia) - 1): 
            if sequencia[i+1] not in self.lista[sequencia[i]]: #Verifica se o proximo valor da sequencia (i+1) nao é vizinho do valor anterior da sequencia (i) 
                sequencia_bool = False                         #entao nao é um passeio

        if sequencia_bool:
            print("A sequência é um passeio no grafo.")
        else:
            print("A sequência não é um passeio no grafo.")
        return 
    
    def verificar_caminho(self, sequencia):
        caminho_bool = True
        if len(set(sequencia)) != len(sequencia): #verifica se há valores duplicados
            caminho_bool = False 

        for i in range(len(sequencia) - 1): 
            if sequencia[i+1] not in self.lista[sequencia[i]]: #Verifica se o proximo valor da sequencia (i+1) nao é vizinho do valor anterior da sequencia (i)
                caminho_bool = False                           #entao nao é um caminho
            
        if caminho_bool:
            print("A sequência é um caminho no grafo.")
        else:
            print("A sequência não é um caminho no grafo.")

        return

    def verificar_ciclo(self, sequencia):
        ciclo_bool = True
        if len(sequencia) < 3 or sequencia[0] != sequencia[-1]: #Verifica se a sequencia tem menos de 3 elementos ou se o primeiro elemento é diferente do ultimo
            ciclo_bool = False 

        if len(set(sequencia)) != len(sequencia) - 1: #Verifica se há elementos duplicados, menos o ultimo que seja igual ao primeiro
            ciclo_bool = False  

        for i in range(len(sequencia) - 1):
            if sequencia[i+1] not in self.lista[sequencia[i]]: #Verifica se o proximo valor da sequencia (i+1) nao é vizinho do valor anterior da sequencia (i)
                ciclo_bool = False
            
        if ciclo_bool:
            print("A sequência é um ciclo no grafo.")
        else:
            print("A sequência não é um ciclo no grafo.")  

        return

    def verificar_trilha(self, sequencia):
        trilha_bool = True

        if len(set(sequencia)) != len(sequencia): #Verifica se há elementos duplicados
            trilha_bool = False  

        arestas_visitadas = set()
        for i in range(len(sequencia) - 1): 
            aresta = (sequencia[i], sequencia[i+1]) #criasse duplas com um valor da sequencia dada e seu sucessor
            if aresta in arestas_visitadas: #Se a aresta foi visitada anteriormente entao nao é trilha
                trilha_bool = False 
            if sequencia[i+1] not in self.lista[sequencia[i]]: #Se a sequencia nao existir na lista de adjacencias entao nao é uma trilha 
                trilha_bool = False  
            arestas_visitadas.add(aresta)

        if trilha_bool:
            print("A sequência é uma trilha no grafo.")
        else:
            print("A sequência não é uma trilha no grafo.")

        return
    
    
    def verificar_clique(self, lista, conjunto_vertices,nun_texto):
        clique_bool = True
        num = nun_texto
        for i in conjunto_vertices:
            for j in conjunto_vertices:
                if i != j and j not in lista[i]: #Se i nao aparece na lista de adjacencia de j e j é igual a i entao não há clique
                    clique_bool = False
                    break
            if not clique_bool: #se já n for clique so encerra a iteraçao de i mais cedo
                break

        if clique_bool:
            if nun_texto == 1:
                print("O conjunto de vértices é um clique no grafo.")
                return True
            else:
                return True
        else:
            if nun_texto == 1:
                print("O conjunto de vértices não é um clique no grafo.")
                return False
            else:
                return False
    
    def verificar_clique_maximal(self, conjunto_vertices):
        clique_maximal_bool = True

        for i in self.lista:
            if i not in conjunto_vertices:
                clique_possivel = True
                for j in conjunto_vertices:
                    if j != i and j not in self.lista[i]: #Se j nao aparece na lista de adjacencia de i e j é igual a i entao não há clique
                        clique_possivel = False
                        break
                if clique_possivel: #se ele verificar que existe uma clique porem i continua presente no conjunto de vertices entao ele n é clique maximo.
                    clique_maximal_bool = False
                    break

        if clique_maximal_bool:
            print("O conjunto de vértices é um clique maximal no grafo.")
        else:
            print("O conjunto de vértices não é um clique maximal no grafo.")

        return

    def complemento_grafo(self,matriz):
        vertices = len(matriz)
        complemento = [[0 for _ in range(vertices)] for _ in range(vertices)] # Cria-se uma matriz com somente o valor 0.

        for i in range(vertices):
            for j in range(vertices):
                if i != j and matriz[i][j] == 0: # Para todas as posiçoes verificadas que sao 0 na matriz de adjacencias do grafo desde que i seja diferente de j
                    complemento[i][j] = 1        # colocar o numero 1

        return complemento

    def conjunto_independente(self, conjunto_vertices):

        complemento = self.complemento_grafo(self.matriz) # Cria-se o complemento do grafo
        clique_no_complemento = self.verificar_clique(complemento, conjunto_vertices,0) # Verifica se existe um clique entre os valores do conjunto de vertices no complemento do grafo

        if not clique_no_complemento: #Se existir um clique no complemento entao ele é um conjunto independente
            print("O conjunto de vértices é um conjunto independente no grafo.")
        else:
            print("O conjunto de vértices não é um conjunto independente no grafo.")

        return

if len(sys.argv) != 2:
    print("Uso: python meu_programa.py arquivo_grafo.txt")
    sys.exit(1)

nome_arquivo = sys.argv[1]

grafo = Grafo()


grafo.ler_grafo(nome_arquivo)
grafo.gerar_lista_adjacencias()

print("\n------Matriz de adjacencias ------\n")

grafo.imprimir_matriz_adjacencias()

print("\n------Lista de adjacencias ------\n")

grafo.imprimir_lista_adjacencias()

print("\n------Graus do Grafo ------\n")
grau_minimo, grau_maximo = grafo.calcular_graus()

print(f"Graumaximo: {grau_maximo}")
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
        print(f"Vizinhança fechada do vértice {vertice}: {vizinhanca_fechada}\n")

print("\n------Adjacência de dois vertices do grafo------\n")
u = 0
v = 1

if grafo.sao_vizinhos(u, v):
    print(f"Os vértices {u} e {v} são vizinhos.")
else:
    print(f"Os vértices {u} e {v} não são vizinhos.")

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

sequencia = [0,1,4,2,0]
grafo.verificar_ciclo(sequencia)

print("\n------Trilha ------\n")

sequencia = [1, 2, 3, 4]
grafo.verificar_trilha(sequencia) 

print("\n------Clique ------\n")

conjunto_vertices = {0,1}
grafo.verificar_clique(grafo.lista,conjunto_vertices,1)

print("\n------Clique Maximal------\n")

conjunto_vertices = {0,1}
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
    print("O subgrafo é um subgrafo do grafo original.\n")

else:
    print("O subgrafo não é um subgrafo do grafo original.\n")