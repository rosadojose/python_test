<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage
import helpers
import data
=======
import data
from selenium import webdriver
from pages import UrbanRoutesPage
import helpers

>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
<<<<<<< HEAD
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.URBAN_ROUTES_URL)

=======
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://cnt-c14b4ed8-3556-499c-b095-3678b12b58ce.containerhub.tripleten-services.com")
        cls.pages = UrbanRoutesPage(cls.driver)
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
<<<<<<< HEAD
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        self.pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

=======
        self.pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
        from_input = self.pages.driver.find_element(*self.pages.FROM_LOCATOR)
        to_input = self.pages.driver.find_element(*self.pages.TO_LOCATOR)
        assert from_input.get_attribute("value") == data.ADDRESS_FROM, \
            f"Expected 'From' address to be {data.ADDRESS_FROM}, but got {from_input.get_attribute('value')}"
        assert to_input.get_attribute("value") == data.ADDRESS_TO, \
            f"Expected 'To' address to be {data.ADDRESS_TO}, but got {to_input.get_attribute('value')}"

    def test_select_supportive_plan(self):
<<<<<<< HEAD
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
=======
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
        self.pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.pages.click_call_taxi()
        self.pages.fill_phone_number(data.PHONE_NUMBER)
        self.pages.fill_card_number(data.CARD_NUMBER)
        self.pages.select_supportive_plan()
        self.pages.fill_message(data.MESSAGE_FOR_DRIVER)
<<<<<<< HEAD
        assert selected_plan.text == "Supportive", "Supportive plan should be selected"


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
=======


    def test_fill_phone_number(self):
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
        self.pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.pages.click_call_taxi()  # open the form
        self.pages.fill_phone_number(data.PHONE_NUMBER)
        phone_input = self.pages.driver.find_element(*self.pages.PHONE_NUMBER_LOCATOR)
        assert phone_input.get_attribute("value") == data.PHONE_NUMBER

    def test_add_credit_card(self):
<<<<<<< HEAD
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
=======
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
        self.pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.pages.click_call_taxi()
        self.pages.fill_phone_number(data.PHONE_NUMBER)
        self.pages.select_supportive_plan()
<<<<<<< HEAD
        self.pages.fill_card_number(data.CARD_NUMBER)
        self.pages.fill_card_code(data.CARD_CODE)
        assert self.pages.is_link_button_clickable(), "Link button should be clickable after valid card input"
        self.driver.find_element(*self.LINK_BUTTON).click()
=======
        self.pages.select_card_payment_method()
        self.pages.fill_card_number(data.CARD_NUMBER)
        self.pages.fill_card_code(data.CARD_CODE)
        self.pages.focus_out_of_card_fields()
        assert self.pages.is_link_button_clickable(), "Link button should be clickable after valid card input"
        self.pages.click_link_button()
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
        payment_method_element = self.pages.driver.find_element(*self.pages.PAYMENT_METHOD_LOCATOR)
        assert payment_method_element.text == "Card", \
            "Payment method should be updated to 'Card' after adding a credit card"

    def test_comment_for_driver(self):
<<<<<<< HEAD
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
=======
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
        self.pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.pages.click_call_taxi()  # ensures the message field is visible
        self.pages.fill_message(data.MESSAGE_FOR_DRIVER)
        message_element = self.pages.driver.find_element(*self.pages.MESSAGE_LOCATOR)
        assert message_element.get_attribute("value") == data.MESSAGE_FOR_DRIVER, \
            "Driver message should match the input"

    def test_order_blanket_and_handkerchiefs(self):
<<<<<<< HEAD
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
=======
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
        self.pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.pages.click_call_taxi()
        self.pages.carmodel()
        self.pages.blankets_and_handerchiefs()
<<<<<<< HEAD
        slider_element = self.pages.driver.find_element(*self.pages.BLANKETS_AND_HANDKERCHIEFS)
        assert slider_element.get_property('checked'), "Blankets and handkerchiefs should be selected"

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi()
        routes_page.carmodel()

        for _ in range(2):
            routes_page.click_ice_cream()

        count = routes_page.get_ice_cream_count()
=======
        slider_element = self.pages.driver.find_element(*self.pages.BLANKETS_AND_HANDKERCHIEFS_LOCATOR)
        assert slider_element.get_property('checked'), "Blankets and handkerchiefs should be selected"

    def test_order_2_ice_creams(self):
        self.pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.pages.click_call_taxi()
        self.pages.carmodel()
        for _ in range(2):
            self.pages.click_ice_cream()
        count = self.pages.get_ice_cream_count()
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
        assert count == 2, f"Expected 2 ice creams, got {count}"

    def test_call_taxi(self):
        self.pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
<<<<<<< HEAD

=======
        self.pages.click_call_taxi()

        assert phone_input.is_displayed(), "Phone number field should be visible after calling taxi"
>>>>>>> 3613ed2cbf07b43d445a08137fb6dfcb533227f1
