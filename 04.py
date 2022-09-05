class Stack :
    def __init__(self,items = None) :
        if items == [] or items == None :
            self.items = []
        else :
            self.items = items

    def push(self,i) :
        self.items.append(i)

    def pop(self) :
        return self.items.pop(-1)

    def size(self) :
        return len(self.items)

    def isEmpty(self) :
        return self.items == []

def str_to_list(inp) :
    l = []
    x = ""
    n = 0
    while n < len(inp) :
        if inp[n] == ',' or inp[n] == " " :
            if x.isnumeric() :
                l.append(int(x))
            else :
                l.append(x)
            x = ""
        else :
            x += inp[n]
        n += 1
    if x.isnumeric() :
        l.append(int(x))
    else :
        l.append(x)
    return l

inp = input("Enter Input : ")
data = str_to_list(inp)
height = Stack()

for c in data :
    if c == 'A' :
        pass
    elif c == 'B' :
        print(len(height.items))
    else :
        if height.isEmpty() :
            height.push(c)
        else :
            if c < height.items[-1] :
                height.push(c)
            elif c > height.items[-1] :
                while c > height.items[-1] :
                    height.pop()
                    if height.isEmpty() :
                        break
                height.push(c)
            else :
                pass
    
