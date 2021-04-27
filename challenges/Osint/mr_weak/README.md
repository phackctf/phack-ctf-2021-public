# Mr Weak
## Challenge

Un nouveau est arrivé dans l'équipe sécu de votre entreprise mais sa tête ne vous revient pas. Vous décidez de faire votre propre petite enquête sur lui pour en savoir plus.

Son nom : Johnny Weak

## Résolution

Pour ce genre de challenge, un outils comme sherlock peut s'avérer très utile.

```
Aller sur  https://github.com/johnnyweak
Lire le .bash_history
Récupérer la clé SSH
ssh -p 6969 -i id_rsa johnnyweak@secr3t-pr0j3cts.phack.fr
```

## Setup

```docker-compose up --build -d```

* **Domain name :** `secr3t-pr0j3cts.phack.fr`
* **Port :** 6969

## Flag
```
PHACK{th3y_k1ll3d_j0hN_wicK_s_d0g!}
```