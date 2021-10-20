FROM teamvaders/hellbot:latest

COPY . .

RUN git clone https://github.com/TheVaders/InVade.git ./TheVaders
RUN pip install --upgrade pip
RUN pip3 install -r ./requirements.txt
RUN mv ./Hellbot ./TheVaders

WORKDIR ./TheVaders

CMD ./Hellbot
