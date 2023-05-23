from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class MacOSButton(Button):
    def paint(self):
        return "Render a button in a MacOS style"

class WindowsButton(Button):
    def paint(self):
        return "Render a button in a Windows style"

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class MacOSCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in a MacOS style"

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in a Windows style"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class Application:
    def __init__(self, factory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        return f"{self.button.paint()} and {self.checkbox.paint()}"

app = Application(MacOSFactory())
app.create_ui()
print(app.paint())

app = Application(WindowsFactory())
app.create_ui()
print(app.paint())