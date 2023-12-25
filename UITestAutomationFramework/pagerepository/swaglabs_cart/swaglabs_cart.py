from UITestAutomationFramework.pagerepository.base_page import BasePage
from UITestAutomationFramework.uiobjectrepository.uiobjectrepositoryreader import UiObjectRepositoryReader


class SwaglabsCartPage(BasePage):
    """
    This class stores all the page elements present in the Cart Page of Swaglabs application with functionalities
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
            r"./pagerepository/swaglabs_cart/swaglabs_cart.csv")

    def __init_page_elements(self):
        """
        Initilizes all page elements in the method.
        """
        self.cart_header = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CartPage_header'))
        self.continue_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CartPage_continue_shopping_button'))
        self.checkout_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CartPage_checkout_button'))
        self.cart_remove_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('CartPage_remove_button'))
        self.cart_items = self.create_web_elements(self.ui_object_reader.read_ui_object_data('CartPage_cart_item'))
        self.cart_item = self.create_web_element(self.ui_object_reader.read_ui_object_data('CartPage_cart_item_single'))

    def is_page_loaded(self):
        if self.cart_header.get_text() == "Your Cart":
            return True
        else:
            return False

    def verify_conitnue_button_displayed(self):
        self.continue_button.is_displayed()

    def verify_checkout_button_displayed(self):
        self.checkout_button.is_displayed()

    def click_continue_button(self):
        self.continue_button.click()

    def click_checkout_button(self):
        self.checkout_button.click()

    def click_remove_button(self, product_name):
        self.cart_remove_button._WebElement__locator_info = self.cart_remove_button._WebElement__locator_info.replace(
            "{PRODUCT}", product_name)
        self.cart_remove_button.click()
        self.cart_remove_button._WebElement__locator_info = self.cart_remove_button._WebElement__locator_info.replace(
            product_name, "{PRODUCT}")

    def verify_remove_button_displayed(self, product_name):
        self.cart_remove_button._WebElement__locator_info = self.cart_remove_button._WebElement__locator_info.replace(
            "{PRODUCT}", product_name)
        self.cart_remove_button.is_displayed()

    def get_all_cart_items(self):
        cart_items = []
        for i in self.cart_items.get_elements():
            cart_items.append(i.get_text())
        return cart_items

    def verify_cart_item_is_displayed(self, product_name):
        try:
            self.cart_item._WebElement__locator_info = self.cart_item._WebElement__locator_info.replace(
                "{PRODUCT}", product_name)
            return self.cart_item.is_displayed()
        except:
            return False
