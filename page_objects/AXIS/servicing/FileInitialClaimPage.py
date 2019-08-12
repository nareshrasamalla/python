from commons.WebPage import WebPage
import selenium.common.exceptions,time
from selenium.webdriver.common.by import By

class FileInitialClaimPage(WebPage):

    def __init__(self,driver,testDataHolder):
        super(FileInitialClaimPage, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.fileInitialClaimHeading_xpath = "//span[text()='File Initial Claim']"
        self.titletransferEventShortSale = "//input[@id='shortsaleref']"
        self.titleTransferDate_xpath = "//input[@id='title-transfer-date']"
        self.netSaleProceeds = "//input[@id='net-sale-proceeds']"
        self.valuationType_xpath = "//select[@id='valuation-type']/following::a[1]"  #
        self.investorType_xpath = "//select[@id='investorOption']/following::a[1]"
        self.currentValue_xpath = "//input[@id='current-value']"
        self.valuationDate = "//input[@id='valuation-date']"
        self.nextBtn_xpath = "//span[@id='file-claim-next-button']/a"
        self.serviccerCommnets_xpath = "(//div[contains(text(),'Servicer Comment')]/following::div/textarea)[1]"
        self.nmiComment_xpath = "(//div[contains(text(),'National MI Comment')]/following::div/textarea)[1]"
        self.submittedBy_xpath = "//input[@id='claim-submitted-by']"
        self.acknowledgementsLeftPanel_xpath = "//a[text()='Acknowledgements']"
        self.acceptAcknowledge_xpath = "//h3[text()=' Acknowledgements']/following::input[1]"
        self.fileClaim_xpath = "//span[@id='file-claim-button']/a"
        self.noDocsUploadAlert_xpath = "//div[@id='claim-no-document-overlay']"
        self.noDocsUploadAlertYes_xpath = "//div[@id='claim-no-document-overlay']//a[text()='Yes']"
        self.createClaimAlertyes_xpath = "//div[@id='claimActionPopup']//a[text()='Yes']"
        self.checkPage()


    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.fileInitialClaimHeading_xpath).is_displayed():
            pass
        else:
            print("FileNoticeOfDefault Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def fileInitialClaim(self):
        time.sleep(5)
        self.click(self.titletransferEventShortSale)
        self.sendKeys(self.titleTransferDate_xpath,self.tdh['File Initial Claim-Title Transfer Date'])
        self.click(self.fileInitialClaimHeading_xpath)
        self.sendKeys(self.netSaleProceeds,str(self.tdh['File Initial Claim-Net Sale Proceeds']))
        self.click(self.investorType_xpath)
        self.click("//li/a[text()='"+self.tdh['File Initial Claim-Investor']+"']")
        self.click(self.valuationType_xpath)
        self.click("//li/a[text()='" + self.tdh['File Initial Claim-Valuation Type'] + "']")
        self.sendKeys(self.currentValue_xpath,self.tdh['File Initial Claim-Current Value'])
        self.sendKeys(self.valuationDate,self.tdh['File Initial Claim-Valuation Date'])
        self.clickNext()
        time.sleep(2)
        self.click(self.createClaimAlertyes_xpath)
        time.sleep(5)
        self.clickNext()
        self.sendKeys(self.serviccerCommnets_xpath,self.tdh['File Initial Claim-Servicer Comment'])
        self.sendKeys(self.nmiComment_xpath, self.tdh['File Initial Claim-National MI Comment'])
        self.sendKeys(self.submittedBy_xpath, self.tdh['File Initial Claim-Submitted By'])
        self.acceptAcknowledgements()
        self.click(self.fileClaim_xpath)
        self.noDocsUploadAlert()

    def noDocsUploadAlert(self):
        time.sleep(4)
        if self.isDisplayed(self.noDocsUploadAlert_xpath):
            self.click(self.noDocsUploadAlertYes_xpath)


    def acceptAcknowledgements(self):
        self.click(self.acknowledgementsLeftPanel_xpath)
        time.sleep(2)
        self.click(self.acceptAcknowledge_xpath)

    def clickNext(self):
        self.click(self.nextBtn_xpath)
        time.sleep(2)