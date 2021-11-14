FROM teamvaders/hellbot:latest

RUN git clone https://github.com/The-HellBot/Plugins.git /root/hellbot

WORKDIR /root/hellbot

RUN -m pip install --upgrade pip -U -r requirements.txt

ENV PATH="/home/hellbot/bin:$PATH"

CMD ["python3", "-m", "hellbot"]
      
