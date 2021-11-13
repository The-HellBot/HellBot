FROM teamvaders/hellbot:latest

RUN git clone https://github.com/The-HellBot/Plugins.git /root/hellbot

WORKDIR /root/hellbot

RUN pip3 install -U -r requirements.txt
    && pip install --upgrade pip

ENV PATH="/home/hellbot/bin:$PATH"

CMD ["python3", "-m", "hellbot"]
