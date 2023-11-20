class Node:
    def __init__(self, id, lines):
        """
        id: int
        lines: list of chars (R, G, B, Y)
        neighbors: list of Nodes
        previous: Node
        """
        self.id = id
        self.lines = lines
        self.neighbors = None
        self.previous = None
