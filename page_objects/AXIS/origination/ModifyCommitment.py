from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from commons.WebPage import WebPage
import selenium.common.exceptions,time

class ModifyCommitment(WebPage):

    def __init__(self,driver,testDataHolder):
        super(ModifyCommitment, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.mortgageInsuranceInformationTab_xpath = "//div[contains(text(),'Mortgage Insurance Information')]"
        self.modifyCommitment_xpath = "//span[text()='Modify Commitment']"
        self.collapseAll_xpath = "//div[@id='modify-commitment']/div/h2/a[@title='Click to Collapse']"
        self.coverageDropDown_xpath = "//select[@id='proposed-coverage-percentage']/following::a[1]"
        self.updateCommitmentBtn_xpath = "//a[text()='Update Commitment']"
        self.comments_xpath = "//textarea[@id='modify-commitment-comment']"
        self.acceptViewCommitment_xpath = "//a[@id='acceptAndViewCommitmentId']"
        self.checkPage()


    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.modifyCommitment_xpath).is_displayed():
            pass
        else:
            print("Application Details Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException


    def collapseAll(self):
        #self.scrollDownToElement(self.collapseAll_xpath)
        self.click(self.collapseAll_xpath)

    def modifyCoverage(self):
        time.sleep(5)
        self.collapseAll()
        time.sleep(5)
        self.click(self.mortgageInsuranceInformationTab_xpath)
        time.sleep(5)
        self.click(self.coverageDropDown_xpath)
        time.sleep(3)
        self.click("(//a[text()='"+self.tdh['Mortgage Insurance Information-Coverage']+"'])[2]")
        self.clickUpdateCommitment()
        time.sleep(5)
        self.addComments()
        self.clickAcceptViewCommitment()

    def clickUpdateCommitment(self):
        time.sleep(2)
        self.click(self.updateCommitmentBtn_xpath)
        time.sleep(5)

    def addComments(self):
        self.sendKeys(self.comments_xpath,self.tdh['Modify Commitment-Comments'])

    def clickAcceptViewCommitment(self):
        self.click(self.acceptViewCommitment_xpath)
        time.sleep(15)
        self.driver.switch_to.window(self.driver.window_handles[0])


