class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.data:
            if self.data[key]>1:
                self.data[key] -= 1
            else:
                self.data.pop(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.data:
            return ''
        max_value = 0
        max_key = None
        for k,v in self.data.items():
            if v>max_value:
                max_value = v
                max_key = k
        return max_key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if not self.data:
            return ''
        min_value = float('inf')
        min_key = None
        for k,v in self.data.items():
            if v<min_value:
                min_value = v
                min_key = k
        return min_key
