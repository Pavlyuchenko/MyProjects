import string

translation_dict = dict([('a', '.-'), ('b', '-...'), ('c', '-.-.'), ('d', '-..'), ('e', '.'), ('f', '..-.'), ('g', '--.'), ('h', '....'), ('i', '..'), ('j', '.---'), ('k', '-.-'), ('l', '.-..'), ('m', '--'), ('n', '-.'), ('o', '---'), ('p', '.--.'), ('q', '--.-'), ('r', '.-.'), ('s', '...'), ('t', '-'), ('u', '..-'), ('v', '...-'), ('w', '.--'), ('x', '-..-'), ('y', '-.--'), ('z', '--..'), (' ', ''), ('/', '-..-.'), ('-', '-....-'), ('.', '.-.-.-'), (',', '--..--'), (' ', ''), ("1", ".----"), ("2", "..---"), ("3", "...--"), ("4", "....-"), ("5", "....."), ("6", "-...."), ("7", "--..."), ("8", "---.."), ("9", "----."), ("0", "-----")])
alphabet = {}
morse = {}

for key, value in translation_dict.items():
    alphabet[key] = value
    alphabet[value] = key

def encode(plaintext):
    plaintext = plaintext.lower()
    morse_text = ""
    for char in plaintext:
        morse_text += translation_dict[char] + "/"
    morse_text += "//"
    return morse_text

def decode(morse_text):
    morse_text = morse_text[0:len(morse_text)-3]
    morse_array = morse_text.split("/")
    plain_text = ""

    for i in range(len(morse_array)):
        current_element = morse_array[i]
        for key, value in translation_dict.items():
            if current_element == value:
                plain_text += key

    return plain_text

print(decode(encode("tezke troleni")))
print(decode(encode("garant rocniku se predem omlouva za zpusobene psychicke potize.")))
print(decode(encode("do translation dict jsou pridany vsechny specialni znaky a cisla, ktera budete potrebovat.")))
print(encode("ab c")) # .-/-...//-.-.///

