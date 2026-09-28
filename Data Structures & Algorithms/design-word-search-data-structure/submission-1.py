class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False
        

    def addWord(self, word: str) -> None:
        root = self

        for char in word:
            if char not in root.children:
                root.children[char] = WordDictionary()
            root = root.children[char]

        root.word = True

    def search(self, word: str) -> bool:
        '''
        do dfs but we need idx and node for every level
        '''
        root = self
        length = len(word)
        found = False

        def dfs(node, idx):
            nonlocal found

            if idx == length: return node.word

            letter = word[idx]

            for nei_node in node.children:
                if nei_node == letter or letter == '.':
                    found = found or dfs(node.children[nei_node], idx+1)

            return found 

        return dfs(root, 0)

                




        
