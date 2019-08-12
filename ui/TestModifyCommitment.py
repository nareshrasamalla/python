from commons import DataProvider, UICommons, B2BCommons
from pageObjects.AXIS import LoginPage
from pageObjects.AXIS.Origination import LandingPage,ApplicationDetailsPage,ModifyCommitment
from utilities import xml_utility
import time

dataProvider = DataProvider.DataProvider(workbookLocation="D:/Python/pythonSelenium/pythonSelenium/resources/uiTestData/DemoTC1.xlsx", testType='Demo')
data = dataProvider.commonDataProvider()
tdh = data[0]

tdh['Rate Quote ID'] = B2BCommons.generateRateQuote(tdh.get("B2B Rate Quote-File Name"))

updatedMi_Order_Sub_Doc = xml_utility.updateElementValue(tdh.get("B2B Mi-Order Submission-File Name"), tdh.get("B2B Mi-Order Submission-Rate Quote Xpath"), tdh['Rate Quote ID'])
tdh['MI Application Number'] = B2BCommons.createMIApplication(updatedMi_Order_Sub_Doc)

launch = UICommons.Commons()
webdriver = launch.launchApplication()

login = LoginPage.LoginPage(webdriver, tdh)
login.loginAs()
landingPage = LandingPage.LandingPage(webdriver, tdh)
landingPage.searchApplication(str(tdh['MI Application Number']))
applicationDetailsPage = ApplicationDetailsPage.ApplicationDetailsPage(webdriver,tdh)
applicationDetailsPage.verifyTotalInitialRateDetails()
#login.logOut()


updatedMi_Order_ReSub_Doc = xml_utility.updateElementValue(tdh.get("B2B Mi-Order ReSubmission-File Name"), tdh.get("B2B Mi-Order ReSubmission-Coverage Xpath"), str(tdh['B2B Mi-Order ReSubmission-Coverage']))
updatedMi_Order_ReSub_Doc = xml_utility.updateElementValue(updatedMi_Order_ReSub_Doc, tdh.get("B2B Mi-Order ReSubmission-MI Application No Xpath"), str(tdh['MI Application Number']))
tdh['MI Application Number'] = B2BCommons.createMIApplication(updatedMi_Order_ReSub_Doc)

#login.loginAs()
landingPage.searchApplication(str(tdh['MI Application Number']))
applicationDetailsPage.verifyTotalInitialRateDetailsAfterSub()

login.logOut()
login.loginAs('Solution Center')
landingPage.searchApplication(str(tdh['MI Application Number']))
time.sleep(15)
applicationDetailsPage.clickModifyCommitment()
modifyCommitment = ModifyCommitment.ModifyCommitment(webdriver,tdh)
modifyCommitment.modifyCoverage()
time.sleep(5)
applicationDetailsPage.cancelSendNationalMIDecision()
login.logOut()
login.loginAs()
landingPage.searchApplication(str(tdh['MI Application Number']))
applicationDetailsPage.verifyTotalInitialRateDetailsModifyCom()
login.logOut()