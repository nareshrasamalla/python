from selenium.webdriver.common.by import By
from commons.WebPage import WebPage
import selenium.common.exceptions,time

class PostCloseReviewTab(WebPage):

    def __init__(self,driver,testDataHolder):
        super(PostCloseReviewTab, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.pcrTabStatusText_xpath = "//label[@class='font-size-23 font-weight-700 inline-block']/following::span[text()='Status']"
        self.pcrTabStatus_xpath = "(//label[@class='font-size-23 font-weight-700 inline-block'])[1]"
        self.updateStatus_xpath = "//a[text()='Update Status']"
        self.statusLink_xpath = "//select[@id='pcr-status']/following::a[1]"
        self.statusComments = "//textarea[@id='review-status-update-comments']"
        self.checkPage()


    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.pcrTabStatusText_xpath).is_displayed():
            pass
        else:
            print("Application Details Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def verifyPCRStatus(self, expectedStatus):
        self.assertText(self.pcrTabStatus_xpath,expectedStatus,"PCR Flow Current status is not updated.")

    def updateStatus(self):
        self.click(self.updateStatus())
        self.click(self.statusLink_xpath)
        self.click("(//a[text()='"+self.tdh['Update Status-Status']+"'])[2]")
        self.sendKeys(self.statusComments,self.tdh['Update Status-Comment'])
