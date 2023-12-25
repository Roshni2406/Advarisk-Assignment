from typing import List
from UITestAutomationFramework.webelements.locator_parser import LocatorIdentifier
from UITestAutomationFramework.webelements.webelement import WebElement


class WebElements:
    """class Description: This is a webElement factory class which wraps the
    list of remote WebElement objects to corresponding WebElement wrappers and
    Providing indexing over them and respective operations through WebElement wrapper objects
    """

    def __init__(self, ui_objected_data, driver):
        self.__ui_objected_data = ui_objected_data
        self.__locator_info = self.__ui_objected_data.locator_info
        self.__driver = driver
        self.__by = LocatorIdentifier.string_to_locator(self.__ui_objected_data.locator)

    def __getitem__(self, index):
        """indexing for the webElements list
          :param index: index of the element
          :type index: int
          :return: WebElement class object which represents the remote webElement int he corresponding index
          :rtype:WebElement
        """
        return WebElement(self.__ui_objected_data, self.__driver, index)

    def get_elements(self):
        """returns the wrapper objects for elements returned by Find_elements
           Each remote WebElement in the list is wrapped into the WebElement wrapper class object
          :return: list of WebElement objects
          :rtype: List[WebElement]
        """
        try:
            web_element_wrappers: List[WebElement] = []
            web_elements = self.__driver.find_elements(self.__by, self.__locator_info)
            for index in range(len(web_elements)):
                web_element_wrappers.append(WebElement(self.__ui_objected_data, self.__driver, index))
            return web_element_wrappers
        except Exception as ex:
            raise ex