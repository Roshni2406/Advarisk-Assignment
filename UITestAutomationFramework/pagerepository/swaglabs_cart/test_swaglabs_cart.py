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


    def test_verify_continue_shopping_button_is_displayed(self):
        """
        Scenario to verify that Continue shopping button is displayed on cart page
        """
        self.swag_labs_product_page.click_cart_button()
        Assert.assert_true(self.swag_labs_cart_page.verify_conitnue_button_displayed())

    def test_verify_checkout_button_is_displayed(self):
        """
        Scenario to verify that Checkout button is displayed on cart page
        """
        self.swag_labs_product_page.click_cart_button()
        Assert.assert_true(self.swag_labs_cart_page.verify_checkout_button_displayed())

    def test_click_continue_shopping_button(self):
        """
        Scenario to verify that when user clicks on continue shopping button user is navigated to Products page
        """
        self.swag_labs_product_page.click_cart_button()
        self.swag_labs_cart_page.click_continue_button()
        Assert.assert_true(self.swag_labs_product_page.is_page_loaded())

    def test_items_added_in_cart_button(self):
        """
        Scenario to verify the number of items added in cart on products page shall be displayed on cart page
        """
        actual_products_list = self.swag_labs_product_page.get_all_products()
        for product in actual_products_list:
            self.swag_labs_product_page.click_on_add_to_cart_button_by_product_name(product)
        self.swag_labs_product_page.click_cart_button()
        cart_items = self.swag_labs_cart_page.get_all_cart_items()
        deep_diff = DeepDiff(actual_products_list, cart_items)
        Assert.assert_equal(deep_diff, {})

    def test_remove_item_from_cart(self):
        """
        Scenario to verify that when user clicks on remove button for a product on cart page, product is removed for the cart
        """
        actual_products_list = self.swag_labs_product_page.get_all_products()
        for product in actual_products_list:
            self.swag_labs_product_page.click_on_add_to_cart_button_by_product_name(product)
        self.swag_labs_product_page.click_cart_button()
        for product in actual_products_list:
            self.swag_labs_cart_page.click_remove_button(product)
            Assert.assert_false(self.swag_labs_cart_page.verify_cart_item_is_displayed(product))

    def test_verify_items_in_cart_when_user_logout_and_login(self):
        """
        Scenario to verify that items added in cart are not changed when user logs out and login
        """
        actual_products_list = self.swag_labs_product_page.get_all_products()
        for product in actual_products_list:
            self.swag_labs_product_page.click_on_add_to_cart_button_by_product_name(product)
        self.swag_labs_product_page.click_cart_button()
        cart_items_before_logout = self.swag_labs_cart_page.get_all_cart_items()
        self.swag_labs_product_page.click_logout_button()
        self.swag_labs_login_page.login_swag_labs("standard_user", "secret_sauce")
        self.swag_labs_product_page.click_cart_button()
        cart_items_after_logout = self.swag_labs_cart_page.get_all_cart_items()
        deep_diff = DeepDiff(cart_items_before_logout, cart_items_after_logout)
        Assert.assert_equal(deep_diff, {})

    def test_verify_click_checkout_button(self):
        """
        Scenario to verify that when user clicks on checkout button user is navigated to checkout page
        """
        actual_products_list = self.swag_labs_product_page.get_all_products()
        for product in actual_products_list:
            self.swag_labs_product_page.click_on_add_to_cart_button_by_product_name(product)
        self.swag_labs_product_page.click_cart_button()
        self.swag_labs_cart_page.click_checkout_button()
        Assert.assert_true(self.swag_labs_checkout_page.is_page_loaded())

