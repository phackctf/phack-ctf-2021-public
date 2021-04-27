# Alter Egg-o
## Challenge

L'agent Smith de la HSA (Hack Secret Agency) a retiré trop rapidement la clé USB de son PC (ce n00b !!). La preuve qu'il voulait vous montrer semble corrompue.

Montrer lui que vous pouvez lui sauver la mise et récupérer ce fichier.

## Résolution

Le magic-number a été modifié.

Ouvrir l'image avec un éditeur hexadécimal et modifier les premiers bytes avec `89 50 4E 47`

## Setup

Fournir le fichier altered.png

## Flag

```
PHACK{ju5t_ch4ng3d_a_m4gic_nUmb3R_i5_i7_b4d?}
```