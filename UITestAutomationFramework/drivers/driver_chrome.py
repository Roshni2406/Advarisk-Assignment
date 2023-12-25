import os

from selenium import webdriver
from UITestAutomationFramework.drivers.driver_base import DriverBase


class DriverChrome(DriverBase):
    """
    Class to create Chrome Driver Object
    """

    @staticmethod
    def get(private_mode=False):
        """
        This method creates and returns Chrome Driver object
        :return: Chrome Driver Object
        """
        chrome_driver_path = r"driver_exe_files\chromedriver.exe"
        chrome_driver_path_abs = os.path.join(os.path.dirname((os.path.abspath(__file__))),
                                              chrome_driver_path)
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(executable_path=chrome_driver_path_abs, options=options)