# Una clase para representar un conjunto disjunto
class DisjointSet:
    def __init__(self):
        self.parent = {}

    # Realiza la operación MakeSet
    def makeSet(self, n):
        # Crear 'n' conjuntos disjuntos (uno para cada vértice)
        for i in range(n):
            self.parent[i] = i

    # Encuentra la raíz del conjunto al que pertenece el elemento 'k'
    def find(self, k):
        if self.parent[k] == k:
            return k
        # Recurre para el padre hasta que encontramos la raíz
        return self.find(self.parent[k])

    # Realizar la unión de dos subconjuntos
    def union(self, a, b):
        # Encontrar la raíz de los conjuntos a los que pertenecen los elementos x e y
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y

# Función para construir MST usando el algoritmo de Kruskal
def runKruskalAlgorithm(edges, n):
    # Almacenar los bordes presentes en MST
    MST = []

    # Inicializa la clase 'DisjointSet'
    # Crea un conjunto singleton para cada elemento del universo
    ds = DisjointSet()
    ds.makeSet(n)

    index = 0

    # Ordena los bordes aumentando el peso
    edges.sort(key=lambda x: x[2])
    while len(MST) != n - 1:
        # Considerar el borde siguiente con peso mínimo del gráfico
        (src, dest, weight) = edges[index]
        index = index + 1

        # Encontrar la raíz de los conjuntos a los que se unen dos extremos
        # Vértices de la siguiente arista pertenecen
        x = ds.find(src)
        y = ds.find(dest)

        # Si ambos extremos tienen diferentes padres, pertenecen a
        # Diferentes componentes conectados y se pueden incluir en MST
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)

    return MST

if __name__ == '__main__':
    # (u, v, w) el triplete representa un borde no dirigido desde
    # vértice 'u' a vértice con peso 'w'
    edges = [
        (0, 1, 7),
        (1, 2, 8),
        (0, 3, 5),
        (1, 3, 9),
        (1, 4, 7),
        (2, 4, 5),
        (3, 4, 15),
        (3, 5, 6),
        (4, 5, 8),
        (4, 6, 9),
        (5, 6, 11)
    ]

    n = 7

    e = runKruskalAlgorithm(edges, n)

    print(e)