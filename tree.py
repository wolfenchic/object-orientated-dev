class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
    def add(self, value):
        if value < self.value:
           t.left = Tree(value)
        else:
            t.right = Tree(value)
        
        
t = Tree(5)
t.add(7)
t.add(2)
t.add(13)
print(t.right.value)
print(t.left.value)


