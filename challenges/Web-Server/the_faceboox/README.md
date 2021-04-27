# TheFaceboox
## Challenge

Un jeune étudiant prétentieux d'Harvard se vante d'avoir lancé TheFaceboox, un réseau social qui sera bientôt plus populaire que mySpoox, votre site de coeur.

Prouvez au monde entier que son site ne vaut pas un clou en prenant le contrôle de son compte !

## Résolution

Il faut trouver trouver le compte press "demo / demo".  
En modifiant le cookie et en suivant les erreurs on se rend compte qu'on peut passer de manière horizontale d'un compte press à un compte student.

Une fois avec le premier compte student, un test de recherche fait ressortir une référence à une base mysql que l'on peut télécharger.
On peut craker les mdp des utilisateurs, jusqu'à celui d'une journaliste qui a recu en message privé le mdp de son compte press.

Ce compte press a le même id que celui de mark on peut donc switch sur son compte.

## Setup

```
docker-compose up --build -d
```

## Flag

```
PHACK{1Nt3rnet_C'e7ait_m1euX_Av@nt!:(}
```