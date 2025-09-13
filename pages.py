from selenium import webdriver
from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    ADDRESS_FROM = (By.ID, "from")
    ADDRESS_TO = (By.ID, "to")
    PHONE_NUMBER = (By.ID, "phoneNumber")
    PAYMENT = (By.ID, "payment")
    MESSAGE = (By.ID, "message")
