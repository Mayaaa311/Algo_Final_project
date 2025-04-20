#!/bin/bash

DATA_DIR="data"
for file in "$DATA_DIR"/*.in; do
    if [[ -f "$file" ]]; then

        python3 main.py -inst "$file" -alg LS1 -time 600 -seed 80 -outfile ls1_seed80_time600
    fi
done
