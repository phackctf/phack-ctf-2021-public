#! /usr/bin/env python3

words_to_letter = {
"alpha" : "A",
"bravo" : "B",
"charlie" : "C",
"delta" : "D",
"echo" : "E",
"foxtrot" : "F",
"golf" : "G",
"hotel" : "H",
"india" : "I",
"juliett" : "J",
"kilo" : "K",
"lima" : "L",
"mike" : "M",
"november" : "N",
"oscar" : "O",
"papa" : "P",
"quebec" : "Q",
"romeo" : "R",
"sierra" : "S",
"tango" : "T",
"uniform" : "U",
"victor" : "V",
"whisky" : "W",
"x-ray" : "X",
"yankee" : "Y",
"zulu" : "Z",
"zero": "0",
"one": "1",
"two": "2",
"three": "3",
"four": "4",
"five": "5",
"six": "6",
"seven": "7",
"eight": "8",
"nine": "9",
"underscore": "_",
"accoladedroite": "}",
"accoladegauche": "{",
}

with open("cipher_text.txt") as f:
    lines = f.readlines()

def map_word_to_letter(line):
    for word, initial in words_to_letter.items():
        line = line.lower().replace(word.lower(), initial)
    return line


flag = ""
for line in lines:
    line = map_word_to_letter(line.strip()).replace(" ", "")
    line = map_word_to_letter(line)
    flag += line

print("The flag is %s" % flag)
