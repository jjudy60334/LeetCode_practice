class TreeNode:
    def __init__(self):
        self.child = {}
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        self.head = TreeNode()

    def addWord(self, word: str) -> None:
        h = self.head
        for w in word:
            if w not in h.child:
                h.child[w] = TreeNode()
            h = h.child[w]
        h.end_of_word = True

    def search(self, word: str) -> bool:
        h = self.head
        ans = self._search(h, word, 0)
        return ans

    def _search(self, root, w, l):
        if l == len(w):
            return True and root.end_of_word
        if w[l] in root.child:
            return self._search(root.child[w[l]], w, l+1)
        elif w[l] == '.':
            for c in root.child:
                s = self._search(root.child[c], w, l+1)
                if s:
                    return True
            return False
        else:
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
