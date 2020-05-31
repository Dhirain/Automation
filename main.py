from selenium import webdriver
from time import sleep
import credential as c

class HelloBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        print('Open HelloFresh')
        self.driver.get('https://hellofresh.de')
        sleep(2)
        print("click on accepting cookies")
        self.driver.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]').click()
        print("click on login Button")
        self.driver.find_element_by_xpath("//a[contains(@href,'/login')]").click()
        print('open login screen')
        sleep(4)

    def open_login(self,userid,password):
        print('Enter Email')
        self.driver.find_element_by_xpath("//input[@type=\"email\"]").send_keys(userid)
        print('Enter password')
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        print("open plan screen")
        sleep(4)

    def select_plan(self):
        print("Select Veggie box")
        self.driver.find_element_by_xpath("//button[@data-test-id=\"veggie-box-t4-family\"]").click()
        sleep(1)
        print("Apply coupon code")
        self.driver.find_element_by_xpath("//input[@data-test-id=\"promo-input\"]").send_keys('NEW')
        self.driver.find_element_by_xpath("//button[@data-test-id=\"promo-button\"]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[@data-test-id=\"select-plan-button\"]").click()
        print("Open delivery screen")
        sleep(7)

    def delivery(self):
        print("Enter Details")
        self.driver.find_element_by_xpath("//input[@data-test-id=\"first-name-field\"]").send_keys('Dhirain')
        self.driver.find_element_by_xpath("//input[@data-test-id=\"last-name-field\"]").send_keys('Jain')
        self.driver.find_element_by_xpath("//input[@id=\"address-address1Street\"]").send_keys('Saarbrücker Str.')
        self.driver.find_element_by_xpath("//input[@id=\"address-address1No\"]").send_keys('37')
        self.driver.find_element_by_xpath("//input[@id=\"address-postcode\"]").send_keys('10405')
        self.driver.find_element_by_xpath("//input[@id=\"address-city\"]").send_keys('Berlin')
        self.driver.find_element_by_xpath("//input[@id=\"address-phone\"]").send_keys('+491111111111')
        sleep(2)
        self.driver.find_element_by_xpath("//button[@data-test-id=\"next-step-button\"]").click()
        sleep(4)


hellofresh_bot = HelloBot()
hellofresh_bot.open_login(c.username, c.password)
hellofresh_bot.select_plan()
hellofresh_bot.delivery()
input("press close to exit")