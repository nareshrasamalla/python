from commons import DataProvider, UICommons, B2BCommons

from pageObjects.AXIS import LoginPage
from pageObjects.AXIS.Origination import LandingPage,ApplicationDetailsPage,PostCloseReviewTab,VendorManagementPage,BatchUploadPage,ScheduledJobsPage
from pageObjects.AXIS.Servicing import CertificateDetailsPage,UpdateLoanClosedDatePage,FileNoticeOfDefaultPage,FileInitialClaimPage,ReviewInitialClaim


from utilities import xml_utility,excel_utility
import time


dataProvider = DataProvider.DataProvider(workbookLocation="D:\\PythonBDD\\pythonSelenium\\resources\\uiTestData\\DemoTC3.xlsx", testType='Demo')
data = dataProvider.commonDataProvider()
tdh = data[0]

tdh['MI Application Number'] = B2BCommons.createMIApplication(tdh['B2B Mi-Order Submission-File Name'])


launch = UICommons.Commons()
webdriver = launch.launchApplication()
#
login = LoginPage.LoginPage(webdriver, tdh)
login.loginAs()
landingPage = LandingPage.LandingPage(webdriver, tdh)
time.sleep(5)
landingPage.searchApplication(str(tdh['MI Application Number']))
certificateDetailsPage = CertificateDetailsPage.CertificateDetailsPage(webdriver,tdh)
certificateDetailsPage.clickUpdateLoanClosedDate()
loanClosedDatePage = UpdateLoanClosedDatePage.UpdateLoanClosedDate(webdriver,tdh)
loanClosedDatePage.updateLoanCloseDate()
loanClosedDatePage.handleAxisAlert()
certificateDetailsPage.clickFileNoticeOfDefault()
fileNOD = FileNoticeOfDefaultPage.FileNoticeOfDefaultPage(webdriver,tdh)
fileNOD.fileNOD()
print(certificateDetailsPage.getLoanStatus())
certificateDetailsPage.clickFileInitialClaim()
fileInitialClaimPage = FileInitialClaimPage.FileInitialClaimPage(webdriver,tdh)
fileInitialClaimPage.fileInitialClaim()
certificateDetailsPage.clickReviewInitialClaim()
reviewInitialClaim = ReviewInitialClaim.ReviewInitialClaim(webdriver,tdh)
reviewInitialClaim.reviewInititalClaim()
reviewInitialClaim.recommendClaim()

