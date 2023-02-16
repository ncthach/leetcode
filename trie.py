from typing import Optional

class Trie(dict):
    ENDING_CHAR = -1
    def __init__(self):
        self.count = 0

    def _search(self, word: str, index: int) -> Optional["Trie"]:
        # print("search", self, word, index)
        if index == len(word):
            return self
        if len(self) == 0:
            return None
        char = word[index]
        return self.get(char, Trie())._search(word, index + 1)

    def _add(self, word: str, index: int) -> None:
        # assume no duplicates
        self.count += 1
        if index == len(word):
            leaf = Trie()
            leaf.count += 1
            self[self.ENDING_CHAR] = leaf
            return

        char = word[index]
        if char not in self:
            self[char] = Trie()
        self[char]._add(word, index + 1)

    def add(self, word: str) -> None:
        return self._add(word, 0)

    def search(self, word: str) -> Optional["Trie"]:
        return self._search(word, 0)

    def has_word(self, word: str) -> bool:
        return (self.ENDING_CHAR in self._search(word, 0))

    def count_prefix(self, prefix: str) -> int:
        prefix_trie = self.search(prefix)
        if prefix_trie is None:
            return 0
        return prefix_trie.count


class TestTrie(dict):
    def addElement(self, key, val):
        self[key] = val

    def getElement(self, key, default_val = None):
        return self.get(key, default_val)


x = TestTrie()
x.addElement('a', 1)
print(x.getElement('a'))
print(x.getElement('b'))
print(x.getElement('b', 'default'))

x = Trie()
x.add("apple")
print(x)
print(x.search("apple"))
print(x.search("app"))
x.add("app")
print(x)
print(x.count_prefix("a"))
print(x.count_prefix("ap"))
print(x.count_prefix("app"))
print(x.count_prefix("appl"))
print(x.count_prefix("apple"))
print(x.count_prefix("apple1"))
print(x.count_prefix("b"))
x.add("hello")
print(x.count_prefix("h"))
print(x.count_prefix("he"))
print(x.count_prefix("hel"))
print(x.count_prefix("hell"))
print(x.count_prefix("hello"))
print(x.count_prefix("b"))
print(x.count_prefix("hello1"))
print(x.has_word("a"))
print(x.has_word("ap"))
print(x.has_word("app"))
print(x.has_word("appl"))
print(x.has_word("apple"))
print(x.has_word("apple1"))
print(x.has_word("h"))
print(x.has_word("he"))
print(x.has_word("hel"))
print(x.has_word("hell"))
print(x.has_word("hello"))
print(x.has_word("b"))
print(x.has_word("hello1"))

print(x.search(""))

