from playwright.sync_api import APIRequestContext, APIResponse

class APIClient:
    def __init__(self, request: APIRequestContext, base_url: str):
        self.request = request
        self.base_url = base_url

    def get(self, endpoint: str) -> APIResponse:
        return self.request.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint: str, data: dict) -> APIResponse:
        return self.request.post(f"{self.base_url}{endpoint}", data=data)

    def put(self, endpoint: str, data: dict) -> APIResponse:
        return self.request.put(f"{self.base_url}{endpoint}", data=data)

    def delete(self, endpoint: str) -> APIResponse:
        return self.request.delete(f"{self.base_url}{endpoint}")

    def delete_service(self, service_id: str) -> None:
        res = self.request.delete(f'{self.base_url}/default/services/{service_id}')
        assert res.status == 204