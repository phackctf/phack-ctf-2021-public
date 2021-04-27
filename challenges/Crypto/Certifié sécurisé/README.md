# Certifié sécurisé
## Challenge

Une de vos connaissance sur le darknet vous informe avoir réussi à s'infiltrer sur l'ordinateur de l'un des admins du CTF.
Après avoir capturé un peu de trafic réseau et récupéré quelques fichiers, la connexion a été coupée subitement.

Il semblerait qu'il était en train de travailler sur l'un des challenges du CTF.
Voyez si vous arriver à récupérer un mot de passe !

## Résolution

Dans le docker-compose.yml on voit qu'il y a une image `phackctf/challenge` qui est publique.
Il y a également la capture .pcapng effectuée par le hacker du darknet.

Il faut pull l'image et regarder ce qu'il y a dedans.
On trouve un site web basique et un certificat.

On ouvre la capture avec wireshark et on ajoute la clé privée associée au certificat dans préférences > protocole > TLS
pour activer le déchiffrement de trafic dynamique.

Dans les échanges HTTPS qui sont maintenant en clair, on retrouve un POST sur le site avec le mot de passe de l'admin.

## Setup

Fournir `stolen_data.zip`.

# Flag

```
PHACK{Th1sIsH3llOfAP4ssw0rd!}
```
