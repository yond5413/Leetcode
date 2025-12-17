class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]
        while (stack):
            curr = stack.pop()
            visited.add(curr)
            for i in rooms[curr]:
                if i not in visited:
                    stack.append(i)
            
        return len(rooms) == len(visited)