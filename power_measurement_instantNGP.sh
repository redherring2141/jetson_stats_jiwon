#!/bin/bash

# File to store the tegrastats output
TEGRSTATS_OUTPUT_FILE="tegrastats_output.log"



# for SET in DeepBlending
# do
#     for DATA in drjohnson playroom
#     do
#         python3 ./tegrastats_instantNGP.py $SET $DATA
#     done
# done

# for SET in Tanks_and_Temples
# do
#     for DATA in train truck
#     do
#         python3 ./tegrastats_instantNGP.py $SET $DATA
#     done
# done

for SET in MipNeRF360
do
    #for DATA in bicycle bonsai counter flowers garden kitchen
    for DATA in bicycle bonsai counter flowers garden kitchen room stump treehill
    do
        python3 ./tegrastats_instantNGP.py $SET $DATA
    done
done
