"""Services module."""


# [TODO] ConfigService
class ConfigService:
    # [TODO] ConfigService > __init__
    def __init__(self, config):
        self._config = config

    # [TODO] ConfigService > build
    def build(self):
        self._config.from_dict({"default": {"db_path": "~/test"}})