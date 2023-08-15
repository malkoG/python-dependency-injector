import os


# [TODO] ApiClient
class ApiClient:

    # [TODO] ApiClient > __init__
    def __init__(self):
        self.api_key = os.getenv("API_KEY")  # <-- dependency
        self.timeout = os.getenv("TIMEOUT")  # <-- dependency


# [TODO] Service
class Service:

    # [TODO] Service > __init__
    def __init__(self):
        self.api_client = ApiClient()  # <-- dependency


# [TODO] main
def main() -> None:
    service = Service()  # <-- dependency
    ...


if __name__ == "__main__":
    main()
