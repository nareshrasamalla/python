from selenium.webdriver.common.by import By
from commons.WebPage import WebPage
import selenium.common.exceptions,time

class VendorManagementPage(WebPage):

    def __init__(self,driver,testDataHolder):
        super(VendorManagementPage, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.noOfCertiReadyText_xpath = "//span[text()='Number of Certificates ready for assignment: ']"
        self.sendNow_xpath = "//a[contains(text(),'Send')]"
        self.sendBtn_xpath = "//span[@id='sendSendNow']/a"
        self.checkPage()


    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.noOfCertiReadyText_xpath).is_displayed():
            pass
        else:
            print("Application Details Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def clickSendNow(self):
        self.click(self.sendNow_xpath)
        time.sleep(5)

    def sendNow(self):
        self.clickSendNow()
        self.click(self.sendBtn_xpath)
