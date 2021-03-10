class myDictionary:
    def __init__(self):
        self.myDict = {}

    def addItem(self,k):
        if k not in self.myDict:
            self.myDict[k] = 1
        else:
            self.myDict[k] += 1
        
    def printd(self):
        print(self.myDict)
    
    def getvalue(self,k):
        print(self.myDict[k])


cc = myDictionary()
cc.addItem("g")
cc.addItem("g")
cc.addItem("g")
cc.addItem("g")
cc.addItem("g")
cc.printd()
cc.getvalue("g")
