#!/bin/bash

# File to store the tegrastats output
TEGRSTATS_OUTPUT_FILE="tegrastats_output.log"
TEGRSTATS_PID_FILE="tegrastats_pid.txt"



#for DATA in drjohnson playroom train truck bicycle bonsai counter flowers garden kitchen
for DATA in bicycle bonsai counter flowers garden kitchen room stump treehill
do
    python3 ./tegrastats_3DGS.py $DATA


    # # Command to start tegrastats with sudo and verbose option
    # TEGRSTATS_CMD="sudo tegrastats --verbose --interval 50 --logfile /home/jetson-agx/NeRF/power_measurement/3DGS_20240806/$DATA.csv"

    # # Start the 3DGS rendering process in the background
    # python3 /home/jetson-agx/NeRF/gaussian-splatting/render.py -m /home/jetson-agx/NeRF/models/$DATA\_30k --skip_train &
    # RENDER_PID=$!

    # # Start tegrastats and write its output to a file
    # $TEGRSTATS_CMD > $TEGRSTATS_OUTPUT_FILE &
    # sleep 1
    # TEGRSTATS_PID=$(pgrep -f "tegrastats --verbose")
    # echo $! > $TEGRSTATS_PID_FILE

    # # Wait for the rendering process to complete
    # wait $RENDER_PID

    # # Stop the tegrastats process after rendering is done
    # #if [ -f $TEGRSTATS_PID_FILE ]; then
    # if [ -n "$TEGRSTATS_PID" ]; then
    #     TEGRSTATS_PID=$(cat $TEGRSTATS_PID_FILE)
    #     sudo kill $TEGRSTATS_PID
    #     rm $TEGRSTATS_PID_FILE
    # fi
done


