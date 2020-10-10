from ppadb.client import Client as AdbClient
from utils.resource_manager import get_gold_and_gems
from utils.find_image import find_covenant_bookmarks
from utils.inputs import *
import time


HOST = "127.0.0.1"
PORT = 5037
NAME = "emulator-5554"
SIZE = "1600x900"
DENSITY = 240

# game related stats
GOLD_MIN = 3000000
GEMS_MIN = 3000


def main():
    device = device_setup()
    print("---Startning main loop---")
    
    while True:
        # do gem and gold check
        gold, gems = get_gold_and_gems()
        print(f"Current gold: {gold}, current gems: {gems}")
        if(int(gold) <= GOLD_MIN or int(gems) <= GEMS_MIN):
            break

        # check top of shop
        take_screenshot(device)
        covenant_bookmarks_location = find_covenant_bookmarks()
        if covenant_bookmarks_location:
            purchase(device, covenant_bookmarks_location[1])
            time.sleep(1)
            purchase_confirm(device)

        time.sleep(1)
        scroll_shop(device)
        time.sleep(1)

        # check bottom of shop
        take_screenshot(device)
        covenant_bookmarks_location = find_covenant_bookmarks()
        if covenant_bookmarks_location:
            purchase(device, covenant_bookmarks_location[1])
            time.sleep(1)
            purchase_confirm(device)
        
        time.sleep(1)

        # refresh
        click_refresh(device)
        time.sleep(1)
        refresh_confirm(device)
        time.sleep(1)

    print("---Program complete---")



# Sets up ADB device
def device_setup():
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("emulator-5554")
    device.shell(f"wm size {SIZE}")
    device.shell(f"wm density {DENSITY}")
    return device


# takes a screenshot
# saves in screenshots/screen.png
def take_screenshot(device):
    result = device.screencap()
    with open("screenshots/screen.png", "wb") as fp:
        fp.write(result)


if __name__ == '__main__':
    main()
