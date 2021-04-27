import string

SOLUTION = "C'est bravo ! En hommage au meilleur avocat de notre generation, le flag est marShallEriKSen. J'espere que le jeu de mot vous aura plu (\"A vaut K\")!"

table = { chr( ord('a') + x ):chr( ord('a') + ((x + 10) % 26) ) for x in range(26) }

out = ''

for c in SOLUTION:

    if c in string.ascii_lowercase:
        out += table[c]
    elif c in string.ascii_uppercase:
        out += table[c.lower()].upper()
    else:
        out += c

print(out)
