class Stack :
    def __init__(self,items = None) :
        if items == [] or items == None :
            self.items = []
        else :
            self.items = items

    def push(self,i) :
        self.items.append(i)

    def pop(self) :
        return self.items.pop(0)

    def size(self) :
        return len(self.items)

    def isEmpty(self) :
        return self.items == []

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
data = s.split(',')
soi = Stack()
for c in data :
    if c != '0' :
        soi.push(int(c))
### Enter Your Code Here ###
#check operation
if o == "arrive" :
    #soi full case
    if soi.size() >= m :
        print("car " + str(n) + " cannot arrive : Soi Full")
        print(soi.items)
    #can arrive case
    else :
        if n in soi.items :
            print("car " + str(n) + " already in soi")
            print(soi.items)
        else :
            print("car " + str(n) + " arrive! : Add Car " + str(n))
            soi.push(n)
            print(soi.items)
    pass
elif o == "depart" :
    #empty case
    if soi.isEmpty() :
        print("car " + str(n) + " cannot depart : Soi Empty")
        print(soi.items)
    else :
        #does has car case
        if n not in soi.items :
            print("car " + str(n) + " cannot depart : Dont Have Car " + str(n))
            print(soi.items)
        #can depart case
        else :
            while n in soi.items :
                soi.pop()
            print("car " + str(n) + " depart ! : Car " + str(n) + " was remove")
            print(soi.items)
    
    