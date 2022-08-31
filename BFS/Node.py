class Node:

    def __init__(self, h, w, weight):
        self.h = h
        self.w = w
        self.weight = weight
        self.neighbours_index = []
        self.step = 0
        self.visited = False
        self.come_from_index = None

    def get_index(self):
        return self.h, self.w
