import subprocess

def start_adb_server():
    subprocess.call("adb start-server")
