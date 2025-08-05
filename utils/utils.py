class Utils:
    test_id = 'data-testid='

    @staticmethod
    def get_by_test_id(elem: str) -> str:
        return f'[{Utils.test_id}{elem}]'

    @staticmethod
    def get_dropdown_item(option: str) -> str:
        return f'[{Utils.test_id}"select-item-${option}"]'

    @staticmethod
    def element_exists(page, elem: str) -> bool:
        selector = Utils.get_by_test_id(elem)
        return page.locator(selector).count() > 0