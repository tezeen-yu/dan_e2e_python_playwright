from model.pages.gatewayServicePage.gatewayServicePage import GatewayServicesPage

def test_add_service(service_api, page):
    gs: GatewayServicesPage = GatewayServicesPage(page)
    gs.visit("http://localhost:8002/default/services")
    gs.assert_title("Gateway Services")
    gs_form = gs.add_gateway_services()
    gs_form.assert_title("Create Gateway Service")
    gs_item_details = gs_form.submit_new_form('cc', 'http://testservice_01.com')
    service_id = gs_item_details.get_service_id()
    service_name = gs_item_details.get_service_name()
    gs.visit("http://localhost:8002/default/services")
    gs.open_service_item_details_page(service_name)
    print(service_id)
    res = service_api.delete(service_id)
    assert res.status in (200, 204)

def test_add_service_route(service_api, page):
    gs: GatewayServicesPage = GatewayServicesPage(page)
    gs.visit("http://localhost:8002/default/services")
    gs.assert_title("Gateway Services")
    gs_form = gs.add_gateway_services()
    gs_form.assert_title("Create Gateway Service")
    gs_item_details = gs_form.submit_new_form('cc', 'http://testservice_01.com')
    rt_form_page = gs_item_details.add_related_route()
    rt_form_page.create_new_route_service('route_01', '/route_01')




