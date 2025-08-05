from const.elements import ServiceItemDetailsPageItems
from model.components.button import Button
from model.pages.basePage import BasePage
from model.pages.routesPage.routesFormPage import RoutesFormPage
from utils.utils import Utils


class ServiceItemDetailsPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.service_route = Button(page, Utils.get_by_test_id(ServiceItemDetailsPageItems.Routes))
        self.add_route_empty = Button(page, Utils.get_by_test_id(ServiceItemDetailsPageItems.AddRoutesBtnEmpty))

    def __private_get_inner_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text().strip()

    def get_service_id(self) -> str:
        return self.__private_get_inner_text(Utils.get_by_test_id(ServiceItemDetailsPageItems.ServiceID))

    def get_service_name(self) -> str:
        return self.__private_get_inner_text(Utils.get_by_test_id(ServiceItemDetailsPageItems.ServiceName))

    def add_related_route(self) -> RoutesFormPage:
        self.service_route.click()
        self.add_route_empty.click()
        return RoutesFormPage(self.page)
