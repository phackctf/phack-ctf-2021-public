# Checkmate
## Challenge

Trois semaines avant le CTF, vous avez eu accès à un amuse bouche.

Format du flag : PHACK{<md5_du_fichier_en_minuscules>}

## Résolution

Il faut commencer par cracker le mot de passe de l'archive.  
On télécharge une WL des villes de france, puis :

```
➜  fcrackzip -D -p /tmp/out -u challenge.tar.gz.zip

PASSWORD FOUND!!!!: pw == briare
```

On retrouve ensuite un fichier qui est en réalité une partie d'échecs au format PGN, avec des caractères manquants.  
On rejoue la partie avec les seuls coups possibles étant donné les coups qui nous sont donnés.  

```
e4.e5.Nf3.Nc6.d4.exd4.Nxd4.Nxd4.Qxd4.Nf6.e5.Nh5.g4.f6.gxh5.fxe5.Qxe5+.Be7.Nc3.d6.Qe4.Bf5.Qxf5.Rf8.Qe4.h6.Bc4.Qd7.O-O.c5.Re1.b6.Bb5.Qxb5.Qxe7#
e4.e5.Nf3.Nc6.d4.exd4.Nxd4.Nxd4.Qxd4.Nf6.e5.Nh5.g4.f6.gxh5.fxe5.Qxe5+.Be7.Nc3.d6.Qe4.Bf5.Qxf5.Rf8.Qe4.h6.Bc4.Qd7.Kd1.c5.Re1.b6.Bb5.Qxb5.Qxe7#
e4.e5.Nf3.Nc6.d4.exd4.Nxd4.Nxd4.Qxd4.Nf6.e5.Nh5.g4.f6.gxh5.fxe5.Qxe5+.Be7.Nc3.d6.Qe4.Bf5.Qxf5.Rf8.Qe4.h6.Bc4.Qd7.Kd2.c5.Re1.b6.Bb5.Qxb5.Qxe7#
```

Puis on résoud :

```
➜  echo -n $GAME | md5sum 
➜  echo -n $GAME > out.pgn && md5sum out.pgn
```

## Setup

**Create**

```
$ make
```

**Solutions**

```
$ make solve
880fb53abb202e8d8330484769ff5cff  solution-0
cb51e1b764c10a01c5983e99f3d8d386  solution-1
dfaeae895affceded666b09df2e763b1  solution-2
```

**Clean**

```
$ make clean
```

## Flag

```
PHACK{880fb53abb202e8d8330484769ff5cff}
PHACK{cb51e1b764c10a01c5983e99f3d8d386}
PHACK{dfaeae895affceded666b09df2e763b1}
```