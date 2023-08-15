from fastapi import FastAPI, Depends
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject


# [TODO] Service
class Service:
    # [TODO] Service > process
    async def process(self) -> str:
        return "OK"


# [TODO] Container
class Container(containers.DeclarativeContainer):

    service = providers.Factory(Service)


app = FastAPI()


# [TODO] index
@app.api_route("/")
@inject
async def index(service: Service = Depends(Provide[Container.service])):
    result = await service.process()
    return {"result": result}


container = Container()
container.wire(modules=[__name__])
