import time

from selenium.webdriver.common.by import By


class SigninPage:
    def __init__(self, driver):
        self.driver = driver

        self.email_name = (By.NAME, "email")
        self.password_name = (By.NAME, "password")
        self.login_button_xpath = (By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained "
                                             "MuiButton-containedPrimary MuiButton-sizeMedium "
                                             "MuiButton-containedSizeMedium MuiButton-fullWidth MuiButton-root "
                                             "MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium "
                                             "MuiButton-containedSizeMedium MuiButton-fullWidth mui-style-qv8acy']")

    def for_login(self, email, password):
        self.driver.find_element(*self.email_name).send_keys(email)
        self.driver.find_element(*self.password_name).send_keys(password)
        self.driver.find_element(*self.login_button_xpath).click()

        time.sleep(2)
