#!/bin/bash

# Buscando el numid donde se encuentra el volumen
PCM=$(amixer controls | grep Volume | awk -F , '{print $1}')
ARRAY=( amixer aplay alsamixer alsactl )

#if [ -n $1 ]; then
# printf "Se debe de usar: ./increase.sh VOL\n"; exit 1;
#fi

function check_libs () {
for i in "${ARRAY[@]}"
do
 command -v $i > /dev/null 2>&1 || { echo >&2 "No tienes instalado $i"; exit 1; }
done
}

function amixer_inst () {
 amixer cset numid=3 1
 amixer cset $1 "$2%";
}

check_libs
amixer_inst $PCM $1
alsactl store
