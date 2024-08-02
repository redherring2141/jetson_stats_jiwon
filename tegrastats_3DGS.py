import subprocess
import time

# File to store the tegrastats output
tegrastats_output_file = "tegrastats_output.log"

# Start the 3DGS rendering process
render_process = subprocess.Popen(["python3", "/home/jetson-agx/NeRF/gaussian-splatting/render.py", "-m", "/home/jetson-agx/NeRF/models/bonsai_30k", "--skip_train"])

# Start tegrastats and write its output to a file
with open(tegrastats_output_file, "w") as tegrastats_file:
    tegrastats_process = subprocess.Popen(["tegrastats", "--verbose", "--interval", "50", "--logfile", "../test.csv"], stdout=tegrastats_file, stderr=subprocess.STDOUT)

# Wait for the rendering process to complete
render_process.wait()

# Stop the tegrastats process after rendering is done
tegrastats_process.terminate()
