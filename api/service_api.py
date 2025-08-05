
from api.api_client import APIClient

class ServiceAPI:
    def __init__(self, client: APIClient):
        self.client = client

    def get_all(self):
        return self.client.get("/default/services")

    def create(
            self,
            name: str,
            url: str,
            tags: str = None,
            port: int = 80,
            retries: int = 5
    ):
        return self.client.post("/default/services", {
            "name": name,
            "url": url,
            "tags": tags,
            "port": port,
            "retries": retries
        })

    def delete(self, service_id: str):
        return self.client.delete(f"/default/services/{service_id}")

    def delete_all(self):
        res = self.client.get("/default/services")
        assert res.status == 200
        services = res.json().get("data", [])
        if len(services) > 0:
            for service in services:
                svc_id = service.get("id")
                if len(svc_id):
                    del_service = self.client.delete(f"/default/services/{svc_id}")
                    assert del_service.status in (200, 204), f"failed delete the service from API. {del_service.status}"
