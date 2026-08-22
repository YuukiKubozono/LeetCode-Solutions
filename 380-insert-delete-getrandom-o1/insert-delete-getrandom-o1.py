class RandomizedSet:

    def __init__(self):
        self.val = []
        self.val_to_index = {}
    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        else:
            self.val.append(val)
            self.val_to_index[val] = len(self.val) - 1
            return True
    def remove(self, val: int) -> bool:
        if not val in self.val_to_index:
            return False
        else:
            idx = self.val_to_index[val]
            last_val = self.val[-1]

            self.val[idx] = last_val 
            self.val_to_index[last_val] = idx

            self.val.pop()
            del self.val_to_index[val]
            return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.val)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()