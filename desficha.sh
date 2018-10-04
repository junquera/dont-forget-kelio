#!/bin/bash
prev_state=$(amixer get Master| egrep -o -e '\[([^\]*)\]'| cut -d' ' -f 2 | tr -d '[' | tr -d ']' | tail -n 1)
prev_vol=$(amixer get Master| egrep -o -e '\[([^\]*)\]'| cut -d' ' -f 1 | tr -d '[' | tr -d ']' | tail -n 1)

amixer set Master 100% on
paplay ~/desficha.wav
amixer set Master $prev_vol $prev_state
