#!/bin/bash

# File to store the tegrastats output
TEGRSTATS_OUTPUT_FILE="tegrastats_output.log"

for DATA in bicycle bonsai counter flowers garden kitchen room stump treehill
do
    python3 ./tegrastats_3DGS.py $DATA
done

conda activate instantNGP

for SET in MipNeRF360
do
    for DATA in bicycle bonsai counter flowers garden kitchen room stump treehill
    do
        python3 ./tegrastats_instantNGP.py $SET $DATA
    done
done