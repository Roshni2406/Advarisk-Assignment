
import unittest

from deepdiff import DeepDiff

from UITestAutomationFramework.applicationuiwrapper.browser_manager import BrowserManager
from UITestAutomationFramework.applicationuiwrapper.page_register import PageRegister
from UITestAutomationFramework.assertions.assertion import Assert


class TestSwaglabsLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = BrowserManager()
        self.driver = self.browser.get_driver()
        self.browser.launch("https://www.saucedemo.com/")
        self.swag_labs_login_page = self.browser.get_page(PageRegister.SWAG_LABS_LOGIN_PAGE)
        self.swag_labs_product_page = self.browser.get_page(PageRegister.SWAG_LABS_PRODUCT_PAGE)
        self.swag_labs_cart_page = self.browser.get_page(PageRegister.SWAG_LABS_CART_PAGE)
        self.swag_labs_login_page.login_swag_labs("standard_user", "secret_sauce")


    def test_get_all_products(self):
        """
        Scenario to verify that all the required products displays on the products page
        """
        actual_products_list = self.swag_labs_product_page.get_all_products()
        expected_product_list = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                                 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
        deep_diff = DeepDiff(actual_products_list, expected_product_list)
        Assert.assert_equal(deep_diff, {})

    def test_price_for_all_product(self):
        """
        Scenario to verify price for the products displayed on the products page
        """
        product_price_dict = {}
        expected_product_price_dict = {'Sauce Labs Backpack': '$29.99', 'Sauce Labs Bike Light': '$9.99',
                                       'Sauce Labs Bolt T-Shirt': '$15.99',
                                       'Sauce Labs Fleece Jacket': '$49.99', 'Sauce Labs Onesie': '$7.99',
                                       'Test.allTheThings() T-Shirt (Red)': '$15.99'}
        actual_products_list = self.swag_labs_product_page.get_all_products()
        for product in actual_products_list:
            product_price_dict.update(
                {product: self.swag_labs_product_page.get_price_for_each_product_by_product_name(product)})
        deep_diff = DeepDiff(product_price_dict, expected_product_price_dict)
        Assert.assert_equal(deep_diff, {})

    def test_add_to_cart_for_single_product(self):
        """
        Scenario to verify that Remove button is displayed when user clicks on Add to cart button for a product
        """
        self.swag_labs_product_page.click_on_add_to_cart_button_by_product_name('Sauce Labs Backpack')
        Assert.assert_true(
            self.swag_labs_product_page.verify_remove_button_is_displayed_by_product_name('Sauce Labs Backpack'))

    def test_add_to_cart_button_click_for_all_products(self):
        """
        Scenario to verify that Remove button is displayed when user clicks on Add to cart button for multiple product product
        """
        actual_products_list = self.swag_labs_product_page.get_all_products()
        for product in actual_products_list:
            self.swag_labs_product_page.click_on_add_to_cart_button_by_product_name(product)
            Assert.assert_true(
                self.swag_labs_product_page.verify_remove_button_is_displayed_by_product_name(product))

    def test_click_cart_button(self):
        """
        Scenario to verify that user is navigated to cart page when user clicks on cart button on products page
        """
        self.swag_labs_product_page.click_cart_button()
        Assert.assert_true(self.swag_labs_cart_page.is_page_loaded())

    def test_number_of_items_displayed_on_cart_badge(self):
        """
        Scenario to verify the number of products displayed on cart badge on products page
        """
        actual_products_list = self.swag_labs_product_page.get_all_products()
        for product in actual_products_list:
            self.swag_labs_product_page.click_on_add_to_cart_button_by_product_name(product)

        Assert.assert_equal(len(actual_products_list), int(self.swag_labs_product_page.get_items_in_cart()))
