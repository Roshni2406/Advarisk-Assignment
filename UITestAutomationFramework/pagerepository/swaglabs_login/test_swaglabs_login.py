import time
import unittest

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

    def test_swaglabs_application_navigation(self):
        """
        Verify that user successfully navigates to swag lab application from the given url
        """
        excepted_title = "Swag Labs"
        actual_title = self.browser.get_driver().title
        Assert.assert_equal(excepted_title, actual_title)

    def test_valid_login(self):
        """
        Scenario:Verify that user successfully logs into swag labs application with all the valid accepted usernames and valid accepted password
        """

        self.swag_labs_login_page.login_swag_labs("standard_user", "secret_sauce")
        Assert.assert_true(self.swag_labs_product_page.is_page_loaded())

    def test_lockout_user(self):
        """
        Scenario:Verify the error message when lockout user enters its username and password on swag labs login page
        """
        self.swag_labs_login_page.login_swag_labs("locked_out_user", "secret_sauce")
        expected_error_msg = "Epic sadface: Sorry, this user has been locked out."
        actual_error_msg = self.swag_labs_login_page.get_lockout_error()
        Assert.assert_equal(expected_error_msg, actual_error_msg)

    def test_blank_user_name(self):
        """
        Scenario:Verify the error message when username is blank and valid password is entered on login page
        """
        self.swag_labs_login_page.login_swag_labs("", "secret_sauce")
        expected_error_msg = "Epic sadface: Username is required"
        actual_error_msg = self.swag_labs_login_page.get_login_error()
        Assert.assert_equal(expected_error_msg, actual_error_msg)

    def test_blank_password(self):
        """
        Scenario:Verify the error message when username is valid and blank password is entered on login page
        """
        self.swag_labs_login_page.login_swag_labs("standard_user", "")
        expected_error_msg = "Epic sadface: Password is required"
        actual_error_msg = self.swag_labs_login_page.get_login_error()
        Assert.assert_equal(expected_error_msg, actual_error_msg)

    def test_invalid_username(self):
        """
        Scenario:Verify the error message when username is invalid and valid password is entered on login page
        """
        self.swag_labs_login_page.login_swag_labs("xyz", "secret_sauce")
        expected_error_msg = "Epic sadface: Username and password do not match any user in this service"
        actual_error_msg = self.swag_labs_login_page.get_login_error()
        Assert.assert_equal(expected_error_msg, actual_error_msg)

    def test_invalid_password(self):
        """
        Scenario:Verify the error message when username is valid and invalid password is entered on login page
        """
        self.swag_labs_login_page.login_swag_labs("standard_user", "abc")
        expected_error_msg = "Epic sadface: Username and password do not match any user in this service"
        actual_error_msg = self.swag_labs_login_page.get_login_error()
        Assert.assert_equal(expected_error_msg, actual_error_msg)

    def test_blank_username_and_password(self):
        """
        Scenario:Verify the error message when username and password are blank on login page
        """
        self.swag_labs_login_page.login_swag_labs("", "")
        expected_error_msg = "Epic sadface: Username is required"
        actual_error_msg = self.swag_labs_login_page.get_login_error()
        Assert.assert_equal(expected_error_msg, actual_error_msg)

    def test_priority_of_blank_values_messages(self):
        """
        Verify the priority of error messages for blank fields on login page
        """
        self.swag_labs_login_page.login_swag_labs("", "")
        expected_error_msg = "Epic sadface: Username is required"
        actual_error_msg = self.swag_labs_login_page.get_login_error()
        Assert.assert_equal(expected_error_msg, actual_error_msg)
        self.swag_labs_login_page.login_swag_labs("standard_user", "")
        expected_error_msg = "Epic sadface: Password is required"
        actual_error_msg = self.swag_labs_login_page.get_login_error()
        Assert.assert_equal(expected_error_msg, actual_error_msg)

    def test_close_error_message_bar(self):

        """
        Verify that when user clicks on close button on error message, error message is not displayed on login page
        """
        self.swag_labs_login_page.login_swag_labs("", "")
        self.swag_labs_login_page.close_error_bar()
        Assert.assert_false(self.swag_labs_login_page.get_login_error().is_displayed())


