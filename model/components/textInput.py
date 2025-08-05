from model.components.component import Component


class TextInput(Component):
    @property
    def type_of(self) -> str:
        return "input"

    def fill(self, value: str, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        locator.fill(value)
        locator.blur()