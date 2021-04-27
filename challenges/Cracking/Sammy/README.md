# Sammy
## Challenge

Le grand "[Elon](https://fr.wikipedia.org/wiki/Elon_Musk)", le seul et unique, a été compromis.  
Retrouve son mot de passe pour accéder à son portefeuilles de Bitcoin.

Attention, c'est un homme intelligent: son mot de passe ne se trouve pas dans les dictionnaires communs.

Format : PHACK{motdepasse}

## Résolution

```bash
sam2dump2 ./system ./sam > hash.txt
john --fork=4 --rules --format=nt hash.txt --wordlist=my-custom-elon-wordlist.txt
```

## Setup

Fournir les fichiers sam et system (--> sammy.zip)

## Flag

```
PHACK{Tesla1971}
```