class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.dict = {}

        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.lst.append(val)
        self.dict[val] = len(self.lst) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        index = self.dict[val]
        last = self.lst[-1]

        # swap
        self.lst[index] = last
        self.dict[last] = index

        # remove last
        self.lst.pop()
        del self.dict[val]

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()