# Android Cloud
## Challenge

Un service américain propose de se débarasser définitivement de son smartphone
grâce à sa nouvelle plateforme de AaaS (Android as a Service).

Mais méfiant de nature, vous décidez d'aller vérifier par vous même que la
sécurité correspond à vos standards.

## Résolution

La note bas de page est un lien vers le fichier `backup.php`.

Grâce au code, on comprend qu'une archive de backup de la mémoire du téléphone
se trouve dans `./dev-backups/backup@03-10-2020.zip`.

Une fois téléchargé, on récupère le fichier `/android/data/system/gesture.key` et on en extrait
le sha1 du schéma de déverouillage.

Vu le faible nombre de possibilités, un simple bruteforce suffira à retrouver la séquence de déverrouillage : 1-5-2-4-8-7-6-9.

## Setup

```
➜  docker-compose up -d --build
```

## Flag

```
PHACK{T4ke_c4rE_oF_Ur_B4cKupS!}"
```
