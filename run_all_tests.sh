#!/bin/bash

DATA_DIR="data"
for file in "$DATA_DIR"/*.in; do
    if [[ -f "$file" ]]; then

        python3 main.py -inst "$file" -alg Approx -time 60
    fi
done
