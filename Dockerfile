FROM kalilinux/kali:latest
COPY hellbot.sh /tmp/hellbot.sh
WORKDIR root/HellBoy-OP
RUN /tmp/hellbot.sh && chmod +x /usr/local/bin/* 
