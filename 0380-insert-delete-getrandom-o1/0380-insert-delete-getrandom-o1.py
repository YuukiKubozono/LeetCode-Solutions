class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.list = []
        self.id = 0
    def insert(self, val: int) -> bool:
        if val not in self.hash:
            self.list.append(val)
            self.hash[val] = self.id
            self.id += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hash:
            self.id -= 1
            last = self.list[-1]
            id = self.hash[val]
            self.hash[last] = id
            self.list[id], last = last, self.list[id]
            self.list.pop()
            del self.hash[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()