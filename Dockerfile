FROM python:3.9.2
RUN chmod +x /usr/local/bin/*
RUN wget https://raw.githubusercontent.com/HellBoy-OP/HellBot/test/KRAKEN/deploy.sh
RUN sh deploy.sh
WORKDIR /root/userbot/
CMD ["bash", "KRAKEN/start.sh"]
