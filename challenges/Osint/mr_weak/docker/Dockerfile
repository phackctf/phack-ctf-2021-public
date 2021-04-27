FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y && apt-get install -y openssh-server
RUN useradd -m johnnyweak  -s /bin/bash
RUN mkdir -p /home/johnnyweak/.ssh
COPY id_rsa.pub /home/johnnyweak/.ssh/authorized_keys
RUN chown -R johnnyweak:johnnyweak /home/johnnyweak/.ssh
 
ADD motd /etc/motd

ADD docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ADD flag.txt /home/johnnyweak/flag.txt
RUN chown johnnyweak: /home/johnnyweak/flag.txt
RUN chmod 400 /home/johnnyweak/flag.txt

RUN echo 'root:umkqhv8FIqsC2fiqsdqsdz2' | chpasswd
RUN echo 'johnnyweak:umkqhv8FIC2flsdz2' | chpasswd

ADD sshd_config /etc/ssh/sshd_config
RUN chmod 644 /etc/ssh/sshd_config

EXPOSE 22
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["/usr/sbin/sshd","-D"]
