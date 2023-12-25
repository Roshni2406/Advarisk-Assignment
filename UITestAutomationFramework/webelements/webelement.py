import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UITestAutomationFramework.webelements.base_webelement import BaseWebElement
from UITestAutomationFramework.webelements.locator_parser import LocatorIdentifier


class WebElement(BaseWebElement):
    """class Description: This is a wrapper for the Selenium Remote WebElement and wraps all the functions of the
    Selenium remote\WebElement class
    """

    def __init__(self, ui_objected_data, driver, index=None, parent=None):
        super().__init__()
        self.__ui_objected_data = ui_objected_data
        self.__locator_info = self.__ui_objected_data.locator_info
        self.__driver = driver
        self.__by = LocatorIdentifier.string_to_locator(self.__ui_objected_data.locator)
        self.index = index
        self.parent = parent

    def get_element(self):
        """finds and returns the web element
            :returns element which is a webelement object
        """
        try:
            if self.index is not None:
                if self.parent is not None:
                    elements = self.parent.get_element().find_elements(self.__by,
                                                                       self.__locator_info)
                else:
                    elements = self.__driver.find_elements(self.__by, self.__locator_info)
                if len(elements) <= self.index:
                    raise IndexError
                else:
                    element = elements[self.index]
            else:
                count = 0
                while not (self.__driver.find_element(self.__by,
                                                      self.__locator_info).is_displayed() or count == 30):
                    time.sleep(1)
                    count = count + 1
                element = self.__driver.find_element(self.__by, self.__locator_info)
            return element
        except Exception as ex:
            raise type(ex)(
                "Not able to get webelement with locator:(" + self.__by + ") and locator info:(" + self.__locator_info + ")") from ex

    def is_displayed(self):
        """returns True if element is visible else False
                    :returns  boolean True/ False
                """
        try:
            web_element = self.get_element()
            return web_element.is_displayed()
        except Exception as ex:
            raise type(ex)("Not able to get webelements with locator:(" + self.__by + ") and locator info:"
                                                                                      "(" + self.__locator_info + ")") from ex

    def click(self, use_action_chains=False):
        """clicks on the web element(any clickable objects)"""
        try:
            web_element = self.get_element()
            web_element.click()
        except Exception as ex:
            if "Other element would receive the click" in str(ex):
                self.get_element().click()
            elif "could not be scrolled into view" in str(ex) or "rect is undefined" in str(
                    ex) or "stale element reference" in str(ex):
                element = WebDriverWait(self.__driver, 30).until(
                    EC.presence_of_element_located((self.__by, self.__locator_info)))
                self.__driver.execute_script("arguments[0].click();", element)
            else:
                raise type(ex)(
                    "Not able to click webelement with locator:(" + self.__by + ") and locator info:(" + self.__locator_info + ")") from ex

    def send_keys(self, txt_to_set, loose_focus=False):
        """sets the value @txt_to_set to the text box
        """
        try:
            web_element = self.get_element()
            web_element.clear()
            web_element.send_keys(txt_to_set)
        except Exception as ex:
            raise type(ex)("Not able to set value in webelement with locator:(" + self.__by + ") and locator info:"
                                                                                              "(" + self.__locator_info + ")") from ex

    def get_text(self, encoding=None):
        """Returns the text set in the textbox
            :returns the value set to the textbox
        """
        try:
            web_element = self.get_element()
            if web_element.text:
                text = web_element.text
            else:
                text = web_element.get_attribute('value')
            return text.encode(encoding) if encoding else text
        except Exception as ex:
            raise type(ex)(
                "'value' attribute not present for webelement with locator:(" + self.__by + ") and locator info:"
                                                                                            "(" + self.__locator_info + ")") from ex

    def get_elements(self):
        """finds and returns the web elements
            :returns list of webelements object
        """
        try:
            if self.index is not None:
                if self.parent is not None:
                    elements = self.parent.get_element().find_elements(self.__by,
                                                                       self.__locator_info)
                else:
                    elements = self.__driver.find_elements(self.__by, self.__locator_info)
                if len(elements) <= self.index:
                    raise IndexError
                else:
                    element = elements[self.index]
            else:
                element = self.__driver.find_elements(self.__by, self.__locator_info)
            return element
        except Exception as ex:
            raise type(ex)(
                "Not able to get webelement with locator:(" + self.__by + ") and locator info:(" + self.__locator_info + ")") from ex
