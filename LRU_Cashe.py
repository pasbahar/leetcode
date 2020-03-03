from collections import deque

class LRUCashe:
    def __init__(self,capacity:int):
        self.d={}
        self.dq=deque()

    def get(self,key:int):
        if key in self.d.keys():
            return self.dq[d[key]]
        else: return -1

    def put(self,key:int,value:int):
        if key in self.d:
            self.dq.pop(d[value])
            self.dq.leftappend(value)
            self.d[value]=0
        else:
            tmp=self.dq.pop()
            self.dq.leftappend(value)
            self.d[value]=0
            del self.d[tmp]

p=LRUCashe(2)
p.put(1,1)
print(p.get(1))          

            

    
