import subprocess
from ppadb.client import Client as AdbClient
from ppadb.device import Device
from Epic7Luna.config import config


def start_adb_server(bluestacks_adb_port: int) -> None:
    """Starts the ADB server

    Args:
        bluestacks_adb_port (int): The adb port for Bluestacks.
    """
    subprocess.call("adb kill-server")
    # subprocess.call("adb devices -l");
    # subprocess.call("adb start-server")
    subprocess.call(f"adb connect 127.0.0.1:{bluestacks_adb_port}")


# Sets up ADB device
def device_setup() -> Device:
    """
    Sets up the ADB device connection and configures the screen size and density.
    Returns the connected device object.
    """

    start_adb_server(config.PORT)
    client = AdbClient(host=config.HOST)
    device: None | Device = client.device(config.DEVICE_NAME)

    if not device:
        print(f"Device {config.DEVICE_NAME} not found")
        raise SystemExit(1)

    device.shell(f"wm size {config.SIZE}")
    device.shell(f"wm density {config.DENSITY}")
    return device
