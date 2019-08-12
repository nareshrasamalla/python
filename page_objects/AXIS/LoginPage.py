from commons import LoginActions
from commons import WebPage
from selenium.webdriver.common.by import By
import selenium.common.exceptions


class LoginPage(WebPage.WebPage):

    def __init__(self,driver,testDataHolder):
        super(LoginPage,self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.axisUsername_xpath = "//input[@id='username']"
        self.axisPassword_xpath = "//input[@id='password']"
        self.submit_xpath = "//input[@id='submitBtn']"
        self.logoutBtn_xpath = "//a[@id='logout']"
        self.checkPage()

    def loginAs(self,user=''):
        loginAct = LoginActions.LoginToAxis(self.tdh)
        userName, Password = loginAct.logintoAxis(user)
        self.sendKeys(self.axisUsername_xpath,userName)
        self.sendKeys(self.axisPassword_xpath, Password)
        self.click(self.submit_xpath)
        # self.driver.find_element(By.NAME, self.axisUsername_name).send_keys(userName)
        # self.driver.find_element(By.ID,self.axisPassword_name).send_keys(Password)
        # self.driver.find_element(By.ID,self.submit_name).click()


    def checkPage(self):
        if self.isDisplayed(self.axisUsername_xpath):
            pass
        else:
            print("Landing page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def logOut(self):
        self.click(self.logoutBtn_xpath)
        print("Logged out from application successfully.")