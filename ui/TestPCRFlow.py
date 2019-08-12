from commons import DataProvider, UICommons, B2BCommons
from pageObjects.AXIS import LoginPage
from pageObjects.AXIS.Origination import LandingPage,ApplicationDetailsPage,PostCloseReviewTab,VendorManagementPage,BatchUploadPage,ScheduledJobsPage
from pageObjects.AXIS.Servicing import CertificateDetailsPage,UpdateLoanClosedDatePage
from utilities import xml_utility,excel_utility
import time

dataProvider = DataProvider.DataProvider(workbookLocation="D:/Python/pythonSelenium/pythonSelenium/resources/uiTestData/DemoTC2.xlsx", testType='Demo')
data = dataProvider.commonDataProvider()
tdh = data[0]

#excelPCR = ExcelUtil.PCRExcel('D:\Python\pythonSelenium\pythonSelenium\\resources\\uiTestData\PCR\\AMC_DEL_073119_045933.xlsx',tdh)
#excelPCR.updateCellValue(tdh['PCR Excel Sheet - 1-Sheet Name - 1'])2600296369


#tdh['MI Application Number'] = B2BCommons.createMIApplication(tdh['B2B Mi-Order Submission-File Name'])

launch = UICommons.Commons()
webdriver = launch.launchApplication()
#
login = LoginPage.LoginPage(webdriver, tdh)
#login.loginAs('VP Servicing')
login.loginAs('SysAdmin')
landingPage = LandingPage.LandingPage(webdriver, tdh)
time.sleep(5)
#landingPage.clickBatchUpload()

# landingPage.searchApplication(str(tdh['MI Application Number']))
# certificateDetailsPage = CertificateDetailsPage.CertificateDetailsPage(webdriver,tdh)
# certificateDetailsPage.clickUpdateLoanClosedDate()
# loanClosedDatePage = UpdateLoanClosedDatePage.UpdateLoanClosedDate(webdriver,tdh)
# loanClosedDatePage.updateLoanCloseDate()
# loanClosedDatePage.handleAxisAlert()
# login.logOut()
# login.loginAs()
# landingPage = LandingPage.LandingPage(webdriver, tdh)
# landingPage.searchApplication(str(tdh['MI Application Number']))
# appDetailsPage = ApplicationDetailsPage.ApplicationDetailsPage(webdriver,tdh)
# appDetailsPage.completeAdvanceWorkflow()
# appDetailsPage.clickPostCloseReview()
# postCloseReviewTab = PostCloseReviewTab.PostCloseReviewTab(webdriver,tdh)
# postCloseReviewTab.verifyPCRStatus('Waiting for Credit Package')
#postCloseReviewTab.updateStatus()
#postCloseReviewTab.verifyPCRStatus('Eligible for VEndor Assigning')
# batchUpload = BatchUploadPage.BatchUploadPage(webdriver,tdh)
# batchUpload.selectVendor()
# batchUpload.uploadWorksheet()
landingPage.clickRunScheduledJobs()
runScheduledJobs = ScheduledJobsPage.ScheduledJobsPage(webdriver,tdh)
runScheduledJobs.selectScheduledJob()
runScheduledJobs.handleJobAlert()

