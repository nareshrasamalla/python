from selenium.webdriver.common.by import By
from commons.WebPage import WebPage
import selenium.common.exceptions,time

class ApplicationDetailsPage(WebPage):

    def __init__(self,driver,testDataHolder):
        super(ApplicationDetailsPage, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.actionsAvailableHeader_xpath = "//h3[text()='Actions Available']"
        self.pricingInformationTab_xpath = "//div[contains(text(),'Pricing Information')]"
        self.totalInitialRateLabel_xpath = "(//label[text()='Total Initial Rate'])[1]"
        self.totalInitialRate_xpath = "(//label[text()='Total Initial Rate'])[1]/following::span[1]"
        self.totalInitialRateDropDown_xpath = "(//label[text()='Total Initial Rate'])[1]/following::a[1]"
        self.adjustersElements_xpath = "//span[@class='marL2 inline-block-i maxwidth135']"
        self.adjustersRate_xpath = "//span[@class='pad5n3 binding-na width95 inline-block-i']/span"
        self.collapseAll_xpath = "//a[@title='Click to Collapse']"
        self.modifyCommitmentLink_xpath = "//a[text()='Modify Commitment']"
        self.cancelSendNMIDecision_xpath = "//span[@id='cancelDecisionEmail']/a"
        self.advanceWorkflowLink_xpath = "//li[@id='pcrAdvanceWorkflowLink']/a"
        self.advanceWorkflowComments_xpath = "//textarea[@id='pcr_assign_comment']"
        self.advanceWorkflowAssignTo_xpath = "//select[@id='pcrAssignToDropdown']/following::a/span[1]"
        self.postCloseReviewTab_xpath = "//li[@id='pcrPostSubmit']/a"
        self.advanceWorkFlowSubmit = "//span[@id='pcr_assign_submit']/a"
        self.checkPage()

    def checkPage(self):
        if self.driver.find_element(By.XPATH, self.actionsAvailableHeader_xpath).is_displayed():
            pass
        else:
            print("Application Details Page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException

    def verifyTotalInitialRateDetails(self):
        time.sleep(4)
        self.collapseAll()
        time.sleep(4)
        self.click(self.pricingInformationTab_xpath)
        time.sleep(2)
        self.scrollDownToElement(self.pricingInformationTab_xpath)
        time.sleep(2)
        if self.isDisplayed(self.totalInitialRateLabel_xpath):
            self.assertText(self.totalInitialRate_xpath,self.tdh["Pricing Information - Before Resubmission-Total Initial Rate"], 'Total Initial Rate is not as expected')
            self.clickTotalInitialRateDropDownDetails()
            self.compareAdjusters()

    def verifyTotalInitialRateDetailsAfterSub(self):
        time.sleep(2)
        self.collapseAll()
        time.sleep(5)
        self.click(self.pricingInformationTab_xpath)
        self.scrollDownToElement(self.pricingInformationTab_xpath)
        time.sleep(2)
        if self.isDisplayed(self.totalInitialRateLabel_xpath):
            self.assertText(self.totalInitialRate_xpath, self.tdh["Pricing Information - After Resubmission-Total Initial Rate"], 'Total Initial Rate is not as expected')
            self.clickTotalInitialRateDropDownDetails()
            uiAdjusters = self.getAdjustersWithRatesfromUI()
            tdhAdjusters = self.getAdjustersWithRatesfromTDHAfterSub()
            try:
                assert uiAdjusters == tdhAdjusters
                print("Actual Adjusters:")
                print(uiAdjusters)
                print("Expected Adjusters")
                print(tdhAdjusters)
            except:
                print("Actual Adjusters:")
                print(uiAdjusters)
                print("Expected Adjusters")
                print(tdhAdjusters)
                print("Assertion Failure.")


    def collapseAll(self):
        self.scrollDownToElement(self.collapseAll_xpath)
        self.click(self.collapseAll_xpath)

    def clickTotalInitialRateDropDownDetails(self):
        try:
            self.click(self.totalInitialRateDropDown_xpath)
        except:
            print('''Unable to click on Total Initial Rate Drop Down.
            Please check whether required permissions are assigned.''')
            raise selenium.common.exceptions.NoSuchElementException

    def getAdjustersWithRatesfromUI(self):
        adjusters = self.getElements(self.adjustersElements_xpath)
        adjustersRates = self.getElements(self.adjustersRate_xpath)
        uiAdjusterRates = dict()
        for i in range(0,len(adjusters)):
            uiAdjusterRates[adjusters[i].text] = adjustersRates[i].text
        return uiAdjusterRates

    def getAdjustersWithRatesfromTDH(self):
        count = int(self.tdh['Pricing Information-No of Adjusters'])
        print(count)
        tdhAdjusters = dict()
        for i in range(1,count+1):
            tdhAdjusters[self.tdh['Pricing Information - Before Resubmission-Adjuster - '+str(i)+' Name']] = self.tdh['Pricing Information - Before Resubmission-Adjuster - '+str(i)+' Value']
        return tdhAdjusters

    def getAdjustersWithRatesfromTDHAfterSub(self):
        count = int(self.tdh['Pricing Information-No of Adjusters'])
        print(count)
        tdhAdjusters = dict()
        for i in range(1,count+1):
            tdhAdjusters[self.tdh['Pricing Information - After Resubmission-Adjuster - '+str(i)+' Name']] = self.tdh['Pricing Information - After Resubmission-Adjuster - '+str(i)+' Value']
        return tdhAdjusters

    def compareAdjusters(self):
        uiAdjusters = self.getAdjustersWithRatesfromUI()
        tdhAdjusters = self.getAdjustersWithRatesfromTDH()
        try:
            assert uiAdjusters == tdhAdjusters
        except:
            print("Actual Adjusters:")
            print(uiAdjusters)
            print("Expected Adjusters")
            print(tdhAdjusters)
            print("Assertion Failure.")

    def clickModifyCommitment(self):
        self.click(self.modifyCommitmentLink_xpath)
        time.sleep(3)

    def cancelSendNationalMIDecision(self):
        time.sleep(6)
        self.click(self.cancelSendNMIDecision_xpath)

    def verifyTotalInitialRateDetailsModifyCom(self):
        time.sleep(4)
        self.collapseAll()
        time.sleep(5)
        self.click(self.pricingInformationTab_xpath)
        self.scrollDownToElement(self.pricingInformationTab_xpath)
        time.sleep(2)
        if self.isDisplayed(self.totalInitialRateLabel_xpath):
            self.assertText(self.totalInitialRate_xpath, self.tdh["Pricing Information - Modify Commitment-Total Initial Rate"], 'Total Initial Rate is not as expected')
            self.clickTotalInitialRateDropDownDetails()
            uiAdjusters = self.getAdjustersWithRatesfromUI()
            tdhAdjusters = self.getAdjustersWithRatesfromTDHModifyCom()
            try:
                assert uiAdjusters == tdhAdjusters
                print("Actual Adjusters:")
                print(uiAdjusters)
                print("Expected Adjusters")
                print(tdhAdjusters)
            except:
                print("Actual Adjusters:")
                print(uiAdjusters)
                print("Expected Adjusters")
                print(tdhAdjusters)
                print("Assertion Failure.")

    def getAdjustersWithRatesfromTDHModifyCom(self):
        count = int(self.tdh['Pricing Information-No of Adjusters'])
        print(count)
        tdhAdjusters = dict()
        for i in range(1,count+1):
            tdhAdjusters[self.tdh['Pricing Information - Modify Commitment-Adjuster - '+str(i)+' Name']] = self.tdh['Pricing Information - Modify Commitment-Adjuster - '+str(i)+' Value']
        return tdhAdjusters

    def clickAdvanceWorkFlow(self):
        self.click(self.advanceWorkflowLink_xpath)
        time.sleep(4)

    def completeAdvanceWorkflow(self):
        time.sleep(10)
        self.clickAdvanceWorkFlow()
        self.click(self.advanceWorkflowAssignTo_xpath)
        self.click("//label[text()='Assign To']/following::a[text()='"+self.tdh['Advance Workflow-Assign To']+"']")
        self.sendKeys(self.advanceWorkflowComments_xpath,self.tdh['Advance Workflow-Comment'])
        self.click( self.advanceWorkFlowSubmit)

        time.sleep(5)

    def clickPostCloseReview(self):
        self.click(self.postCloseReviewTab_xpath)
        time.sleep(8)
