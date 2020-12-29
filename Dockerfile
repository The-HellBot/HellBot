FROM kalilinux/kali:latest
COPY hell.sh /tmp/hell.sh
WORKDIR root/HellBoy-OP
RUN /tmp/hell.sh && chmod +x /usr/local/bin/* 
