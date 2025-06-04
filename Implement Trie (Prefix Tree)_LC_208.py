class TrieNode():
    def __init__(self):
            self.isEnd = False
            self.children = 26 * [None]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord("a")]:
                curr.children[ord(i) - ord("a")] = TrieNode()
            curr = curr.children[ord(i) - ord("a")] 
        curr.isEnd = True  

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord("a")]:
                return False
            curr = curr.children[ord(i) - ord("a")]
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if not curr.children[ord(i) - ord("a")]:
                return False
            curr = curr.children[ord(i) - ord("a")]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
