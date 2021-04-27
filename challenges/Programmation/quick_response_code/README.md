# Quick Response Code
## Challenge

Philippe XXXIV, roi de Macédoine et descendant de Philippe II, souhaiterais cacher son mot de passe sur son ordinateur pour éviter qu'on puisse facilement lui dérober. Mais pas question pour Philippe d'utiliser un gestionnaire de mot de passe (qui serait digne de garder le précieux mot de passe d'un roi après tout ?). Il décide donc d'appliquer le célèbre principe de son arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-arrière-grand-père : diviser pour mieux... enfin vous avez compris.

## Résolution

Les QR Codes ne contenant rien sont de la forme `Nothing here (id = 0x123)`
Les QR Codes contenant un bout de flag sont de la forme `Flag char 0 is "P" (id = 0x123)`, `Flag char 1 is "H" (id = 0x123)`.

J'ai volontairement rajouté un `id` random pour éviter que les QR Codes "vides" soient les mêmes.

Il faut donc retrouver les QR Codes qui contiennent un bout du flag, les ordonner et l'afficher.

```
➜  ./solve.py
```

# Flag

```
PHACK{MaaaYb3_Th1s_Waas_Overk1lL?!}
```