FROM alpine:edge

# ---------------
# Build machine
# ---------------
RUN apk update

RUN apk add busybox-suid --no-cache
RUN apk add openssh --no-cache
RUN apk add openrc --no-cache
RUN apk add python3 --no-cache
RUN apk add py3-pip --no-cache
RUN apk add bash --no-cache
RUN apk add sqlite --no-cache
RUN apk add py3-lxml --no-cache
RUN apk add busybox-initscripts --no-cache
RUN apk add supervisor --no-cache
RUN rm  -rf /tmp/* /var/cache/apk/*


RUN rc-update add sshd
RUN rc-update add crond
RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key

ADD docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r  /tmp/requirements.txt
RUN rm -rf /tmp/requirements.txt

ADD supervisord.conf /etc/supervisord.conf

# ---------------
# Build challenge
# ---------------
ADD motd /etc/motd

RUN adduser --home /home/teacher --shell /bin/bash -S teacher
RUN adduser --home /home/rector --disabled-password -S rector

RUN echo 'teacher:teacher' | chpasswd
RUN echo 'root:umkqhv8FIC2fiRTWcco9MVwo2zaz22sdq' | chpasswd
RUN echo 'rector:umkqhv8FIC2fiRTWcco9MVwo2zaz222' | chpasswd

ADD note.txt /home/teacher/note.txt
RUN chown rector:root /home/teacher/note.txt
RUN chmod 444 /home/teacher/note.txt

ADD flag.txt /home/rector/flag.txt
RUN chown rector:root /home/rector/flag.txt
RUN chmod 400 /home/rector/flag.txt

ADD grade_integrator.py /home/rector/integrator.py
RUN chown rector:root /home/rector/integrator.py
RUN chmod 540 /home/rector/integrator.py

ADD template.xml /home/teacher/template.xml
RUN chown root:root /home/teacher/template.xml
RUN chmod 444 /home/teacher/template.xml

RUN touch /home/rector/integrator.log
RUN chown rector:root /home/rector/integrator.log
RUN chmod 644 /home/rector/integrator.log

RUN mkdir /home/teacher/evaluations
RUN chown teacher:root /home/teacher/evaluations
RUN chmod 777 /home/teacher/evaluations

ADD template.xml /home/teacher/evaluations/eval.xml
RUN chown rector:root /home/teacher/evaluations/eval.xml
RUN chmod 644 /home/teacher/evaluations/eval.xml

ADD crontab /etc/crontabs/rector
RUN chmod 600 /etc/crontabs/rector


EXPOSE 22
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["supervisord" , "--nodaemon", "-c","/etc/supervisord.conf"]
