#!/bin/bash

DATA_DIR="data"
for file in "$DATA_DIR"/*.in; do
    if [[ -f "$file" ]]; then

        python3 main.py -inst "$file" -alg LS1 -time 300 -seed 100 -outfile ls1_seed100
    fi
done
