from const.elements import ServicesPageItems
from model.components.button import Button
from model.pages.basePage import BasePage
from model.pages.gatewayServicePage.gatewayServiceFormPage import GatewayServiceFormPage
from model.pages.gatewayServicePage.gatewayServiceItemDetailsPage import ServiceItemDetailsPage
from utils.utils import Utils


class GatewayServicesPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.create_new_service_btn_empty = Button(page, Utils.get_by_test_id(ServicesPageItems.AddGatewayServiceEmpty))
        self.create_new_service_btn = Button(page, Utils.get_by_test_id(ServicesPageItems.AddGatewayService))
        self.filter_btn = Button(page, Utils.get_by_test_id(ServicesPageItems.FilterButton))

    def add_gateway_services(self) -> GatewayServiceFormPage:
        if Utils.element_exists(self.page, ServicesPageItems.FilterButton):
            self.create_new_service_btn.click()
        else:
            self.create_new_service_btn_empty.click()
        return GatewayServiceFormPage(self.page)

    def get_services_count(self) -> int:
        return self.page.locator('table > tbody > tr').count()

    def open_service_item_details_page(self, service_name:str) -> ServiceItemDetailsPage:
        row_selector = Utils.get_by_test_id(service_name)
        td_selector = Utils.get_by_test_id('name')
        self.page.locator(f'tr{row_selector} > td{td_selector}').click()
        return ServiceItemDetailsPage(self.page)
