# Git de France
## Challenge

J'ai perdu mon flag quelque part dans ce projet.. Pas moyen de remettre la main dessus :(

## Résolution

Il faut aller sur la branche `search-engine`, au commit `9ed72103b0a0625e63163f0768da0c776e86e597`, le flag se trouve dans le fichier `search copy.php`.

```bash
# Pour chaque branche de repo
➜  git log | grep "^commit " | cut -d ' ' -f2 | while read commit; do git show $commit | grep "PHACK"; done

# Solution proposée par @ribt
➜  git reflog -p | grep PHACK
```

## Flag

```
PHACK{Z2l0IGNvbW1pdCAtbSAiRXogZ2l0IDp0YWRhOiI=}
```