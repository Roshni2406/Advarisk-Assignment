"""
Python file containing BrowserManager class
"""
from UITestAutomationFramework.applicationuiwrapper.abstract_browser_manager import AbstractBrowserManager
from UITestAutomationFramework.drivers.driver_factory import DriverFactory


class BrowserManager(AbstractBrowserManager):
    """
    Class to maintain browser functionalities, driver initialization, page initialization.
    """

    def __init__(self):
        """
          Creates a new instance of Browser
          Initialises browser config
          Initialises webdriver
        """
        self.__driver = None
        self.__init_driver("chrome")

    def __init_driver(self, driver_type, privatebrowsing=False):
        """
        Creates and initilizes webdriver object.
        :param driver_type: driver_type should be mentioned in the browser config file
        :param privatebrowsing : Open browser in private mode
        """
        self.__driver = DriverFactory.get(driver_type, privatebrowsing)
        self.__driver.implicitly_wait("10")

    def get_driver(self):
        """
        Returns webdriver object.
        :return: webdriver
        """
        return self.__driver

    def launch(self, url=None):
        """
        Launches the browser with url specified in browser configuration file.
        """
        if self.__driver is None:
            self.__init_driver("chrome")
        self.__driver.maximize_window()
        self.__driver.get(url)

    def get_page(self, page_name):
        """
        Returns object of page class for interaction with page elements
        :param page_name: name of the page class
        :return: object of page class
        """

        try:
            path_list = page_name.split('.')
            module_name = ".".join(path_list[:-1])
            mod = __import__(module_name)
            for cls in path_list[1:]:
                mod = getattr(mod, cls)
            page_obj = mod(self.__driver)
            return page_obj
        except Exception as ex:
            raise ex
