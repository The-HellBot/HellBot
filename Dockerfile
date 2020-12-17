FROM HellBoy-OP/HellBot:latest

#clonning repo 
RUN git clone https://github.com/HellBoy-OP/L/HellBot.git/root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["bash","startup.sh"]
