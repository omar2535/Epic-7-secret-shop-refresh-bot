import subprocess

def start_adb_server():
    subprocess.call("adb devices -l");
    subprocess.call("adb start-server")
