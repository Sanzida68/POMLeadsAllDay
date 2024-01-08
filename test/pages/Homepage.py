from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.signup_button_xpath = (By.XPATH, "//button[@class='sc-hLclGa eiOLAt']")
        self.sign_in_button_xpath = (By.XPATH, "//button[@class='sc-hLclGa inSyvO me-4']")

    def for_signin_page(self, url):
        self.driver.get(url)
        self.driver.find_element(*self.sign_in_button_xpath).click()

    def for_signup_page(self, url):
        self.driver.get(url)
        self.driver.find_element(*self.signup_button_xpath).click()
