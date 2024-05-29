from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import test_data
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import *


class Test_Imdb:
    url = "https://www.imdb.com/search/name/"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        yield
        self.driver.close()

    # IMDB
    def test_data_26(self, booting_function):
        self.driver.get(self.url)
        self.driver.execute_script('window.scrollBy(0, 500)')

        # EXPAND ALL:-
        expand_all = self.driver.find_element(By.XPATH, test_data.TestSelectors.expand_all_xpath)

        expand_all.click()
        self.driver.execute_script('window.scrollBy(0, 500)')

        wait = WebDriverWait(self.driver, 15, 1, ignored_exceptions=[NoSuchElementException, TimeoutException,
                                                                     ElementClickInterceptedException])
        # Enter name:-
        username_input = wait.until(EC.visibility_of_element_located((By.XPATH, test_data.TestSelectors.input_name)))
        username_input.send_keys(test_data.TestData.name)
        self.driver.execute_script('window.scrollBy(0, 500)')

        # Birthdate:-
        Birthdate_input = wait.until(EC.visibility_of_element_located((By.XPATH, test_data.TestSelectors.input_birthdate)))
        Birthdate_input.send_keys(test_data.TestData.birthdate)

        # To --(Birthdate):-
        Birthdate_to_input = wait.until(EC.visibility_of_element_located((By.XPATH, test_data.TestSelectors.
                                                                          input_birthdate1)))
        Birthdate_to_input.send_keys(test_data.TestData.birthdate1)
        self.driver.execute_script('window.scrollBy(0, 500)')

        # Awards & recognition:-
        oscar_winning = wait.until(EC.element_to_be_clickable((By.XPATH, test_data.TestSelectors.awards_xpath)))
        self.driver.execute_script("arguments[0].click();", oscar_winning)
        self.driver.execute_script('window.scrollBy(0, 1000)')
        #
        # # Gender Identity(Male):
        Gender_identity = wait.until(EC.element_to_be_clickable((By.XPATH, test_data.TestSelectors.gender_male_xpath)))
        self.driver.execute_script("arguments[0].click();", Gender_identity)
        #
        # # Click on See Results:-
        see_results = wait.until(EC.element_to_be_clickable((By.XPATH, test_data.TestSelectors.see_result_xpath)))
        self.driver.execute_script("arguments[0].click();", see_results)
        print('Success name search')
        self.driver.quit()