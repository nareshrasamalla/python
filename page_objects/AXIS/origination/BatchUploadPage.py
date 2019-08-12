from commons.WebPage import WebPage
import selenium.common.exceptions,time
from selenium.webdriver.common.by import By

class BatchUploadPage(WebPage):

    def __init__(self,driver,testDataHolder):
        super(BatchUploadPage, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.vendorDropDown = "//label[text()='Vendor ']/following::a[1]"
        self.batchUploadHeading_xpath = "//div[@id='batch-upload-vendor']/section/h2[text()='Batch Upload']"
        self.uploadWorksheetBtn_xpath = "//span[@id='upload-vendor-worksheet']/a"
        self.uploadWorksheetPopUpHeading_xpath = "//span[text()='Upload Worksheet']"
        self.browseBtn_xpath = "//input[@accept='.xls, .xlsx']"
        self.uploadBtn_xpath = "//button[@id='upload-worksheet-upload']/a"
        self.submitUploadSheet_xpath = "//span[@id='upload-vendor-submit']/a"
        self.checkPage()


    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.batchUploadHeading_xpath).is_displayed():
            pass
        else:
            print("Application Details Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def selectVendor(self):
        self.click(self.vendorDropDown)
        self.click("//li/a[text()='"+self.tdh['Batch Upload-Vendor']+"']")

    def uploadWorksheet(self):

        if self.isDisplayed(self.uploadWorksheetBtn_xpath):
            self.click(self.uploadWorksheetBtn_xpath)
            if self.isDisplayed(self.uploadWorksheetPopUpHeading_xpath):
                self.driver.find_element(By.XPATH,self.browseBtn_xpath).send_keys(self.tdh['Batch Upload-Sheet Path'])
                self.click(self.uploadBtn_xpath)
                self.click(self.submitUploadSheet_xpath)





