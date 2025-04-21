#!/bin/bash

DATA_DIR="data"

for seed in {1..20}; do
    OUTPUT_FILE="ls2_seed${seed}.out"
    for file in "$DATA_DIR"/*.in; do
        if [[ -f "$file" ]]; then
            python3 main.py -inst "$file" -alg LS2 -time 300 -seed "$seed" -outfile ls2_seed${seed}>> "$OUTPUT_FILE" 2>&1 &
        fi
    done
done
