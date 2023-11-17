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

g_score[start] = 0
f_score[start] = h(start, goal)
Open.put((f_score[start], f_score[start], start))
reversedPath = {}

while Open != []: 
    curr = Open.get()[1] # get the id of the node with the lowest f-score
    if curr == goal:
        break
    for neighbor in curr.neighbors:
        if curr == start:
            curr.previous = curr

        tempGScore = g(curr.id, curr.previous.id) #g-score of current (0) 
        tempFScore = tempGScore + h(neighbor.id, goal.id) #f-score of neighbor (27.4)

        if tempFScore < f_score[neighbor]:
            if f_score[neighbor] == float('inf'): #if neighbor was never visited
                g_score[neighbor] = tempGScore
                f_score[neighbor] = tempFScore
            else:
                g_score[neighbor] = tempGScore + g_score[curr]
                f_score[neighbor] = tempFScore + g_score[curr]
            Open.put((tempFScore, neighbor))
            reversedPath[neighbor] = curr
            neighbor.previous = curr

print(reversedPath)

'''
path = {}
curr = goal
while curr != start:
    path[reversedPath[curr]] = curr
    curr = reversedPath[curr]
'''