import pytest
from playwright.sync_api import expect

from const.elements import ServicesFormPageItems
from model.components.button import Button
from model.components.textInput import TextInput
from model.pages.basePage import BasePage
from model.pages.gatewayServicePage.gatewayServiceItemDetailsPage import ServiceItemDetailsPage
from utils.utils import Utils


class GatewayServiceFormPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.serviceNameInput = TextInput(page, Utils.get_by_test_id(ServicesFormPageItems.GatewayServiceNameInput))
        self.tagsInput = TextInput(page, Utils.get_by_test_id(ServicesFormPageItems.GatewayServiceTagsInput))
        self.fullURLRadioBtn = Button(page, Utils.get_by_test_id(ServicesFormPageItems.GatewayServiceURLRadioBtn))
        self.fullURLInput = TextInput(page, Utils.get_by_test_id(ServicesFormPageItems.GatewayServiceFullURLInput))
        self.advancedFields = Button(page,Utils.get_by_test_id(ServicesFormPageItems.AdvancedFieldsExpandBtn))
        self.retriesInput = TextInput(page, Utils.get_by_test_id(ServicesFormPageItems.GatewayServiceRetriesInput))
        self.saveBtn = Button(page,Utils.get_by_test_id(ServicesFormPageItems.GatewayServiceFormSubmit))

    def service_name_fill(self, service_name: str) -> None:
        self.serviceNameInput.fill(service_name)

    def tags_fill(self, tags: str) -> None:
        self.tagsInput.fill(tags)

    def full_url_fill(self, full_url: str) -> None:
        self.fullURLInput.fill(full_url)

    def save(self) -> ServiceItemDetailsPage:
        try:
            self.saveBtn.click()
            expect(self.page.locator('.k-breadcrumbs')).to_be_visible(timeout=5000)
        except AssertionError as e:
            self.page.screenshot(path='error_snapshots/error_submitNewService.png')
            pytest.fail('Save the new service failed.\n' + str(e))
        return ServiceItemDetailsPage(self.page)

    def submit_new_form(self, service_name: str, full_url: str) -> ServiceItemDetailsPage:
        self.service_name_fill(service_name)
        self.full_url_fill(full_url)
        return self.save()