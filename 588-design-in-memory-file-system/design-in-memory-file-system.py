class Node:
    def __init__(self):
        self.name = ""
        self.isFile = False
        self.content = []
        self.children = {}
    def insert(self,path,isFile):
        node = self
        path_entry = path.split("/")
        for entry in path_entry[1:]:
            if entry not in node.children:
                node.children[entry] = Node()
            node = node.children[entry]
        node.isFile = isFile
        if node.isFile:
            node.name = path_entry[-1]
        return node
    def search(self,path):
        node = self
        if path == "/":
            return node
        path_entry = path.split("/")
        for entry in path_entry[1:]:
            if entry not in node.children:
                return None
            node = node.children[entry]
        return node
class FileSystem:

    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        res = self.root.search(path)
        if not res:
            return []
        if res.isFile:
            return [res.name]
        return sorted(res.children.keys())

    def mkdir(self, path: str) -> None:
        self.root.insert(path,False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        res = self.root.insert(filePath,True)
        res.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        return "".join(self.root.search(filePath).content)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)