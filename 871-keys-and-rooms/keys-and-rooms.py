class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]
        while(queue):
            curr= queue.pop(0)
            edges = rooms[curr]
            visited.add(curr)
            for v in edges:
                if v not in visited:
                    queue.append(v)
        return len(rooms) == len(visited)
        
