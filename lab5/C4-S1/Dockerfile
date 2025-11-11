FROM ubuntu:22.04
RUN apt-get update && apt-get install -y \
    openssh-client \
    openssh-server 
RUN useradd -m -s /bin/bash prueba && \
    echo 'prueba:prueba' | chpasswd && \
    usermod -aG sudo prueba
RUN mkdir -p /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && \
    echo 'AllowUsers prueba root' >> /etc/ssh/sshd_config
RUN ssh-keygen -A
WORKDIR /root
EXPOSE 22
COPY start_ssh.sh /usr/local/bin/start_ssh.sh
RUN chmod +x /usr/local/bin/start_ssh.sh
CMD ["/usr/local/bin/start_ssh.sh"]
