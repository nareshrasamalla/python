from ext import Constants
from commons import UICommons

class LoginToAxis():

    def __init__(self,testDataHolder):
        self.tdh = testDataHolder

    def logintoAxis(self,username=''):
        if username == '':
            username = self.tdh['User Role']
        userName = ''
        passWord = ''
        if "Customer" == username:
            userName = Constants.externaluserID
            passWord = Constants.externalpwd


        elif "Processor" == username:
            userName = Constants.processoruserID
            passWord = Constants.processorpwd

        elif "Solution Center" == username:
            userName = Constants.solutionuserID
            passWord = Constants.solutionpwd

        elif "Underwriter" == username:
            userName = Constants.underwriteruserID
            passWord = Constants.underwriterpwd

        elif "Servicing Specialist" == username:
            userName = Constants.Servicing_SpecialistuserID
            passWord = Constants.Servicing_Specialistuserpwd

        elif "VP Servicing" == username:
            userName = Constants.VPServicingUserID
            passWord = Constants.VPServicingUserpwd

        elif "DARManager"  == username:
            userName = Constants.DAR_ManagerID
            passWord = Constants.DAR_ManagerPwd

        elif "SysAdmin" == username:
            userName = Constants.SysAdminID
            passWord = Constants.SysAdminPwd

        elif "Servicing Director" == username:
            userName = Constants.ServicingDirectorUserID
            passWord = Constants.ServicingDirectorPwd

        elif "Solution Center Manager" == username:
            userName = Constants.SolutionMgrID
            passWord = Constants.SolutionMgrpwd

        else:
            userName = Constants.underwriteruserID
            passWord = Constants.underwriterpwd

        launcher = UICommons.Commons()

        if self.tdh['User Role'] == "Customer" or self.tdh['User Role'] == "Servicer External" or self.tdh['User Role'] == "LoanCloseExternal" or self.tdh['User Role'] == "Customer Manager" or self.tdh['User Role'] == "Contract UW Ext" or self.tdh['User Role'] == "Investor":
            launcher.navigateToURL(Constants.ext_url)

        return userName,passWord





