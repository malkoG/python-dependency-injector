"""`Aggregate` provider example."""

from dependency_injector import containers, providers


# [TODO] ConfigReader
class ConfigReader:

    # [TODO] ConfigReader > __init__
    def __init__(self, path):
        self._path = path

    # [TODO] ConfigReader > read
    def read(self):
        print(f"Parsing {self._path} with {self.__class__.__name__}")
        ...


# [TODO] YamlReader
class YamlReader(ConfigReader):
    ...


# [TODO] JsonReader
class JsonReader(ConfigReader):
    ...


# [TODO] Container
class Container(containers.DeclarativeContainer):

    config_readers = providers.Aggregate(
        yaml=providers.Factory(YamlReader),
        json=providers.Factory(JsonReader),
    )


if __name__ == "__main__":
    container = Container()

    yaml_reader = container.config_readers("yaml", "./config.yml")
    yaml_reader.read()  # Parsing ./config.yml with YamlReader

    json_reader = container.config_readers("json", "./config.json")
    json_reader.read()  # Parsing ./config.json with JsonReader