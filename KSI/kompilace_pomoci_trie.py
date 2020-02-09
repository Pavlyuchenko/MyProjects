
def index_from_letter(letter):
    return ord(letter) - ord("a")


class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = [None for _ in range(26)]
        self.accepting = False


class Trie:
    def __init__(self, node=None):
        self.root = TrieNode() if node is None else node


def search(trie, word):
    """Returns value associated with word, or None if word is not in trie."""
    node = trie.root
    for letter in word:
        if node is None:
            return None
        node = node.children[index_from_letter(letter)]
    if node is not None and node.accepting:
        return node.value
    return None


def insert(trie, word, value):
    """Inserts word and its value this trie."""
    node = trie.root
    for letter in word:
        index = index_from_letter(letter)
        if node.children[index] is None:
            node.children[index] = TrieNode()
        node = node.children[index]
    node.accepting = True
    node.value = value


def compress_output(wordlist): # wordlist je set
    output = ""
    print(wordlist)
    # todo: napis sem tvuj program
    return output

def decompress_output(content): # content je string
    wordlist = set()
    # todo: napis sem tvuj program
    return wordlist

def load_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

def output_file(content, filename="default_output_name.txt"):
    with open(filename,"w+") as f:
        f.write(content)

def plaintext_to_wordlist(lines):
    output = set()
    for x in lines:
        current_word = x.strip().lower()
        if len(current_word) == 0:
            continue
        if current_word.isalpha() == False:
            continue
        output.add(current_word)
    return output


# print(plaintext_to_wordlist('a, aa, aaa, aah, aahed, aahing, aahs, aal, aalii, aaliis, aals, aam, aani, aardvark, aardvarks, aardwolf, aardwolves, aargh, aaron, aaronic, aaronical, aaronite, aarrgh, aarrghh, aaru, aas, aasvogel, aasvogels, ab, aba, ababdeh, ababua, abac, abaca, abacay, abacas, abacate, abacaxi, abaci, abacinate, abacination'))
print(compress_output(plaintext_to_wordlist("tos")))
st = {"asd", "Adb"}

print(st)

'''
a
aa
aaa
aah
aahed
aahing
aahs
aal
aalii
aaliis
aals
aam
aani
aardvark
aardvarks
aardwolf
aardwolves
aargh
aaron
aaronic
aaronical
aaronite
aaronitic
aarrgh
aarrghh
aaru
aas
aasvogel
aasvogels
ab
aba
ababdeh
ababua
abac
abaca
abacay
abacas
abacate
abacaxi
abaci
abacinate
abacination
'''
