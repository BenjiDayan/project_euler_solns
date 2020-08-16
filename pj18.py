#pj18

def triangle_to_list(textTriangle):
    b = textTriangle.split('\n')
    c = []
    for thing in b:
        c.append(thing.split(' '))

    d = []
    for thing in c:
        d.append([])
        for numString in thing:
            d[-1].append(int(numString))
    return(d)

class node():
    
    
    def __init__(self, data, parent=None):
        self.children = []
        self.parent = parent
        self.data = data
        self.level = parent.get_level() + 1 if parent != None else 0
        if parent != None:
            parent.children.append(self)

    def get_data(self):
        return(self.data)

    def get_parent(self):
        return(self.parent)

    def get_level(self):
        return(self.level)

    def get_children(self):
        return(self.children)

class triangle_level(node):

    
    def __init__(self, numList, parent=None):
        node.__init__(self, numList, parent)

        if self.parent == None:
            self.max = self.data
        else:
            self.max = []
            for num in range(len(self.data)):
                if num == 0:
                    self.max.append(self.parent.max[0] + self.data[0])
                elif num == len(self.data)-1:
                    self.max.append(self.parent.max[-1] + self.data[-1])
                else:
                    a = self.parent.max[num-1]
                    b = self.parent.max[num]
                    c = a if a>b else b
                    self.max.append(c + self.data[num])
    
    
