from selenium.webdriver.common.by import By
from commons.WebPage import WebPage
import selenium.common.exceptions,time

class ScheduledJobsPage(WebPage):

    def __init__(self,driver,testDataHolder):
        super(ScheduledJobsPage, self).__init__(driver)
        self.tdh = testDataHolder
        self.driver = driver
        self.scheduledJobsHeading_xpath = "//section[@id='axis-o-mainUserAdminSection']/h2"
        self.scheduledJobsDropDown_xpath = "//select[@id='axis-o-jobTypes']/following::a[1]"
        self.runScheduledJobBtn_xpath = "//span[@id='axis-o-runJob']/a"
        self.checkPage()

    def checkPage(self):
        if self.isDisplayed(self.scheduledJobsHeading_xpath):
            pass
        else:
            print("ScheduledJobs page is not loaded or navigated to another page.")
            raise selenium.common.exceptions.ElementNotVisibleException


    def selectScheduledJob(self):
        self.click(self.scheduledJobsDropDown_xpath)
        time.sleep(2)
        self.click("//a[text()='"+self.tdh['Scheduled Job-Job Name']+"']")
        self.click(self.runScheduledJobBtn_xpath)

    def handleJobAlert(self):
        time.sleep(5)
        if self.isDisplayed("//div[text()='"+self.tdh['Scheduled Job-Alert Message']+"']"):
            self.click("//div[text()='"+self.tdh['Scheduled Job-Alert Message']+"']/following::button")
        else:
            print("Job Alert Msg validation failed or job did not run successfully.")
            assert False