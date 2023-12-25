from selenium.webdriver.common.by import By


class LocatorIdentifier:
    """
    This class converts and returns the locator strings to locator values using hash map
    """
    locators = {"xpath": By.XPATH}

    @staticmethod
    def string_to_locator(locator_string):
        try:
            return LocatorIdentifier.locators[str.lower(locator_string)]
        except Exception as ex:
            raise type(ex)("Couldn't convert locator string %s to locator value" % locator_string) from ex
