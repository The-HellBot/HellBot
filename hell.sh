
#!/usr/bin/env bash 


set -euo pipefail


echo '
╔╗╔╦═╦╗╔╗╔══╦═╦══╗
║╚╝║╦╣║║║║╔╗║║╠╗╔╝
║╔╗║╩╣╚╣╚╣╔╗║║║║║
╚╝╚╩═╩═╩═╩══╩═╝╚╝
'
export DEBIAN_FRONTEND=noninteractive
export TZ=Asia/Kolkata
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

apt-get update && apt upgrade -y 
apt-get install -y --no-install-recommends \
    coreutils \
    bash \
    nodejs \
    bzip2 \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    util-linux \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    musl \
    neofetch \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    openssl \
    mediainfo \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    libreadline-dev \
    zipalign \
    sqlite \
    ffmpeg \
    libsqlite3-dev \
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    libfreetype6-dev \
    procps \
    policykit-1\
    unzip
apt autoremove --yes

pip3 install --upgrade pip setuptools 
git clone https://github.com/HellBoy-OP/HellBot ./
mkdir bin && mkdir userbot/plugins
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb
rm -f ./google-chrome-stable_current_amd64.deb
wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && mv -f chromedriver /usr/bin/ && rm -f ./chromedriver_linux64
pip3 install -r requirements.txt 

echo '
╔╗╔╦═╦╗╔╗╔══╦═╦══╗
║╚╝║╦╣║║║║╔╗║║╠╗╔╝
║╔╗║╩╣╚╣╚╣╔╗║║║║║
╚╝╚╩═╩═╩═╩══╩═╝╚╝ 
• Wait While update is being pushed to Heroku
• Turn your Dynos on 
If You face any issue then contact Admins 
at @HellBot_Official_Chat
'
