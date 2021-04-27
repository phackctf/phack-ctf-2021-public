FROM alpine:edge

# ---------------
# Build machine
# ---------------
RUN apk update

RUN apk add openssh --no-cache
RUN apk add openrc --no-cache
RUN apk add zip --no-cache
RUN apk add bash --no-cache
RUN apk add python3 --no-cache
RUN rm  -rf /tmp/* /var/cache/apk/*

RUN rc-update add sshd
RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key

ADD docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# ---------------
# Build challenge
# ---------------
ADD motd /etc/motd

RUN adduser --home /home/padawan --shell /bin/bash -S padawan
RUN adduser --home /home/master --shell /bin/bash -S master

RUN echo 'root:umkqhv8FIC2fiRTWcco9MVwo2z' | chpasswd
RUN echo 'padawan:padawan' | chpasswd
RUN echo 'master:umkqhv8FIC2fiRTWcco9MVwo2z' | chpasswd

ADD note.txt /home/padawan/note.txt
RUN chown padawan /home/padawan/note.txt
RUN chmod 400 /home/padawan/note.txt

ADD flag.txt /home/master/flag.txt
RUN chown master /home/master/flag.txt
RUN chmod 400 /home/master/flag.txt

RUN chown master /usr/bin/python3
RUN chmod u+s /usr/bin/python3


EXPOSE 22
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["/usr/sbin/sshd","-D"]
