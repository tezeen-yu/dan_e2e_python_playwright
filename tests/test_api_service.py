import pytest

@pytest.mark.parametrize("name,url",[
  ('svc-test-01', "http://testservice_01.com"),
  ('svc-test-02', "http://testservice_02.com"),
  ('svc-test-03', "http://testservice_03.com")
])
def test_create_and_get_service(service_api,clear_data, name, url):

  res = service_api.create(name, url)
  assert res.status == 201

  services = service_api.get_all().json().get('data', [])
  print(services)
  assert len(services) > 0
  assert any(s["name"] == name for s in services)
