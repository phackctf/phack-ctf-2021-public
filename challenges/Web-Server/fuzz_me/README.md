# Fuzz Me
## Challenge

Votre ami vient vous voir en panique car il a perdu ses identifiants et il ne peut plus se connecter à son site préféré.  
Aidez-le à sauver la situation.

## Résolution

* Le submit du formulaire renvoie vers un `/api/login`
* On fuzz les urls en `/api` --> On trouve `/api/sessions` et `/api/user`
* On décode les sessions trouvées dans `/api/sessions` et on récupère le UUID de l'admin
* On fuzz l'url `/api/user` pour comprendre qu'il faut utiliser le paramètre UUID
* `/api/user?uuid=xxx` renvoie le login/mot de passe de l'admin
* Après connexion, on récupère le flag


## Setup

Fournir le fichier ciphered_text.txt sous le nom data.txt

## Flag

```
PHACK{th1s_1s_H0w_w3_d0_enum3r4ti0n_m4n}
```