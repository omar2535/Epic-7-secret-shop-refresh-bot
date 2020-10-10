from ppadb.client import Client as AdbClient
from utils.resource_manager import get_gold_and_gems
from utils.find_image import find_covenant_bookmarks, find_mystic_bookmarks
from utils.inputs import *
import time
import yaml

with open("config.yml", 'r') as stream:
    data = yaml.safe_load(stream)

HOST = data['Host'] or "127.0.0.1"
PORT = data['Port'] or 5037
NAME = data['Name'] or "emulator-5554"
SIZE = "1600x900"
DENSITY = 240

# game related stats
GOLD_MIN = data['Gold_min'] or 0
GEMS_MIN = data['Gems_min'] or 0


# main program to be called
def main():
    mystics_seen = 0
    covenants_seen = 0

    device = device_setup()
    print(f"---Startning shop refresher. MIN_GEMS: {GEMS_MIN}, MIN_GOLD: {GOLD_MIN} ---")

    while True:
        # check top of shop
        check_for_bookmarks_and_purchase(device, covenants_seen, mystics_seen)

        # scroll down to bottom of shop
        time.sleep(0.1)
        scroll_shop(device)
        time.sleep(0.1)

        # check bottom of shop
        check_for_bookmarks_and_purchase(device, covenants_seen, mystics_seen)

        # sleep for a bit before refreshing
        time.sleep(0.5)

        # refresh
        click_refresh(device)
        time.sleep(0.5)
        refresh_confirm(device)
        time.sleep(0.1)

        # update stats file
        update_stats_file(covenants_seen, mystics_seen)

        # if resource count not above threshold, stop the program
        if not is_resource_count_above_threshold():
            break

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

# checks for bookmarks and purchases them
def check_for_bookmarks_and_purchase(device, covenants_seen, mystics_seen):
    # check bottom of shop
    take_screenshot(device)
    covenant_bookmarks_location = find_covenant_bookmarks()
    mystic_bookmarks_location = find_mystic_bookmarks()
    if covenant_bookmarks_location:
        purchase(device, covenant_bookmarks_location[1])
        time.sleep(0.1)
        purchase_confirm(device)
        covenants_seen += 1
    if mystic_bookmarks_location:
        purchase(device, mystic_bookmarks_location[1])
        time.sleep(0.1)
        purchase_confirm(device)
        mystics_seen += 1

# do gem and gold check. Since OCR isn't reliable, the min checks aren't hard stops
def is_resource_count_above_threshold():
    try:
        gold, gems = get_gold_and_gems()
        print(f"Current gold: {gold}, current gems: {gems}")
        if(int(gold) <= GOLD_MIN or int(gems) <= GEMS_MIN):
            return False
    except Exception:
        print("Couldn't do OCR")
        return True
    return True


# update statistics
def update_stats_file(covenants_seen, mystics_seen):
    f = open("stats.txt", "w")
    f.write(f'''Covenant bookmarks purchased: {covenants_seen}
Mystic bookmarks purchased: {mystics_seen}''')
    f.close()

if __name__ == '__main__':
    main()
