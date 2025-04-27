import yaml
from pathlib import Path


class Config:
    _instance = None

    # Default values
    HOST: str = "127.0.0.1"
    PORT: int = 5037
    DEVICE_NAME: str = "emulator-5554"
    GOLD_MIN: int = 0
    GEMS_MIN: int = 0
    SIZE: str = "1600x900"
    DENSITY: int = 240

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        """Load configuration from config.yml if it exists"""
        config_path = Path(__file__).parent.parent / "config.yml"

        if config_path.exists():
            with open(config_path, "r") as stream:
                try:
                    yaml_config = yaml.safe_load(stream)

                    # Only override values that exist in the yaml file
                    if yaml_config.get("Host"):
                        self.HOST = yaml_config["Host"]
                    if yaml_config.get("Port"):
                        self.PORT = yaml_config["Port"]
                    if yaml_config.get("Name"):
                        self.DEVICE_NAME = yaml_config["Name"]
                    if yaml_config.get("Gold_min") is not None:
                        self.GOLD_MIN = yaml_config["Gold_min"]
                    if yaml_config.get("Gems_min") is not None:
                        self.GEMS_MIN = yaml_config["Gems_min"]

                except yaml.YAMLError as e:
                    print(f"Error loading config.yml: {e}")

    @classmethod
    def get_instance(cls):
        return cls()


# Create a global instance
config = Config()
