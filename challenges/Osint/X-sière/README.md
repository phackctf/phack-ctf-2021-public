# X-sière
## Challenge

En revenant de votre croisière en amoureux, votre femme vous met au défit de vous souvenir du nom du bateau sur lequel vous avez naviguez pendant 3 semaines.
C'était un de ces énormes paquebots mais impossible pour vous de vous en rappeler.

Heureusement, vous vous rappelez que vous aviez pris cette photo après avoir marcher 300 mètres en débarquant du bateau.
Peut-être que cela pourra aider votre mémoire ?

NB: Le flag est au format PHACK{<NOMDUBATEAUSANSESPACEETENMAJUSCULE>}

## Résolution

En regardant dans les metadata de l'image on récupère des coordonnées GPS :

```
➜  exiftool x-sière.jpg 
[...]
GPS Position : 36 deg 26' 37.34" N, 28 deg 13' 52.12" E
```

Il faut ensuite se rendre sur google map et chercher un gros bateau.

## Setup

Fournir le fichier `x-sière.jpg`

## Flag

```
PHACK{CELEBRITYINFINITY}
```
