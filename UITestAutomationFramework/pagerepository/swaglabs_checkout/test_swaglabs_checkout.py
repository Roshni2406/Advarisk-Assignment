import time
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
        self.swag_labs_checkout_page = self.browser.get_page(PageRegister.SWAG_LABS_CHECKOUT_PAGE)
        self.swag_labs_login_page.login_swag_labs("standard_user", "secret_sauce")
        actual_products_list = self.swag_labs_product_page.get_all_products()
        for product in actual_products_list:
            self.swag_labs_product_page.click_on_add_to_cart_button_by_product_name(product)
        self.swag_labs_product_page.click_cart_button()
        self.swag_labs_cart_page.click_checkout_button()

    def test_verify_continue_button_is_displayed(self):
        Assert.assert_true(self.swag_labs_checkout_page.verify_continue_button_displayed())

    def test_verify_cancel_button_is_displayed(self):
        Assert.assert_true(self.swag_labs_checkout_page.verify_cancel_button_displayed())

    def test_error_message_first_name_last_name_postal_code_blank(self):
        """
        Verify the error message when first name, last name and postal code is blank
        """
        self.swag_labs_checkout_page.click_continue_button()

        expected_error_message = "Error: First Name is required"
        Assert.assert_equal(expected_error_message, self.swag_labs_checkout_page.get_error_message())

    def test_error_message_last_name_postal_code_blank(self):
        """
        Verify the error message when last name and postal code is blank
        """
        self.swag_labs_checkout_page.set_first_name("ABC")
        self.swag_labs_checkout_page.click_continue_button()
        expected_error_message = "Error: Last Name is required"
        Assert.assert_equal(expected_error_message, self.swag_labs_checkout_page.get_error_message())

    def test_error_message_postal_code_blank(self):
        """
        Verify the error message when postal code is blank
        """
        self.swag_labs_checkout_page.set_first_name("ABC")
        self.swag_labs_checkout_page.set_last_name("XYZ")
        self.swag_labs_checkout_page.click_continue_button()
        expected_error_message = "Error: Postal code is required"
        Assert.assert_equal(expected_error_message, self.swag_labs_checkout_page.get_error_message())

    def test_verify_cancel_button(self):
        """
        Scenario to verify that when user clicks on Cancel button user is navigated to cart page
        """
        self.swag_labs_checkout_page.click_cancel_button()
        Assert.assert_true(self.swag_labs_cart_page.is_page_loaded())

    def test_verify_click_finish_button(self):
        """
        Scenario to verify checkout successfull bu adding valid first name, last name and zip code
        """
        self.swag_labs_checkout_page.set_first_name("ABC")
        self.swag_labs_checkout_page.set_last_name("XYZ")
        self.swag_labs_checkout_page.set_postal_code("123")
        self.swag_labs_checkout_page.click_continue_button()
        self.swag_labs_checkout_page.click_finish_button()
        expected_message = "Thank you for your order!"
        Assert.assert_equal(expected_message,self.swag_labs_checkout_page.verify_thankyou_message())
