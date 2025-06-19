# Completar con el código correspondiente
from simpleai.search import astar, SearchProblem

# Clase que contiene métodos para resolver el puzzle.
class PuzzleSolver(SearchProblem):

    # Explicar el objetivo de "def actions(self, cur_state)"
    # Esta funcion toma un estado actual y devuelve una lista con todas las fichas valizas para mover.
    def actions(self, cur_state):
        rows = string_to_list(cur_state)
        row_empty, col_empty = get_location(rows, 'z')

        actions = []
        if row_empty > 0:
            actions.append(rows[row_empty - 1][col_empty])
        if row_empty < 2:
            actions.append(rows[row_empty + 1][col_empty])
        if col_empty > 0:
            actions.append(rows[row_empty][col_empty - 1])
        if col_empty < 2:
            actions.append(rows[row_empty][col_empty + 1])
        return actions

    # Devuelve el estado resultante después de mover una pieza al espacio vacío
    def result(self, state, action):
        rows = string_to_list(state)
        row_empty, col_empty = get_location(rows, 'z')
        row_new, col_new = get_location(rows, action)

        rows[row_empty][col_empty], rows[row_new][col_new] = \
                rows[row_new][col_new], rows[row_empty][col_empty]

        return list_to_string(rows)

    # Retorna verdadero si el estado es estado objetivo
    def is_goal(self, state):
        return state == GOAL

    # Explicar el objetivo de "def heuristic(self, state)"
    # Indicar que heurística se utiliza
    # Esta funcion estima cuánto falta para llegar a completar el puzzle desde un estado dado. Está utilizando la distancia Manhattan como heuristica.
    # La suma de movimientos necesarios para llegar al objetivo
    def heuristic(self, state):
        rows = string_to_list(state)

        distance = 0

        for number in '12345678z':
            row_new, col_new = get_location(rows, number)
            row_new_goal, col_new_goal = goal_positions[number]

            distance += abs(row_new - row_new_goal) + abs(col_new - col_new_goal)

        return distance

# Convierte lista en string
def list_to_string(input_list):
    return '\n'.join(['-'.join(x) for x in input_list])

# Convierte string en lista
def string_to_list(input_string):
    return [x.split('-') for x in input_string.split('\n')]

# Encuentra la ubicación 2D del elemento de entrada
def get_location(rows, input_element):
    for i, row in enumerate(rows):
        for j, item in enumerate(row):
            if item == input_element:
                return i, j

# Final result that we want to achieve
GOAL = '''1-2-3
4-5-6
7-8-z'''

# Starting point
INITIAL = '''1-z-2
6-5-4
8-3-7'''

#Crea un caché para la posición de la meta de cada pieza.
goal_positions = {}
rows_goal = string_to_list(GOAL)
for number in '12345678z':
    goal_positions[number] = get_location(rows_goal, number)


# Explicar el objetivo de "result"
# result contiene el camino encontrado por el algoritmo A*.
result = astar(PuzzleSolver(INITIAL))
# Muestra en pantalla los resultados
for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Configuración inicial')
    elif i == len(result.path()) - 1:
        print('Después de mover', action, 'al espacio vacío. Objetivo alcanzado!')
    else:
        print('Después de mover', action, 'al espacio vacío')

    print(state)
