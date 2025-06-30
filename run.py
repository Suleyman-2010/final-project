import signal
import subprocess

# Commands to start your Flask servers
cmd1 = ["python", "app.py"]
cmd2 = ["python", "api.py"]

# Open log files in write mode (overwrites on each run)
log1 = open("app.log", "w")
log2 = open("api.log", "w")

p1 = subprocess.Popen(cmd1, stdout=log1, stderr=subprocess.STDOUT)
p2 = subprocess.Popen(cmd2, stdout=log2, stderr=subprocess.STDOUT)

print("Servers running!")
print("Logs are in app.log and api.log")
print("Server link: http://127.0.0.1:5000/")

try:
    p1.wait()
    p2.wait()
except KeyboardInterrupt:
    print("\nCaught Ctrl+C, shutting down servers...")
    p1.send_signal(signal.SIGINT)
    p2.send_signal(signal.SIGINT)
    p1.wait()
    p2.wait()

log1.close()
log2.close()
print("Servers stopped. Logs saved.")
