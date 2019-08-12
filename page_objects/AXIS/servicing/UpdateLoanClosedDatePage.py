from commons.WebPage import WebPage
import selenium.common.exceptions,time
from selenium.webdriver.common.by import By


class UpdateLoanClosedDate(WebPage):

    def __init__(self, driver, testDataHolder):
        super(UpdateLoanClosedDate, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.newLoanClosedDate_xpath = "//input[@id='newLoanCloseDate']"
        self.updateLCDCommnets_xpath = "//textarea[@id='ulcd-comment']"
        self.submitUpdateLCD_xpath = "//span[@id='submitLoanClosedBtn']/a"
        self.axisAlertOk_xpath = "//button[text()='Ok']"
        self.updateLCDText_xpath ="//span[text()='Update Loan Closed Date']"
        self.checkPage()


    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.updateLCDText_xpath).is_displayed():
            pass
        else:
            print("Application Details Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def updateLoanCloseDate(self):
        time.sleep(5)
        self.sendKeys(self.newLoanClosedDate_xpath,self.tdh['Update Loan Closed Date-New Loan Closed Date'])
        self.sendKeys(self.updateLCDCommnets_xpath,self.tdh['Update Loan Closed Date-Comment'])
        self.click(self.submitUpdateLCD_xpath)
        time.sleep(20)

    def handleAxisAlert(self):
        self.waitTillPresenceAndClick(self.axisAlertOk_xpath)

