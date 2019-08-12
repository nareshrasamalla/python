from commons.WebPage import WebPage
import selenium.common.exceptions,time
from selenium.webdriver.common.by import By

class FileNoticeOfDefaultPage(WebPage):

    def __init__(self,driver,testDataHolder):
        super(FileNoticeOfDefaultPage, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.fileNoticeOfDefaultHeading_xpath = "//span[text()='File Notice of Default']"
        self.defaultDate_xpath = "//input[@id='initialDefaultDate']"
        self.submittedBy_xpath = "//input[@id='submittedBy']"
        self.submitBtn_xpath = "//a[@id='saveOrUpdadateNOD']"
        self.checkPage()


    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.fileNoticeOfDefaultHeading_xpath).is_displayed():
            pass
        else:
            print("FileNoticeOfDefault Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def updateDefaultDate(self):
        self.sendKeys(self.defaultDate_xpath,self.tdh['File Notice of Default-Default Date'])


    def fileNOD(self):
        self.updateDefaultDate()
        self.scrollToBottom()
        self.sendKeys(self.submittedBy_xpath,self.tdh['File Notice of Default-Submitted By'])
        self.click(self.submitBtn_xpath)

