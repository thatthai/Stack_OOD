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


inp = input('Enter Infix : ')
stack = Stack()
print('Postfix : ', end='')
### Enter Your Code Here ###
for c in inp :
    current_priority = 0
    stack_priority = 0
    if c in '[]{()}' :
        current_priority = 1
        if stack.isEmpty() :
            stack.push(c)
        elif c in ')}]' :
            while stack.items[-1] not in '({[' :
                if stack.items[-1] not in '({[' :
                    print(stack.pop(),end = "")
            stack.pop()
        else :
            #set priority of stack's elemnt
            if stack.items[-1] in '[]{()}' :
                stack_priority = 5
            elif stack.items[-1] in '^' :
                stack_priority = 2
            elif stack.items[-1] in '*/' :
                stack_priority = 3
            elif stack.items[-1] in '+-' :
                stack_priority = 4

            if current_priority < stack_priority :
                stack.push(c)
            else :
                while current_priority >= stack_priority :
                    if stack.items[-1] in '[]{()}' :
                        stack_priority = 5
                        break
                    elif stack.items[-1] in '^' :
                        stack_priority = 2
                    elif stack.items[-1] in '*/' :
                        stack_priority = 3
                    elif stack.items[-1] in '+-' :
                        stack_priority = 4
                    if stack.isEmpty() :
                        break
                    print(stack.pop(),end = "")
                stack.push(c)
    elif  c == '^' :
        current_priority = 2
        if stack.isEmpty() :
            stack.push(c)
        else :
            #set priority of stack's elemnt
            if stack.items[-1] in '[]{()}' :
                stack_priority = 5
            elif stack.items[-1] in '^' :
                stack_priority = 2
            elif stack.items[-1] in '*/' :
                stack_priority = 3
            elif stack.items[-1] in '+-' :
                stack_priority = 4

            if current_priority < stack_priority :
                stack.push(c)
            else :
                while current_priority >= stack_priority :
                    if stack.items[-1] in '[]{()}' :
                        stack_priority = 5
                    elif stack.items[-1] in '^' :
                        stack_priority = 2
                    elif stack.items[-1] in '*/' :
                        stack_priority = 3
                    elif stack.items[-1] in '+-' :
                        stack_priority = 4
                    print(stack.pop(),end = "")
                    if stack.isEmpty() :
                        break
                stack.push(c)
    elif c in '*/' :
        current_priority = 3
        if stack.isEmpty() :
            stack.push(c)
        else :
            #set priority of stack's elemnt
            if stack.items[-1] in '[]{()}' :
                stack_priority = 5
            elif stack.items[-1] in '^' :
                stack_priority = 2
            elif stack.items[-1] in '*/' :
                stack_priority = 3
            elif stack.items[-1] in '+-' :
                stack_priority = 4
            
            if current_priority < stack_priority :
                stack.push(c)
            else :
                while current_priority >= stack_priority :
                    if stack.items[-1] in '[]{()}' :
                        stack_priority = 5
                    elif stack.items[-1] in '^' :
                        stack_priority = 2
                    elif stack.items[-1] in '*/' :
                        stack_priority = 3
                    elif stack.items[-1] in '+-' :
                        stack_priority = 4
                    if current_priority >= stack_priority :
                        print(stack.pop(),end = "")
                    if stack.isEmpty() :
                        break
                stack.push(c)

    elif c in '+-' :
        current_priority = 4
        if stack.isEmpty() :
            stack.push(c)
        else :
            #set priority of stack's elemnt
            if stack.items[-1] in '[]{()}' :
                stack_priority = 1
            elif stack.items[-1] in '^' :
                stack_priority = 2
            elif stack.items[-1] in '*/' :
                stack_priority = 3
            elif stack.items[-1] in '+-' :
                stack_priority = 4

            if current_priority < stack_priority :
                stack.push(c)
            else :
                while current_priority >= stack_priority :
                    if stack.items[-1] in '[]{()}' :
                        break
                    elif stack.items[-1] in '^' :
                        stack_priority = 2
                    elif stack.items[-1] in '*/' :
                        stack_priority = 3
                    elif stack.items[-1] in '+-' :
                        stack_priority = 4
                    print(stack.pop(),end = "")
                    if stack.isEmpty() :
                        break
                stack.push(c)
    else :
        print(c,end = "")

while not stack.isEmpty() :
    print(stack.pop(),end = "")
