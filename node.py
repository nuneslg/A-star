class Node:
    def __init__(self, id, lines):
        """
        id: int
        lines: list of chars (R, G, B, Y)
        neighbors: list of Nodes
        """
        self.id = id
        self.lines = lines
        self.neighbors = None

    def __repr__(self):
        return (f'e{self.id}')
    
# initialize nodes with id and lines
e1 = Node(1, ['B'])
e2 = Node(2, ['B', 'Y'])
e3 = Node(3, ['B', 'R'])
e4 = Node(4, ['B', 'G'])
e5 = Node(5, ['B', 'Y'])
e6 = Node(6, ['B'])
e7 = Node(7, ['Y'])
e8 = Node(8, ['G', 'Y'])
e9 = Node(9, ['R', 'Y'])
e10 = Node(10, ['Y'])
e11 = Node(11, ['R'])
e12 = Node(12, ['G'])
e13 = Node(13, ['R', 'G'])
e14 = Node(14, ['G'])

# initialize neighbors
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