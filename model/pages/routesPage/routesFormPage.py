from const.elements import RoutesFormPageItems
from model.components.button import Button
from model.components.textInput import TextInput
from model.pages.basePage import BasePage
from utils.utils import Utils


class RoutesFormPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.route_name_input = TextInput(page, Utils.get_by_test_id(RoutesFormPageItems.GatewayRoutesNameInput))
        self.path_input = TextInput(page, Utils.get_by_test_id(RoutesFormPageItems.RoutesPathInput))
        self.save_btn = Button(page, Utils.get_by_test_id(RoutesFormPageItems.RoutesFormSubmit))

    def route_name_fill(self, route_name: str) -> None:
        self.route_name_input.fill(route_name)

    def path_fill(self, path: str) -> None:
        self.path_input.fill(path)

    def save_route_service(self) -> None:
        self.save_btn.click()


    def create_new_route_service(self, route_name: str, path: str) -> None:
        self.route_name_fill(route_name)
        self.path_fill(path)
        self.save_route_service()

