import os
import json
import logging

LOGGER = logging.getLogger('sLogger')

class ConfigurationManager:
    _instance = None
    _configurations = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def load_from_file(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as config_file:
                self._configurations = json.load(config_file)
                LOGGER.info(f"Configurations loaded from {file_path}")
        except Exception as error:
            LOGGER.critical(f"Failed to load configurations from {file_path} - {error}")

    def load_from_env(self) -> None:
        try:
            for key, value in os.environ.items():
                if key.startswith("APP_"):
                    self._configurations[key] = value
            LOGGER.info("Configurations loaded from environment variables")
        except Exception as error:
            LOGGER.critical(f"Failed to load configurations from environment variables - {error}")

    def get(self, key: str, default=None):
        return self._configurations.get(key, default)
