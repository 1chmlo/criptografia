FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    openssh-client \
    openssh-server 

RUN useradd -m -s /bin/bash prueba && \
    echo 'prueba:prueba' | chpasswd

RUN mkdir -p /var/run/sshd && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

RUN ssh-keygen -A
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
