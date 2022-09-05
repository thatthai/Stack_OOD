class Stack :

    def __init__(self, items = None) :
        if items == None or items == [] :
            self.items = []
        else :
            self.items = items

    def push(self, i) :
        self.items.append(i)
    
    def pop(self) :
        return self.items.pop()

    def delete(self, i) :
        self.items.remove(i)

    def peek(self) :
        return self.items[-1]

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

def ManageStack(data) :
    S = Stack(data)
    Temp = Stack()
    Answer = Stack()
    while not S.isEmpty() :
        if isinstance(S.peek(), int)  :
            if Temp.peek() == 'A' :
                Answer.push(S.peek())
                print("Add = " + str(S.pop()))
                Temp.pop()
            elif Temp.peek() == 'D' :
                if Answer.isEmpty() :
                    print(-1)
                    S.pop()
                    Temp.pop()
                else :
                    while S.peek() in Answer.items :
                        Answer.delete(S.peek())
                        print("Delete = " + str(S.peek()))
                    S.pop()
                    Temp.pop()
            elif Temp.peek() == 'LD' : #delete less than x
                if Answer.isEmpty() :
                    print(-1)
                    S.pop()
                    Temp.pop()
                else :
                    m = []
                    n = []
                    for i in Answer.items :
                        if i < S.peek() :
                            n.append(i)
                        else :
                            m.append(i)
                    n.sort()
                    for j in n:
                        print("Delete = " + str(j) + " Because " + str(j) + " is less than " + str(S.peek()))
                    Answer.items = m
                    S.pop()
                    Temp.pop()
            elif Temp.peek() == 'MD' : #delete more than x
                if Answer.isEmpty() :
                    print(-1)
                    S.pop()
                    Temp.pop()
                else :
                    m = []
                    n = []
                    for i in Answer.items :
                        if i > S.peek() :
                            print("Delete = " + str(i) + " Because " + str(i) + " is more than " + str(S.peek()))
                        else :
                            m.append(i)
                    # n.sort()
                    # for j in n :
                    #     print("Delete = " + str(j) + " Because " + str(j) + " is more than " + str(S.peek()))
                    Answer.items = m
                    S.pop()
                    Temp.pop()
        elif S.peek() == 'P' :
            if Answer.isEmpty() :
                print(-1)
                S.pop()
            else :
                print("Pop = " + str(Answer.pop()))
                S.pop()
        else :
            Temp.push(S.pop())
    print("Value in Stack = " + str(Answer.items)) 

def str_to_list(inp) :
    l = []
    s = []
    x = ""
    for c in inp :
        if c == " " or c == "," :
            if x == 'A' or x == 'D' or x == 'P' or x == 'MD' or x == 'LD' :
                l.append(x)
            else :
                l.append(int(x))
            x = ""
        else :
            x += c
    n = -1
    a = ''
    while inp[n] != " " :
        if inp[n] == 'A' or inp[n] == 'D' or inp[n] == 'P' or inp[n] == 'MD' or inp[n] == 'LD' :
            l.append(inp[-1])
            break
        else :
            a += inp[n]
        n -= 1
    b = ''
    c = len(a) - 1
    while c >= 0 :
        b += a[c]
        c -= 1
    l.append(int(b))
    while len(l) != 0 :
        s.append(l[-1])
        l.pop(-1)
    return s

inp = input("Enter Input : ")
data = str_to_list(inp)
#print(data)
ManageStack(data)
