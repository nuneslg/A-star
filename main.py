from a_star import *

start = int(input('Digite a estação de partida: '))
s_line = input('Digite a linha de partida: ').upper()
goal = int(input('Digite a estação de chegada: '))
g_line = input('Digite a linha de chegada: ').upper()
print()

start = nodes[start-1]
goal = nodes[goal-1]

aStar(start, s_line, goal, g_line)