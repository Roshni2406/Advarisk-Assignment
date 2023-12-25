from UITestAutomationFramework.pagerepository.base_page import BasePage
from UITestAutomationFramework.uiobjectrepository.uiobjectrepositoryreader import UiObjectRepositoryReader


class SwaglabsCheckoutPage(BasePage):
    """
    This class stores all the page elements present in the Checkout Page of Swaglabs application with functionalities
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
            r"./pagerepository/swaglabs_checkout/swaglabs_checkout.csv")

    def __init_page_elements(self):
        """
        Initilizes all page elements in the method.
        """
        self.checkout_header = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CheckoutPage_header'))
        self.continue_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CheckoutPage_continue_button'))
        self.cancel_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CheckoutPage_cancel_button'))
        self.first_name = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CheckoutPage_first_name'))
        self.last_name = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CheckoutPage_last_name'))
        self.postal_code = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CheckoutPage_postal_code'))
        self.error_message = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CheckoutPage_error_message'))
        self.finish_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CheckoutPage_finish_button'))
        self.thankyou_message = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CheckoutPage_thankyou_message'))

    def is_page_loaded(self):
        if self.checkout_header.get_text() == "Checkout: Your Information":
            return True
        else:
            return False

    def verify_continue_button_displayed(self):
        return self.continue_button.is_displayed()

    def verify_cancel_button_displayed(self):
        return self.cancel_button.is_displayed()

    def click_continue_button(self):
        self.continue_button.click()

    def click_cancel_button(self):
        self.cancel_button.click()

    def set_first_name(self,first_name):
        self.first_name.send_keys(first_name)

    def set_last_name(self,last_name):
        self.last_name.send_keys(last_name)

    def set_postal_code(self,postal_code):
        self.postal_code.send_keys(postal_code)

    def get_error_message(self):
        return self.error_message.get_text()

    def click_finish_button(self):
        self.finish_button.click()

    def verify_thankyou_message(self):
        return self.thankyou_message.get_text()






