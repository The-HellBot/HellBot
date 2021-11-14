FROM teamvaders/hellbot:latest

RUN git clone https://github.com/The-HellBot/Plugins.git /root/hellbot

WORKDIR /root/hellbot

RUN pip install --upgrade pip 
Run pip3 install -U -r requirements.txt

ENV PATH="/home/hellbot/bin:$PATH"

CMD ["python3", "-m", "hellbot"]
      
