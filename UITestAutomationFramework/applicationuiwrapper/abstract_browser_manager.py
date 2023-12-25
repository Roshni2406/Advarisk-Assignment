from abc import abstractmethod


class AbstractBrowserManager:
    """
    Class contains abstract methods for Browser
    """

    @abstractmethod
    def get_driver(self):
        pass

    @abstractmethod
    def launch(self):
        pass


