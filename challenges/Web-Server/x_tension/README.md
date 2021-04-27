# X Tension
## Challenge

Votre entreprise est victime d'un méchant ransomware.

Heureusement Sophie du marketing a développé un site pour récupérer les fichiers chiffrés.  
En tant qu'expert en sécurité vous jetez un oeil pour vous faire votre avis.

## Résolution

Utiliser le site https://crxextractor.com/ pour récupérer le code source de l'extension.
Le flag correspond à la clé AES qu'on trouve dans les sources.

## Setup

Fournir le fichier ciphered_text.txt sous le nom data.txt

```
docker-compose up --build -d
```

## Flag

```
PHACK{CRX_F1l3_R3v3rs1nG}
```