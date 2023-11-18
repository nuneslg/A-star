from node import Node

#refactor to stop using id 
g_scores = {(1,2):10, 
            (2,3):8.5, (2,9):10, (2,10):3.5,
            (3,4):6.3, (3,9):9.4, (3,13):18.7,
            (4,5):13, (4,8):15.3, (4,13):12.8, (4,14):11,
            (5,6):3, (5,7):2.4, (5,8):30,
            (8,9):9.6, (8,12):6.4,
            (9,11):12.2,
            (13,14):5.1}

#refactor to stop using id 
h_scores = {(1,2):10, (1,3):18.5, (1,4):24.8, (1,5):36.4, (1,6):38.8, (1,7):35.8, (1,8):25.4, (1,9):17.6, (1,10):9.1, (1,11):16.7, (1,12):27.3, (1,13):27.6, (1,14):29.8,
            (2,3):8.5, (2,4):14.8, (2,5):26.6, (2,6):29.1, (2,7):26.1, (2,8):17.3, (2,9):10, (2,10):3.5, (2,11):15.5, (2,12):20.9, (2,13):19.1, (2,14):21.8,
            (3,4):6.3, (3,5):18.2, (3,6):20.6, (3,7):17.6, (3,8):13.6, (3,9):9.4, (3,10):10.3, (3,11):19.5, (3,12):19.1, (3,13):12.1, (3,14):16.6,
            (4,5):12, (4,6):14.4, (4,7):11.5, (4,8):12.4, (4,9):12.6, (4,10):16.7, (4,11):23.6, (4,12):18.6, (4,13):10.6, (4,14):15.4,
            (5,6):3, (5,7):2.4, (5,8):19.4, (5,9):23.3, (5,10):28.2, (5,11):34.2, (5,12):24.8, (5,13):14.5, (5,14):17.9,
            (6,7):3.3, (6,8):22.3, (6,9):25.7, (6,10):30.3, (6,11):36.7, (6,12):27.6, (6,13):15.2, (6,14):18.2,
            (7,8):20, (7,9):23, (7,10):27.3, (7,11):34.2, (7,12):25.7, (7,13):12.4, (7,14):15.6,
            (8,9):8.2, (8,10):20.3, (8,11):16.1, (8,12):6.4, (8,13):22.7, (8,14):27.6,
            (9,10):13.5, (9,11):11.2, (9,12):10.9, (9,13):21.2, (9,14):26.6,
            (10,11):17.6, (10,12):24.2, (10,13):18.7, (10,14):21.2,
            (11,12):14.2, (11,13):31.5, (11,14):35.5,
            (12,13):28.8, (12,14):33.6,
            (13,14):5.1}

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)
e7 = Node(7)
e8 = Node(8)
e9 = Node(9)
e10 = Node(10)
e11 = Node(11)
e12 = Node(12)
e13 = Node(13)
e14 = Node(14)

e1.neighbors = [e2]
e2.neighbors = [e1, e3, e9, e10]
e3.neighbors = [e2, e4, e9, e13]
e4.neighbors = [e3, e5, e8, e13]
e5.neighbors = [e4, e6, e7, e8]
e6.neighbors = [e5]
e7.neighbors = [e5]
e8.neighbors = [e4, e5, e9, e12]
e9.neighbors = [e2, e3, e8, e11]
e10.neighbors = [e2]
e11.neighbors = [e9]
e12.neighbors = [e8]
e13.neighbors = [e3, e4, e14]
e14.neighbors = [e13]

nodes = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]