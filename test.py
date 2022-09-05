class Stack :
    def __init__(self, l = None) :
        if l == None :
            self.item = []
        else :
            self.item = l

    def __str__(self) :
        s = 'stack of ' + str(self.size())+' items : '
        for ele in self.items :
            s += str(ele) + ' '
        return s

    