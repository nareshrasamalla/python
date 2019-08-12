from commons.WebPage import WebPage
import selenium.common.exceptions,time
from selenium.webdriver.common.by import By

class CertificateDetailsPage(WebPage):

    def __init__(self,driver,testDataHolder):
        super(CertificateDetailsPage, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.certificateDetailsHeadingText_xpath = "//section/h3[contains(text(),'Certificate')]"
        self.updateLoanCloseDateLink_xpath = "//li[@id='updateLoanCloseDate']/a"
        self.fileNoticeOfDefaultLink_xpath = "//a[text()='File Notice of Default']"
        self.loanStatus_xpath = "(//span[@id='loanStatus'])[2]"
        self.fileInitialClaim_xpath = "//li[@id='file-initial-claim']/a"
        self.reviewInitialClaim_xpath = "//li[@id='review-initial-claim']/a"
        self.checkPage()

    def clickUpdateLoanClosedDate(self):
        time.sleep(10)
        self.click(self.updateLoanCloseDateLink_xpath)
        time.sleep(5)

    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.certificateDetailsHeadingText_xpath).is_displayed():
            pass
        else:
            print("Application Details Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def clickFileNoticeOfDefault(self):
        self.click(self.fileNoticeOfDefaultLink_xpath)
        time.sleep(7)

    def getLoanStatus(self):
        self.scrollUpToElement(self.loanStatus_xpath)
        return self.getText(self.loanStatus_xpath)

    def clickFileInitialClaim(self):
        time.sleep(5)
        self.click(self.fileInitialClaim_xpath)
        time.sleep(5)

    def clickReviewInitialClaim(self):
        time.sleep(15)
        self.click(self.reviewInitialClaim_xpath)
        time.sleep(5)