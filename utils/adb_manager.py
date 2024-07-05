import subprocess


def start_adb_server(bluestacks_adb_port):
    subprocess.call("adb kill-server")
    # subprocess.call("adb devices -l");
    # subprocess.call("adb start-server")
    subprocess.call(f"adb connect 127.0.0.1:{bluestacks_adb_port}")
