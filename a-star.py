from queue import PriorityQueue
from data import *

def g(i, j):
    if (i,j) in g_scores:
        return g_scores[(i,j)]
    elif (j,i) in g_scores:
        return g_scores[(j,i)]
    else:
        return 0
    
def h(i, j):
    if (i,j) in h_scores:
        return h_scores[(i,j)]
    elif (j,i) in h_scores:
        return h_scores[(j,i)]
    else:
        return 0

Open = PriorityQueue()
g_score = {node : float('inf') for node in nodes}
f_score = {node : float('inf') for node in nodes}

#only for debugging
start = e12
goal = e7
line = 'G'

g_score[start] = 0
f_score[start] = h(start, goal)
Open.put((f_score[start], start, line))
reversedPath = {}

while Open != []: 
    curr, line = Open.get()[1:] # get the id of the node with the lowest f-score and the line
    if curr == goal:
        break
    for neighbor in curr.neighbors:
        #if curr == start:
            #curr.previous = curr (desnecessário?)
        tempGScore = g(curr.id, neighbor.id) + g_score[curr]
        tempLine = line
        if line not in neighbor.lines:
            tempGScore += 2 #add 4 minutes for changing lines
            for n_line in curr.lines:
                if n_line != line:
                    tempLine = n_line
        #talvez seja necessário guardar essa baldeação
        tempFScore = tempGScore + h(neighbor.id, goal.id) 

        if tempFScore < f_score[neighbor]:
            g_score[neighbor] = tempGScore
            f_score[neighbor] = tempFScore
            print(f_score)
            Open.put((tempFScore, neighbor, tempLine))
            reversedPath[neighbor.id] = curr.id
            #neighbor.previous = curr (desnecessário?)

print(reversedPath)
print('oi')

'''
path = {}
curr = goal
while curr != start:
    path[reversedPath[curr]] = curr
    curr = reversedPath[curr]
'''