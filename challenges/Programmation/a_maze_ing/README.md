# A-MAZE-ING
## Challenge

Un étrange serveur souhaite vous mettre à l'épreuve. Soyez à la hauteur.

## Résolution

Une requête sur `/` nous apprend que nous sommes M. x et que nous devons récupérer le contenu du coffre de la banque en 5 secondes.
On apprend également que les routes disponibles sont :

```
| Route  | Method |
|--------|--------|
| /      | GET    |  <-- Help
| /chall | GET    |  <-- Get maze
| /chall | POST   |  <-- Send solution
| /flag  | GET    |  <-- Troll
```

Une requête `GET` sur `/chall` renvoie une réponse de la forme :

```
{
    "token" : "b49d6239439a42ebacafc0b239778c60", 
    "solveMe" : "######################x      #   #       ######## # # # ########       # # #       ## ####### # ####### ## #   #   #   #     ## # # # ##### # ### ##   # # #     #   # ###### # # ##### # ####   #   # # #   #   ## # ##### # # ##### ## # #     # # # #   ## # # ##### # # # #### # #     #     #   ## ####### ##### ### ##       #     #   # ## # ######### ##### ## #     #   #       ## ##### # # ####### ##     #   #        $######################"
}
```

Il faut comprendre que `token` est un identifiant de "partie" et `solveMe` un labyrinthe en ASCII.

```
#####################
#x      #   #       #
####### # # # #######
#       # # #       #
# ####### # ####### #
# #   #   #   #     #
# # # # ##### # ### #
#   # # #     #   # #
##### # # ##### # ###
#   #   # # #   #   #
# # ##### # # ##### #
# # #     # # # #   #
# # # ##### # # # ###
# # #     #     #   #
# ####### ##### ### #
#       #     #   # #
# # ######### ##### #
# #     #   #       #
# ##### # # ####### #
#     #   #        $#
#####################
```

On tente un `POST` sur `/chall` et on se laisse guider par les messages d'erreur, jusqu'à trouver le bon format.

Pour résoudre le challenge il faut renvoyer le token reçu et une suite valide de `↑↓←→` pour résoudre le labyrinthe et récupérer le flag.

```
{
    "token" : "b49d6239439a42ebacafc0b239778c60"
    "solution" : "→→→→→→↓↓→ [..]"
}
```

# Setup

```
docker-compose up -d --build
```

# Flag

```
PHACK{M4zEs_4Re_7rUly_4m@zIng}
```