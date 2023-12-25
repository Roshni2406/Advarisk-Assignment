from abc import abstractmethod
from UITestAutomationFramework.webelements.webelement import WebElement
from UITestAutomationFramework.webelements.webelements import WebElements


class BasePage:
    """
    Base class for all pages in the application
    """

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def __init_ui_object_reader(self):
        pass

    @abstractmethod
    def __init_page_elements(self):
        pass

    def create_web_element(self, ui_object_data):
        """
        Method creates and returns webelemnt with the ui_object data provided from the pages
        :param ui_object_data: ui object name
        :param wait: explicit wait time for the element
        :return: webelemnt
        """
        return WebElement(ui_object_data, self.driver)

    def create_web_elements(self, ui_object_data):
        """
        Method creates and returns webelemnt with the ui_object data provided from the pages
        :param ui_object_data: ui object name
        :return: webelemnt
        """
        return WebElements(ui_object_data, self.driver)

    def is_page_loaded(self):
        """
        Method to verify a page is loaded properly
        :return:True/False
        :rtype: boolean
        """
        raise NotImplementedError


