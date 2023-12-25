from abc import abstractmethod


class DriverBase:
    """
    Base class for all webdrivers classes
    """

    @staticmethod
    @abstractmethod
    def get():
        pass
