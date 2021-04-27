# Etsy
## Challenge

Un peu saoul après 3 panachés, ton bosse a sous-entendu que son mot de passe de session était en rapport avec l'une de ses activités favorites. Tu sais ce qu'il te reste à faire...

Format : PHACK{motdepasse}

## Résolution

```bash
unshadow passwd shadow > unshadow
john --fork=4 --wordlist=/tmp/irockyou.txt unshadow
```

## Setup

Fournir les fichiers passwd, shadow, irockyou.txt et homes-info.txt (--> files.zip).

## Flag

```
PHACK{murder!}
```