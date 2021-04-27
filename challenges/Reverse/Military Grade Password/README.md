# Military Grade Password
## Challenge

Fraichement arrivé dans l'armée, vous avez déjà perdu votre identifiant pour accéder à l'intranet.
Dépêchez-vous de le retrouver avant que quelqu'un ne s'en aperçoive !

## Résolution

Il faut reverse le binaire et résoudre les multiples équations avec un SAT solver comme z3.

## Setup

```
➜  CFLAGS="-O3" make main && strip ./main
```

## Flag

```
PHACK{q4Eo-eyMq-1dd0-leKx}
```