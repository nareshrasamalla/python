from commons.WebPage import WebPage
import selenium.common.exceptions,time
from selenium.webdriver.common.by import By

class ReviewInitialClaim(WebPage):

    def __init__(self,driver,testDataHolder):
        super(ReviewInitialClaim, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.reviewInitialClaimHeading_xpath = "//span[text()='Review Initial Claim']"
        self.nmiComments_xpath = "//div[contains(text(),'National MI Comment')]/following::textarea"
        self.nextBtn_xpath = "//span[@id='file-claim-next-button']/a"
        self.perfectBtn_xpath = "//span[@id='perfect-claim-button']/a"
        self.perfectAlertAccept_xpath = "//span[@id='perfectclaimbutton']/a"
        self.perfectAlertSection_xpath = "//div[@id='perfectoverlaysection']"
        self.percentageSettlement_xpath = "//input[@value='PCT']"
        self.recommendClaimCheckBox_xpath = "(//div[@id='claim-decision-container']//input)[1]"
        self.recommendclaimComment_xpath = "//span[text()='Comment']/following::textarea"
        self.recommendClaimBtn_xpath = "//span[@id='recommend-claim-button']/a"
        self.checkPage()


    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.reviewInitialClaimHeading_xpath).is_displayed():
            pass
        else:
            print("FileNoticeOfDefault Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def reviewInititalClaim(self):
        time.sleep(5)
        self.scrollToBottom()
        self.sendKeys(self.nmiComments_xpath,self.tdh['Review Initial Claim-National MI Comment'])
        self.clickNxtBtn()
        self.clickNxtBtn()
        self.clickPerfectBtn()
        self.perfectClaimAlert()
        self.clickNxtBtn()

    def perfectClaimAlert(self):
        if self.isDisplayed(self.perfectAlertSection_xpath):
            self.click(self.perfectAlertAccept_xpath)

    def clickNxtBtn(self):
        time.sleep(8)
        self.click(self.nextBtn_xpath)
        time.sleep(8)

    def clickPerfectBtn(self):
        self.click(self.perfectBtn_xpath)
        time.sleep(5)

    def recommendClaim(self):
        time.sleep(5)
        self.click(self.percentageSettlement_xpath)
        self.scrollToBottom()
        self.click(self.recommendClaimCheckBox_xpath)
        self.sendKeys(self.recommendclaimComment_xpath,self.tdh['Recommend Initial Claim-National MI Comment'])
        self.click(self.recommendClaimBtn_xpath)