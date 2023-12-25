from UITestAutomationFramework.pagerepository.base_page import BasePage
from UITestAutomationFramework.uiobjectrepository.uiobjectrepositoryreader import UiObjectRepositoryReader


class SwaglabsProductsPage(BasePage):
    """
    This class stores all the page elements present in the Products Page of Swaglabs application with functionalities
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
            r"./pagerepository/swaglabs_products/swaglabs_products.csv")

    def __init_page_elements(self):
        """
        Initilizes all page elements in the method.
        """
        self.product_header = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('ProductPage_product_header'))
        self.product_menu_bar = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('ProductPage_menu_bar'))
        self.product_logout = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('ProductPage_logout'))
        self.products = self.create_web_elements(
            self.ui_object_reader.read_ui_object_data('ProductPage_products'))
        self.product_price = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('ProductPage_product_price'))
        self.product_add_to_cart_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('ProductsPage_add_to_cart_button'))
        self.product_remove_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data(
                'ProductsPage_remove_button'))
        self.product_cart_button = self.create_web_element(
            self.ui_object_reader.read_ui_object_data(
                'ProductsPage_cart_button'))
        self.product_cart_badge = self.create_web_element(
            self.ui_object_reader.read_ui_object_data('ProductsPage_cart_button_badge'))

    def is_page_loaded(self):
        if self.product_header.get_text() == "Products":
            return True
        else:
            return False

    def click_menu_bar(self):
        self.product_menu_bar.click()

    def click_logout_button(self):
        self.product_menu_bar.click()
        self.product_logout.click()

    def get_all_products(self):
        product_elements = []
        for i in self.products.get_elements():
            product_elements.append(i.get_text())
        return product_elements

    def get_price_for_each_product_by_product_name(self, product_name):
        self.product_price._WebElement__locator_info = self.product_price._WebElement__locator_info.replace("{PRODUCT}",
                                                                                                            product_name)
        price = self.product_price.get_text()
        self.product_price._WebElement__locator_info = self.product_price._WebElement__locator_info.replace(
            product_name, "{PRODUCT}")
        return price

    def click_on_add_to_cart_button_by_product_name(self, product_name):
        self.product_add_to_cart_button._WebElement__locator_info = self.product_add_to_cart_button._WebElement__locator_info.replace(
            "{PRODUCT}", product_name)
        self.product_add_to_cart_button.click()
        self.product_add_to_cart_button._WebElement__locator_info = self.product_add_to_cart_button._WebElement__locator_info.replace(
            product_name, "{PRODUCT}")

    def verify_remove_button_is_displayed_by_product_name(self, product_name):
        self.product_remove_button._WebElement__locator_info = self.product_remove_button._WebElement__locator_info.replace(
            "{PRODUCT}", product_name)
        return self.product_remove_button.is_displayed()

    def click_cart_button(self):
        self.product_cart_button.click()

    def get_items_in_cart(self):
        return self.product_cart_badge.get_text()
