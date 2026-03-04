class Node:
    def __init__(self):
        self.name = ""
        self.isFile = False
        self.content = []
        self.children = {}
    def insert(self,path,isFile):
        dirs = path.split("/")
        node = self
        for i in dirs[1:]:
            if i not in node.children:
                node.children[i] = Node()
            node = node.children[i]
        node.isFile = isFile
        if node.isFile:
            node.name = dirs[-1]
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
        node = self.root.search(path)
        if node is None:
            return []
        if node.isFile:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.root.insert(path,isFile=False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root.insert(filePath,isFile=True)
        node.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root.search(filePath)
        return "".join(node.content)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)