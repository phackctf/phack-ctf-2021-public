echo -n "Tm90aGluZyB5ZXQu" | base64 -d > /tmp/challenge/flag.txt
readlink /proc/$$/exe
curl -H "Authorization: Token $CTFD_TOK" https://ctf.phack.fr/api/v1/teams
cd /tmp/challenge
ls
cat cert/phack.{key,crt}
./docker-build-push.sh
shred -zuvf cert/phack.*
cd ~
ls
vi docker-compose.yml
docker-compose up && docker-compose rm -fsv
echo "127.0.0.1 certificate.phack.fr" | sudo tee -a /etc/hosts
curl -I -v certificate.phack.fr
tail -f /tmp/debug.ssl
cat /tmp/debug.ssl | grep ssl_decrypt_pre_master
ls
vi fun.c
chmod +x run-me && ./run-me
htop
ps -ef | grep -i virus
sudo pkill sup3rVirus