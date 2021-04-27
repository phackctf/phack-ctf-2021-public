# Tenet
## Challenge

Fan du film Tenet de 2020 tu as désormais l'occasion dont tu rêvais d'aider ton héro préféré puisque tu viens d'intercepter une communication venant du future.

## Résolution

* Suivre le stream TCP de la conversation telnet
* Extraire le contenu de secret.txt
* Décoder (base 64) le fichier secret.txt

## Setup

**File creation**
```
docker build -t tenet-server:latest .
docker run -itd --name=tenet-server tenet-server:latest
```

```
telnet <IP> #root:iL0v3Th1sM0viE
pwd
ls -al
cd Documents
ls -al
file guide_hygiene_informatique_anssi.pdf
cat rfc854.txt
head secret.txt
cat tenet-le-film.pdf | grep tenet
```

**Challenge**
Fournir le fichier `tenet.pcapng`

## Flag

```
PHACK{d0_n0t_us3_1ns3cUr3_pR0t0c0l}
```