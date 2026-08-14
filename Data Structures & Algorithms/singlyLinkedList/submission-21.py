class LinkedList:
    
    def __init__(self):
        self.ll = {'head':None}

    
    def get(self, index: int) -> int:
        count = 0
        current = self.ll['head']
        while current:
            if index == count:
                return current.data
            current = current.n
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        temp = self.ll['head']
        self.ll['head'] = nodes(val,temp)

    def insertTail(self, val: int) -> None:
        current = self.ll['head']
        nex = None
        found = False
        if current:
            nex = current.n
        else:
            self.ll['head'] = nodes(val,None)
            found = True
        while nex:
            current = nex
            nex = nex.n
        if not found:
            nex = nodes(val,None)
            current.change_n(nex)

    def remove(self, index: int) -> bool:
        count = 0
        current = self.ll['head']
        if not current:
            return False
        elif index == 0:
            self.ll['head']= current.n
            return True
        while current:
            if count+1 == index and current.n:
                if current.n:
                    new = current.n
                    new = new.n
                else:
                    new = None
                current.change_n(new)
                return True
            current = current.n
            count += 1
        return False
        

    def getValues(self) -> List[int]:
        l = []
        current = self.ll['head']
        while current:
            l.append(current.data)
            current = current.n
        return l

class nodes:

    def __init__(self,data,n):
        self.data = data
        self.n = n

    def change_n(self,new):
        self.n = new