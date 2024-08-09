import sys
import subprocess
import time

# File to store the tegrastats output
tegrastats_output_file = "tegrastats_output.log"

# Start the 3DGS rendering process
#render_process = subprocess.Popen(["python3", "/home/jetson-agx/NeRF/gaussian-splatting/render.py", "-m", "/home/jetson-agx/NeRF/models/bonsai_30k", "--skip_train"])
render_process = subprocess.Popen(["python3", "/home/jetson-agx/NeRF/instant-ngp/scripts/run.py", "/home/jetson-agx/NeRF/datasets/" + sys.argv[1] + "/" + sys.argv[2], "--load_snapshot", "/home/jetson-agx/NeRF/models/" + sys.argv[2] + "_30k/" + sys.argv[2] + "_30k.ingp", "--test_transforms", "/home/jetson-agx/NeRF/datasets/" + sys.argv[1] + "/" + sys.argv[2] + "/transforms_test.json"])

# Start tegrastats and write its output to a file
with open(tegrastats_output_file, "w") as tegrastats_file:
    #tegrastats_process = subprocess.Popen(["tegrastats", "--verbose", "--interval", "50", "--logfile", "../test.csv"], stdout=tegrastats_file, stderr=subprocess.STDOUT)
    tegrastats_process = subprocess.Popen(["tegrastats", "--verbose", "--interval", "1000", "--logfile", "/home/jetson-agx/NeRF/power_measurement/NGP_20240806/" + sys.argv[2] + ".csv"], stdout=tegrastats_file, stderr=subprocess.STDOUT)

# Wait for the rendering process to complete
render_process.wait()

# Stop the tegrastats process after rendering is done
tegrastats_process.terminate()
try:
    # Use sudo to kill the tegrastats process
    subprocess.run(["sudo", "kill", str(tegrastats_process.pid)])
except Exception as e:
    print(f"Error terminating tegrastats: {e}")