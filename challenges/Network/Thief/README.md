# Thief
## Challenge

Vous venez de découvrir quelque chose d'étrange en examinant un dump réseau de votre entreprise.

Analysez ce fichier et remontez l'alerte si c'est nécessaire.

## Résolution

* Récupérer toutes les trames DNS
* Extraire les noms de domaine de type *.phack.fr
* Décoder les données et reconstituer le flag

```bash
python3 solve.py
```

## Setup
**File creation**

```python3
python3 exfiltrate.py
python3 exfiltrate-noise.py
```
+ wireshark

**Challenge**
Fournir le fichier `dump.pcapng`

## Flag

```
PHACK{3xf1ltR4ti0n_thRoUgh_dNs}
```