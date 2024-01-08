from selenium.webdriver.common.by import By


class AccountActivePage:
    def __init__(self, driver):
        self.driver = driver

        self.ac_password_name = (By.NAME, "password")
        self.ac_confirm_password_name = (By.NAME, "confirmPassword")
        self.ac_set_button_xpath = (By.XPATH, "//button[@class='sc-gKHVLF jdfJhN mt-4']")

    def set_password(self, ps):
        self.driver.find_element(*self.ac_password_name).send_keys(ps)

    def set_con_password(self, cp):
        self.driver.find_element(*self.ac_confirm_password_name).send_keys(cp)

    def set_button(self):
        self.driver.find_element(*self.ac_set_button_xpath).click()

    def for_activation(self, url, ps, cp):
        self.driver.get(url)
        self.driver.find_element(*self.ac_password_name).send_keys(ps)
        self.driver.find_element(*self.ac_confirm_password_name).send_keys(cp)
        #self.driver.find_element(*self.ac_set_button_xpath).click()

