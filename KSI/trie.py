def index_from_letter(letter):
    return ord(letter) - ord("a")

class Trie:
    def __init__(self, node=None):
        self.root = TrieNode() if node is None else node

class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = [None for _ in range(26)]
        self.accepting = False

def search(trie, word):
    return search_node(trie.root, word, 0)

def search_node(node, word, index):
    if index == len(word) and node.accepting != False:
        return node.value
    elif index == len(word) and node.accepting == False:
        return None

    if node.children[index_from_letter(word[index])] == None:
        return None

    return search_node(node.children[index_from_letter(word[index])], word, index+1)



def insert(trie, word, value):
    return insert_node(trie.root, word, value, 0)

def insert_node(node, word, value, index):
    if word == "":
        node.accepting = True
        node.value = value
        return

    # promptne se pokud uz pismeno je v listu
    if node.children[index_from_letter(word[index])] != None:

        # uloz anglicke slovo, jestli jsme se dostali na konec ceskeho slova
        if len(word)-1 == index:
            node.children[index_from_letter(word[index])].accepting = True
            node.children[index_from_letter(word[index])].value = value
            return

        # rekurzivne zavolej opet funkci s dalsim children
        return insert_node(node.children[index_from_letter(word[index])], word, value, index+1)

    # pismeno neni v listu, pridej jej tam
    node.children[index_from_letter(word[index])] = TrieNode(word[index])

    # pokud uz jsme dosli na konec ceskeho slova, uloz anglicke
    if len(word)-1 == index:
        node.children[index_from_letter(word[index])].accepting = True
        node.children[index_from_letter(word[index])].value = value
        return

    # rekurzivne zavolej funkci s nove vytvorenym pismenem
    return insert_node(node.children[index_from_letter(word[index])], word, value, index+1)

trie = Trie()

insert(trie, "aa", "test_aa")
insert(trie, "aaaa", "test_aaaa")
print(search(trie, "aa")) # test_aa

insert(trie, "ahoj", "hello")
insert(trie, "", "Whoa")

print(search(trie, "ahoj"))  # hello
print(search(trie, ""))  # Whoa
print(search(trie, "jablko"))  # None
print(search(trie, "hell"))  # None

