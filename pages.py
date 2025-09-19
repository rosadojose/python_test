from typing import Any

import data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from data import CARD_CODE


class UrbanRoutesPage:
    # -----Locators-----
    FROM_LOCATOR = (By.ID, "from")
    TO_LOCATOR = (By.ID, "to")
    PHONE_NUMBER_LOCATOR = (By.CLASS_NAME, "phonenumber")
    CARD_NUMBER_LOCATOR = (By.XPATH, "//input[@name = 'cardnumber']")
    MESSAGE = (By.CSS_SELECTOR, "textarea.comment")
    ICE_CREAM_BUCKET_LOCATOR = (By.XPATH, "//input[@name = 'icecreambucket']")
    CALL_TAXI_BUTTON_LOCATOR = (By.ID, "call-taxi")
    CAR_MODEL_RESULT_LOCATOR = (By.CLASS_NAME, "carmodel")
    SELECT_SUPPORTIVE_PLAN = (By.CLASS_NAME, "selectplan")
    BLANKETS_AND_HANDKERCHIEFS = (By.CLASS_NAME, "blanket")
    CARD_CODE = (By.XPATH, "//input[@name = 'cardcode']")
    LINK_BUTTON_LOCATOR = (By.XPATH, "//input[@name = 'linkbutton']")
    PAYMENT_METHOD_LOCATOR: tuple[Any, str] = (By.XPATH, "//input[@name = 'paymentmethod']")
    #-----Methods-----
    def __init__(self, driver):
               self.driver = driver

    def set_route(self, address_from, address_to):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(address_from)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(address_to, Keys.RETURN)

    def click_call_taxi(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON_LOCATOR).click()

    def fill_phone_number(self, number):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).send_keys(number)

    def fill_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)

    def fill_message(self, message):
        self.driver.find_element(*self.MESSAGE).send_keys(message)

    def order_ice_cream(self, count):
        for _ in range(count):
            self.driver.find_element(*self.ICE_CREAM_BUCKET_LOCATOR).click()

    def get_car_model_text(self):
        return self.driver.find_element(*self.CAR_MODEL_RESULT_LOCATOR).text

    def select_supportive_plan(self):
        plan_element = self.driver.find_element(*self.SELECT_SUPPORTIVE_PLAN)
        plan_element.click()

    def blankets_and_handerchiefs(self):
            self.driver.find_element(*self.BLANKETS_AND_HANDKERCHIEFS).click()

    def fill_card_code(self):
        self.driver.find_element(*self.CARD_CODE).send_keys(CARD_CODE)

    def link_button(self):
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()
        
    def payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def is_link_button_clickable(self):
        pass

    def carmodel(self):
        pass

    def click_ice_cream(self):
        pass

    def get_ice_cream_count(self):
        pass
