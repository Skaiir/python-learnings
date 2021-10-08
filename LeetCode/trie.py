class Node:
    def __init__(self):
        self.subnodes = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        self.sub_insert(word, self.root)
        
    def sub_insert(self, word: str, node: Node):
        if len(word) == 0:
            node.subnodes['*'] = None
            return
        if word[0] not in node.subnodes:
            node.subnodes[word[0]] = Node()
        self.sub_insert(word[1:], node.subnodes[word[0]])

    def search(self, word: str) -> bool:
        return self.sub_search(word, self.root)

    def sub_search(self, word: str, node: Node) -> bool:
        if len(word) == 0:
            return '*' in node.subnodes
        return self.sub_search(word[1:], node.subnodes[word[0]]) if word[0] in node.subnodes else False  

    def startsWith(self, prefix: str) -> bool:
        return self.sub_startsWith(prefix, self.root)

    def sub_startsWith(self, word: str, node: Node) -> bool:
        if len(word) == 0:
            return True
        return self.sub_startsWith(word[1:], node.subnodes[word[0]]) if word[0] in node.subnodes else False  


trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")   