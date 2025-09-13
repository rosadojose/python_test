def in_autotests_we_trust(a, b):
    if a == b:
        print('PASS')
    else:
        print('FAIL')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)


@classmethod
def setup_class(cls):
    # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
    from selenium.webdriver import DesiredCapabilities
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
    cls.driver = webdriver.Chrome()

 @classmethod
    def teardown_class(cls):
        cls.driver.quit()

