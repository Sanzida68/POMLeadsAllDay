from selenium.webdriver.common.by import By


class SignupPage:
    def __init__(self, driver):
        self.driver = driver

        self.full_name = (By.NAME, "fullName")
        self.brokerage_name = (By.NAME, "brokerage")
        self.email_name = (By.NAME, "email")
        self.mobile_name = (By.NAME, "mobileNumber")
        self.address_name = (By.NAME, "address")
        self.province_field_xpath = (By.XPATH, "//div[@class='w-100 position-relative']")
        self.city_name = (By.NAME, "city")
        self.postal_code_name = (By.NAME, "postalCode")
        self.agree_name = (By.NAME, "agreement")
        self.submit_xpath = (By.XPATH, "//button[@class='sc-gKHVLF jdfJhN mt-4']")
        self.holder_name = (By.NAME, "cardHolderName")
        self.card_no_name = (By.NAME, "cardNumber")
        self.exp_date_name = (By.NAME, "cardExpireYear")
        self.cvc_name = (By.NAME, "cardCvc")
        #elf.submit1_xpath = (By.XPATH, "//button[@class='sc-gKHVLF jdfJhN mt-4']")
        #self.submit2_xpath = (By.XPATH, "//button[@class='sc-gKHVLF jdfJhN mt-4']")

    def for_signin(self, fn, br, email_add, m, add, city, pc, ch, cn, ex, cv):
        self.driver.find_element(*self.full_name).send_keys(fn)
        self.driver.find_element(*self.brokerage_name).send_keys(br)
        self.driver.find_element(*self.email_name).send_keys(email_add)
        self.driver.find_element(*self.mobile_name).send_keys(m)
        self.driver.find_element(*self.address_name).send_keys(add)
        self.driver.find_element(*self.province_field_xpath).click()

        for x in range(1, 11):
            a = f"//ul[@class='sc-fEyylQ eNreKR']//li[@class='sc-idyqAC cBRBVe'][{x}]"
            element = self.driver.find_element(By.XPATH, a)
            c = element.text

            if c == "Nova Scotia":
                element.click()
                break

        self.driver.find_element(*self.city_name).send_keys(city)
        self.driver.find_element(*self.postal_code_name).send_keys(pc)
        self.driver.find_element(*self.agree_name).click()
        self.driver.find_element(*self.submit_xpath).click()
        self.driver.find_element(*self.holder_name).send_keys(ch)
        self.driver.find_element(*self.card_no_name).send_keys(cn)
        self.driver.find_element(*self.exp_date_name).send_keys(ex)
        self.driver.find_element(*self.cvc_name).send_keys(cv)
        #self.driver.find_element(*self.submit1_xpath).click()
        #self.driver.find_element(*self.submit2_xpath).click()

