import os


# [TODO] ApiClient
class ApiClient:

    # [TODO] ApiClient > __init__
    def __init__(self, api_key: str, timeout: int) -> None:
        self.api_key = api_key  # <-- dependency is injected
        self.timeout = timeout  # <-- dependency is injected


# [TODO] Service
class Service:

    # [TODO] Service > __init__
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client  # <-- dependency is injected


# [TODO] main
def main(service: Service) -> None:  # <-- dependency is injected
    ...


if __name__ == "__main__":
    main(
        service=Service(
            api_client=ApiClient(
                api_key=os.getenv("API_KEY"),
                timeout=int(os.getenv("TIMEOUT")),
            ),
        ),
    )