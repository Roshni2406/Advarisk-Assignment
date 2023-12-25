
from UITestAutomationFramework.drivers.driver import Driver
from UITestAutomationFramework.drivers.driver_chrome import DriverChrome

class DriverFactory:
    """
    Factory class to create webdriver objects.
    """
    @staticmethod
    def get(driver_type, privatebrowsing):
        """
        This method returns a webdriver object based on the drivertype parameter.
        :param driver_type: driver type
        :param privatebrowsing : Incognito Mode
        :return: webdriver object
        """
        try:
            if driver_type == Driver.CHROME:
                return DriverChrome.get(privatebrowsing)

        except Exception as ex:
            raise ex
