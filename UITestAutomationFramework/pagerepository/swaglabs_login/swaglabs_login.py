from UITestAutomationFramework.pagerepository.base_page import BasePage
from UITestAutomationFramework.uiobjectrepository.uiobjectrepositoryreader import UiObjectRepositoryReader


class SwaglabsLoginPage(BasePage):
    """
    This class stores all the page elements present in the Login Page of Swaglabs application with functionalities
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.__init_ui_object_reader()
        self.__init_page_elements()

    def __init_ui_object_reader(self):
        """
        Method initilizes reader which reads data from the csv
        """
        self.ui_object_reader = UiObjectRepositoryReader(
            r"./pagerepository/swaglabs_login/swaglabs_login.csv")

    def __init_page_elements(self):
        """
        Initilizes all page elements in the method.
        """
        self.username = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('LoginPage_username'))
        self.password = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('LoginPage_password'))
        self.login_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('LoginPage_login_button'))
        self.login_error = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('LoginPage_error'))
        self.error_close_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('LoginPage_error_close_button'))

    def set_username(self, username):
        self.username.send_keys(username)

    def set_password(self, password):
        self.password.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def login_swag_labs(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def get_login_error(self):
        return self.login_error.get_text()

    def close_error_bar(self):
        self.error_close_button.click()
