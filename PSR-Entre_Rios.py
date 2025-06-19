# Introduzca aquí su solución.
from simpleai.search import CspProblem, backtrack
import networkx as nx
import matplotlib.pyplot as plt

# Esta funcion implementa la restriccion de que dos ciudades limitrofes no deben ser del mismo color
def funcion_restriccion(ciudades, colores):
    ciudad1, ciudad2 = ciudades
    color1, color2 = colores

    # Verificamos que los colores sean diferentes
    return color1 != color2

if __name__ == "__main__":

  #Lista con las ciudades de Entre Rios
  departamentos = ('Concordia', 'Federacion', 'Feliciano', 'La Paz',
             'Federal', 'San Salvador', 'Villaguay', 'Colon',
             'Uruguay', 'Gualeguaychu', 'Islas del Ibicuy',
             'Gualeguay' ,'Tala', 'Nogoya','Victoria',
             'Diamante','Parana')

  colores = dict((depto, ['red', 'green', 'blue', 'violet']) for depto in departamentos)

  vecinos = [
      (('Villaguay', 'Federal'), funcion_restriccion),
      (('Villaguay', 'San Salvador'), funcion_restriccion),
      (('Villaguay', 'Colon'), funcion_restriccion),
      (('Villaguay', 'Uruguay'), funcion_restriccion),
      (('Villaguay', 'Tala'), funcion_restriccion),
      (('Villaguay', 'Nogoya'), funcion_restriccion),
      (('Villaguay', 'Parana'), funcion_restriccion),
      (('Villaguay', 'La Paz'), funcion_restriccion),
      (('Tala', 'Nogoya'), funcion_restriccion),
      (('Tala', 'Uruguay'), funcion_restriccion),
      (('Tala', 'Gualeguaychu'), funcion_restriccion),
      (('Tala', 'Gualeguay'), funcion_restriccion),
      (('Islas del Ibicuy', 'Gualeguaychu'), funcion_restriccion),
      (('Islas del Ibicuy', 'Gualeguay'), funcion_restriccion),
      (('Gualeguay', 'Victoria'), funcion_restriccion),
      (('Gualeguay', 'Nogoya'), funcion_restriccion),
      (('Gualeguay', 'Gualeguaychu'), funcion_restriccion),
      (('Victoria', 'Nogoya'), funcion_restriccion),
      (('Victoria', 'Diamante'), funcion_restriccion),
      (('Parana', 'Diamante'), funcion_restriccion),
      (('Parana', 'Nogoya'), funcion_restriccion),
      (('Parana', 'La Paz'), funcion_restriccion),
      (('Feliciano', 'Federal'), funcion_restriccion),
      (('Feliciano', 'Federacion'), funcion_restriccion),
      (('Feliciano', 'La Paz'), funcion_restriccion),
      (('Federacion', 'Federal'), funcion_restriccion),
      (('Concordia', 'Federacion'), funcion_restriccion),
      (('Concordia', 'Federal'), funcion_restriccion),
      (('Concordia', 'San Salvador'), funcion_restriccion),
      (('Concordia', 'Colon'), funcion_restriccion),
      (('Colon', 'San Salvador'), funcion_restriccion),
      (('Colon', 'Uruguay'), funcion_restriccion),
      (('Diamante', 'Nogoya'), funcion_restriccion),
    ]

  problema = CspProblem(departamentos, colores, vecinos)
  salida = backtrack(problema)

  print('\nMapa de colores\n')
  for (x, y) in salida.items():
    print(x, "-->", y)

# Crear grafo con networkx
print("\n-------------GRAFO--------------------\n")

G = nx.Graph()
G.add_edges_from([(a, b) for (a, b), _ in vecinos])

# Dibujar el grafo coloreado
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)

# Extraer colores desde la solución
node_colors = [salida[n] for n in G.nodes()]

nx.draw(G, pos, with_labels=True,
        node_color=node_colors, node_size=2000,
        font_size=10, edge_color='gray')

plt.title("Grafo de restricciones coloreado (CSP)")
plt.show()
