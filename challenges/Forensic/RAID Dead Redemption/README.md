# RAID Dead Redemption
## Énoncé

Vous travaillez à la brigade spéciale du service cyberdéfense de la gendarmerie de Montargis.

Les disques dur d'une femme ont été saisis et vienne de vous être transmis. Elle est suspectée d'avoir téléchargé de nombreux fichiers PNG et JPG dont elle n'avait pas la propirété intellectuelle. Mais il semblerait qu'elle ait eu le temps de supprimer une partie des preuves avant l'intervention. Faites de votre mieux pour en extraire le maximum !

Le manuel d'un logiciel suspect tournant sur l'ordinateur a également été retrouvé et vous a été transmis pour vous guider dans votre enquête.

## Résolution

Il faut lire la "notice technique" du Mastok 3000 pour comprendre qu'il s'agit d'un système de RAID 5.
Il y est précisé que la première parité se fait sur le disque `N`, donc ici `3`.
On sait également qu'il s'agit de `Left-Asynchronous`, le placement des données s'effectuera donc de la façon suivante :

| Disque 1 | Disque 2 | Disque 3 |
|----------|----------|----------|
| 1        | 2        | PARITY   |
| 3        | PARITY   | 4        |
| PARITY   | 5        | 6        |
| 7        | 8        | PARITY   |
| 9        | PARITY   | 10       |
| PARITY   | 11       | 12       |

Enfin le `chunk size` est de 1 octet. La ligne 1 du tableau correspond donc aux 2 premiers octets du fichier + parité.

Il faut tout d'abord restaurer `Disque 2` qui fait 0 octets.

```
Disque 2 = Disque 1 ⊕ Disque 3
```

> Il serait également possible de ne restaurer que les données utiles

Une fois le disque 2 récupéré, il faut extraire les données utiles dans un seul et même bloc qui contient tous les fichiers mis bout à bout :

```
raw = file1.jpg:file2.png:file3.png:file4.png
```

Il faut enfin utiliser les "magic number" des fichiers PNG et JPEG (respectivement `89 50 4E 47 0D 0A 1A 0A` et `FF D8 FF E0`) pour découper les fichiers et retrouver le flag.

On peut le faire manuellement ou s'appuyer sur des outils comme foremost.

## Setup

Fournir `files.zip` et la notice du Mastok 3000.

## Flag

```
PHACK{R41d_1s_N1cE_7hANk_U2_m4s7ok_3000!!}
```