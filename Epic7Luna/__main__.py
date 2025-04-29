import argparse

from Epic7Luna.commands.refresh_secret_shop import RefreshSecretShop
from Epic7Luna.utils.adb_manager import device_setup


def main():
    """Main function to run the Epic7Luna bot command line tool."""
    parser = argparse.ArgumentParser(description="Epic7Luna Bot Command Line Tool")
    parser.add_argument('--refresh', action='store_true', help='Refresh the secret shop')
    args = parser.parse_args()

    if args.refresh:
        device = device_setup()
        shop_refresher = RefreshSecretShop(device)
        shop_refresher.refresh(device)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
