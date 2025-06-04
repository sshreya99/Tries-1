class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = 26 * [None] 

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        string = []
        for word in sentence.split():
            curr = self.root
            replaceStr = ""
            for i in word:
                if not curr.children[ord(i) - ord("a")] or curr.isEnd:
                    break
                curr = curr.children[ord(i) - ord("a")]
                replaceStr = replaceStr + i

            if not curr.isEnd:
                string.append(word)
            else:
                string.append(replaceStr)
        return " ".join(string)

    def insert(self, word):
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord("a")]:
                curr.children[ord(i) - ord("a")] = TrieNode()
            curr = curr.children[ord(i) - ord("a")]
        curr.isEnd = True
