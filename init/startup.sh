#!/bin/bash

_logo() {
    echo '
╭╮╱╭╮╱╱╭╮╭╮╭╮╱╱╱╱╭╮
┃┃╱┃┃╱╱┃┃┃┃┃┃╱╱╱╭╯╰╮
┃╰━╯┣━━┫┃┃┃┃╰━┳━┻╮╭╯
┃╭━╮┃┃━┫┃┃┃┃╭╮┃╭╮┃┃
┃┃╱┃┃┃━┫╰┫╰┫╰╯┃╰╯┃╰╮
╰╯╱╰┻━━┻━┻━┻━━┻━━┻━╯
    '
}

_CleanUp() {
    echo 'Cleaning up HellBot'
    rm -rf ./plugins && rm -rf ./* && rm -rf ./.gitignore && rm -rf ./.git
} 

_UpSource() {
    echo 'Updating HellBot With Latest Codes From HellBoy-OP/HellBot' 
    git clone https://github.com/HellBoy-OP/HellBot ./ &> /dev/null
    mkdir ./plugins
    git clone https://github.com/GhostHellboy/plugs ./Temp &> /dev/null
    cp ./Temp/plugins/*.py ./plugins ./userbot
    rm -rf ./Temp
}

_UpPip() {
    echo '~~~~ Updating Pip ~~~~' 
    pip3 install -U pip &> /dev/null
    echo '✓✓ Updated Pip ✓✓'
}

StartUp() {
    _logo
    _CleanUp
    _UpSource
    _UpPip
    mkdir ./pikabot/main_plugs
    python3 -m pikabot
}
