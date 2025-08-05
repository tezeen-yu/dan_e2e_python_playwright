
from api.api_client import APIClient

class RouteAPI:
    def __init__(self, client: APIClient):
        self.client = client

    def get_all(self):
        return self.client.get("/default/routes")

    def create(
            self,
            name: str,
            url: str,
            tags: str = None,
            port: int = 80,
            retries: int = 5
    ):
        return self.client.post("/default/routes", {
            "name": name,
            "url": url,
            "tags": tags,
            "port": port,
            "retries": retries
        })

    def delete(self, service_id: str):
        return self.client.delete(f"/default/routes/{service_id}")

    def delete_all(self):
        res = self.client.get("/default/routes")
        assert res.status == 200
        services = res.json().get("data", [])
        if len(services) > 0:
            for service in services:
                svc_id = service.get("id")
                if len(svc_id):
                    del_route = self.client.delete(f"/default/routes/{svc_id}")
                    assert del_route.status in (200, 204), f"failed delete the route from API. {del_route.status}"
