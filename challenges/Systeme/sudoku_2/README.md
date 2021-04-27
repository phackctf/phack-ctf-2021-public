# Sudoku 2
## Challenge

## Résolution

```
CVE-2019-18634 (pwfeedback) --> https://www.exploit-db.com/exploits/48052
CVE-2021-3156 (Baron Samedit) --> possible mais pas testé sous Alpine
```

## Setup

```
docker-compose up --build -d
```

**Port :** 22

**Configuration challenge**

* ssh : `padawan@sudoku2.phack.fr`
* Mdp : `padawan`


## Flag

```
PHACK{*_****_****_****_***_**_*_****_***}
```