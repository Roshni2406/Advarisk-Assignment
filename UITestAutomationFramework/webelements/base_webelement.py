from abc import ABC, abstractmethod


class BaseWebElement(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_element(self):
        pass

    @abstractmethod
    def click(self):
        pass



    @abstractmethod
    def send_keys(self, txt_to_set, loose_focus=False):
        pass

    @abstractmethod
    def get_text(self, encoding=None):
        pass
