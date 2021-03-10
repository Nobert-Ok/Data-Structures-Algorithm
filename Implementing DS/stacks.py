class myStack():
    def __init__(self):
        self.data = []

    def isempty(self):
        return len(self.data) == 0

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        return self.data.pop()

    def push(self,k):
        return self.data.append(k)

    def length(self):
        return len(self.data)

    def top(self):
        if self.isempty():
            return print("Stack is empty")
        return self.data[-1]

    def printd(self):
        print(self.data)
        
cc = myStack()
cc.push(4)
cc.push(5)
cc.push(6)
cc.push(7)
print(cc.pop())
print(cc.top())
print(cc.isempty())

cc.isempty()


