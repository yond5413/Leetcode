from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.lookup:
            return ""
        events = self.lookup[key]
        l,r = 0,len(events)-1
        ret = ''
        while(l<=r):
            mid = (r+l)//2
            ts,val = events[mid]
            if ts<=timestamp:
                l = mid+1
                ret =val
            else:
                r = mid-1
        return ret 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)