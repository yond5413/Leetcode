class TimeMap:

    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        if key not in self.lookup:
            return ret
        arr = self.lookup[key]
        l,r = 0,len(arr)-1
        while (l<=r):
            mid = (r+l)//2
            ts,val = arr[mid]
            if ts<=timestamp:
                ret = val
                l = mid+1
            else:
                r = mid-1
        return ret


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)