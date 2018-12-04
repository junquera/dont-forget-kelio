#!/bin/bash
prev_state=$(amixer -c 1 get Master | egrep -o -e '\[([^\]*)\]'| cut -d' ' -f 3 | tail -1 | sed -nE "s/\[([^\)]*)\]/\1/p")
prev_vol=$(amixer -c 1 get Master | egrep -o -e '\[([^\]*)\]'| cut -d' ' -f 1 | tail -1 | sed -nE "s/\[([^\)]*)\]/\1/p")

amixer -c 1 set Master 100% on;
paplay $(pwd)/ficha.wav;
amixer -c 1 set Master $prev_vol $prev_state;
