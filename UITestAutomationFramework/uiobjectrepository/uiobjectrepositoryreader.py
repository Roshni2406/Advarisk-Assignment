import csv
import os

from UITestAutomationFramework.uiobjectrepository.uiobjectdata import UiObjectedData


class UiObjectRepositoryReader():
    """
      Class Description: This class is implementing the Reader Abstract class and returning the
              Locator and LocatorInfo to UiObjectedData class.
     """

    def __init__(self, path):
        self.__path = os.path.join(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))) + path
        self.__web_element_index = 0
        self.__Locator_index = 1
        self.__Locator_info_index = 2
        self.__Locator_Key = 'Locator'
        self.__Locator_info_Key = "Locatorinfo"
        self.csv_file_data = {}

    def read_ui_object_data(self, web_element_name):
        """
           Function Description: Searches the nested dictionary for the matching web_element_name
           and returns the Locator & Locator_info values.
        """
        if os.path.exists(self.__path):

            if len(self.csv_file_data) == 0:
                self.csv_file_reader()

            if web_element_name in self.csv_file_data:
                return UiObjectedData(self.csv_file_data.get(web_element_name).get(self.__Locator_Key),
                                      self.csv_file_data.get(web_element_name).get(self.__Locator_info_Key))
        else:
            raise FileNotFoundError

    def csv_file_reader(self):
        """
           Function Description: Reads the .csv files into nested dictionaries.
        """
        with open(self.__path, 'r') as file:
            reader = csv.reader(file, escapechar='~')
            for row in reader:
                self.csv_file_data[row[self.__web_element_index]] = {self.__Locator_Key: row[self.__Locator_index],
                                                                     self.__Locator_info_Key: row[
                                                                         self.__Locator_info_index]}
