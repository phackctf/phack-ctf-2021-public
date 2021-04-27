FROM ubuntu:latest

RUN mkdir /root/Documents

COPY ciphered_text.txt /root/Documents/secret.txt
COPY Documents/guide_hygiene_informatique_anssi.pdf /root/Documents/guide_hygiene_informatique_anssi.pdf
COPY Documents/rfc854.txt /root/Documents/rfc854.txt
COPY Documents/tenet-le-film.pdf /root/Documents/tenet-le-film.pdf

RUN apt-get update && apt-get install file grep -y &&\
    DEBIAN_FRONTEND=noninteractive apt-get -y install telnetd xinetd && \
    apt-get autoremove -y && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/* && \
    echo root:iL0v3Th1sM0viE | chpasswd && \
		echo "# default: on \n \
    # description: The telnet server serves telnet sessions; it uses unencrypted username/password pairs for authentication. \n \
    service telnet \n \
    { \n \
    disable = no \n \
    flags           = REUSE \n \
    socket_type     = stream \n \
    wait            = no \n \
    user            = root \n \
    server          = /usr/sbin/in.telnetd \n \
    log_on_failure  += USERID \n \
    }" | tee -a /etc/xinetd.d/telnet && \
    rm -f /etc/securetty

ENTRYPOINT ["bash"]
CMD ["-c","xinetd -dontfork -stayalive"]
