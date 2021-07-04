class Skiplist:

    def __init__(self):
        self.ds = {}
        

    def search(self, target: int) -> bool:
        return target in self.ds 

    def add(self, num: int) -> None:
        self.ds[num] = self.ds.get(num, 0) + 1

    def erase(self, num: int) -> bool:
        if num not in self.ds: return false 
        self.ds[num] -= 1
        if self.ds[num] == 0:
            del self.ds[num]
        return true 
        
