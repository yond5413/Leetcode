class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]
        while queue:
            curr = queue.pop()
            visited.add(curr)
            for i in rooms[curr]:
                if i not in visited:
                    queue.append(i)
        return len(rooms) == len(visited)
