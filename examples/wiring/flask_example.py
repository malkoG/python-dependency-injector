"""Flask wiring example."""

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from flask import Flask, json


# [TODO] Service
class Service:
    ...


# [TODO] Container
class Container(containers.DeclarativeContainer):

    service = providers.Factory(Service)


# [TODO] index_view
@inject
def index_view(service: Service = Provide[Container.service]) -> str:
    return json.dumps({"service_id": id(service)})


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    app = Flask(__name__)
    app.add_url_rule("/", "index", index_view)
    app.run()
