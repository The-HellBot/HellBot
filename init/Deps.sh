_logo() {
    echo '
    ╔═╦╦╗───╔╗──╔╗
    ║╬╠╣╠╦═╗║╚╦═╣╚╗
    ║╔╣║═╣╬╚╣╬║╬║╔╣
    ╚╝╚╩╩╩══╩═╩═╩═╝
    '
}

_CleanUp() {
    echo 'Cleaning up HellBot'
    rm -rf ./plugins && rm -rf ./* && rm -rf ./.gitignore && rm -rf ./.git
} 

_UpSource() {
    echo 'Updating HellBot with HellBoy-OP/HellBot' 
    git clone https://github.com/HellBoy-OP/HellBot ./ &> /dev/null
    mkdir ./plugins
    git clone https://github.com/HellBoy-OP/lund ./Temp &> /dev/null
    cp ./Temp/modules/*.py ./modules && cp ./Temp/modules/resources/*.py ./userbot
    rm -rf ./Temp
}

_UpPip() {
    echo '••• Updating Pip •••' 
    pip3 install -U pip &> /dev/null
    echo '••• Updated Pip •••'
}

StartUp() {
    _logo
    _CleanUp
    _UpSource
    _UpPip
    mkdir ./userbot/main_plugs
    python3 -m userbot
}
