FROM teamvaders/hellbot:latest

RUN git clone https://github.com/TheVaders/InVade.git ./TheVaders
RUN pip install --upgrade pip
RUN pip3 install -r ./TheVaders/requirements.txt

WORKDIR ./TheVaders

CMD ["python3", "-m", "hellbot"]
