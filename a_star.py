from distances import *
from node import *

def aStar(start, s_line, goal, g_line):
    Open = []
    closed = []
    counter = 1

    # g and f scores for each pair of node and line
    g_score = {str(node.id)+line : float('inf') for node in nodes for line in node.lines} 
    f_score = {str(node.id)+line : float('inf') for node in nodes for line in node.lines}

    g_score[str(start.id)+s_line] = 0 
    f_score[str(start.id)+s_line] = h(start, goal)

    Open.append((f_score[str(start.id)+s_line], start, s_line))
    nodeParent = {} #dictionary to store the parent of each node

    while Open != []:
        curr, line = Open.pop(0)[1:] #gets the id of the node with the lowest f-score and the line
        closed.append(curr) #add the node to the closed list
        if curr == goal:
            if line == g_line:
                totalTime = f_score[str(curr.id)+line] #total time is the f-score of the goal's node 
                break
            else:
                if g_score[str(curr.id)+line] + 4 < g_score[str(curr.id)+g_line]: #if the time with transfer is less than the current calculated time
                    nodeParent[(curr, g_line)] = (curr, line) #add the transfer to the path
                    totalTime = f_score[str(curr.id)+line] + 4
                    line = g_line
                    break
        for neighbor in curr.neighbors:
            if neighbor not in closed:
                tempGScore = g(curr.id, neighbor.id) + g_score[str(curr.id)+line]
                tempLine = line
                if line not in neighbor.lines:
                    tempGScore += 4 #add 4 minutes for changing lines
                    for n_line in curr.lines:
                        if n_line != line:
                            tempLine = n_line
                tempFScore = tempGScore + h(neighbor.id, goal.id) 

                if tempFScore < f_score[str(neighbor.id)+tempLine]: #if the new f-score is less than the current f-score
                    #update the f-score and g-score
                    g_score[str(neighbor.id)+tempLine] = tempGScore
                    f_score[str(neighbor.id)+tempLine] = tempFScore
                    Open.append((tempFScore, neighbor, tempLine))
                    nodeParent[(neighbor, tempLine)] = (curr, line)
                
        print(f'{counter}ª Fronteira:', end=' [')
        Open.sort(key=lambda x: x[0])
        for i in Open:
            print(f'{i[1].id}{i[2]}', end='')
            if i != Open[-1]:
                print(',', end=' ')
            else: print(']', end='')
        print()
        counter += 1  

    path = []
    curr = goal

    while curr != start:
        parent, parentLine = nodeParent[(curr, line)]
        if parentLine != line and parent != curr: #add the transfer to the path
            path.append((parent, line))
        path.append((parent, parentLine))
        curr, line = parent, parentLine

    print("\nMelhor caminho: ")
    for node, line in reversed(path):
        print(f'{node.id}{line}', end=' -> ')
    print(f'{goal.id}{g_line}\n')
    print("Tempo total: ", totalTime, "min")