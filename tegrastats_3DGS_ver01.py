import sys
import os
import signal
import subprocess
import time

# File to store the tegrastats output
tegrastats_output_file = "tegrastats_output.log"

# Start the 3DGS rendering process
#render_process = subprocess.Popen(["python3", "/home/jetson-agx/NeRF/gaussian-splatting/render.py", "-m", "/home/jetson-agx/NeRF/models/bonsai_30k", "--skip_train"])
render_process = subprocess.Popen(["python3", "/home/jetson-agx/NeRF/gaussian-splatting/render.py", "-m", "/home/jetson-agx/NeRF/models/" + sys.argv[1] + "_30k", "--skip_train"])

# Start tegrastats and write its output to a file
with open(tegrastats_output_file, "w") as tegrastats_file:
    # tegrastats_process = subprocess.Popen(["tegrastats", "--verbose", "--interval", "50", "--logfile", "../test.csv"], stdout=tegrastats_file, stderr=subprocess.STDOUT)
    tegrastats_process = subprocess.Popen(["sudo", "tegrastats", "--verbose", "--interval", "50", "--logfile", "/home/jetson-agx/NeRF/power_measurement/3DGS_20240806/" + sys.argv[1] + ".csv"], stdout=tegrastats_file, stderr=subprocess.STDOUT, shell=True, preexec_fn=os.setsid)


#tegrastats_process = subprocess.Popen(["sudo", "tegrastats", "--verbose", "--interval", "50", "--logfile", "/home/jetson-agx/NeRF/power_measurement/3DGS_20240806/" + sys.argv[1] + ".csv"], shell=True, preexec_fn=os.setsid)

# Wait for the rendering process to complete
render_process.wait()

# Stop the tegrastats process after rendering is done
# tegrastats_process.terminate()
# try:
#     # Use sudo to kill the tegrastats process
#     subprocess.run(["sudo", "kill", str(tegrastats_process.pid)])
# except Exception as e:
#     print(f"Error terminating tegrastats: {e}")

#subprocess.run(["sudo", "kill", str(tegrastats_process.pid)])
#os.kill(tegrastats_process.pid, signal.SIGTERM)
#os.kill(tegrastats_process.pid, signal.SIGKILL)
os.killpg(os.getpgid(tegrastats_process.pid), signal.SIGTERM)