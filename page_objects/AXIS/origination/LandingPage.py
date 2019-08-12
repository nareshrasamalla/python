from selenium.webdriver.common.by import By
from commons.WebPage import WebPage
import selenium.common.exceptions,time

class LandingPage(WebPage):

    def __init__(self,driver,testDataHolder):
        super(LandingPage, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.searchappTextBar_xpath = "//input[@id='txtSearchCertificate']"
        self.searchappBtn_xpath = "//a[@id='quickSearchButton']"
        self.homeTabLink_xpath = "//div[@id='app-nav']//span[contains(text(),'Home')]"
        self.batchUploadLink_xpath = "//a[@id='axis-o-batchUploadVendor']"
        self.userAdministrationDropDown_xpath = "//a[@id='axis-o-userAdminHeader']"
        self.runScheduledJobs_xpath = "//a[@id='axis-o-schedJobs']"
        self.checkPage()

    def checkPage(self):
        if self.isDisplayed(self.homeTabLink_xpath):
            pass
        else:
            print("Landing page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def searchApplication(self,applicationNumber):
        self.sendKeys(self.searchappTextBar_xpath,applicationNumber)
        self.driver.implicitly_wait(30)
        self.click(self.searchappBtn_xpath)
        self.driver.implicitly_wait(30)

    def clickBatchUpload(self):
        self.click(self.batchUploadLink_xpath)
        time.sleep(5)

    def clickRunScheduledJobs(self):
        self.clickUserAdministration()
        self.click(self.runScheduledJobs_xpath)

    def clickUserAdministration(self):
        self.click(self.userAdministrationDropDown_xpath)

