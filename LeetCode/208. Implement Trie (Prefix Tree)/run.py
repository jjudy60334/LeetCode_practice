
class TreeNode:
    def __init__(self):
        self.child = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:
        h = self.head
        for w in word:
            if w not in h.child:
                h.child[w] = TreeNode()
            h = h.child[w]
        h.end_of_word = True

    def search(self, word: str) -> bool:
        h = self.head
        for w in word:
            if w not in h.child:
                return False
            h = h.child[w]
        return h.end_of_word

    def startsWith(self, prefix: str) -> bool:
        h = self.head
        for p in prefix:
            if p not in h.child:
                return False
            h = h.child[p]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
