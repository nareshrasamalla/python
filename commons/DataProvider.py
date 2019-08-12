import xlrd
from datetime import datetime
class DataProvider:

    '''This class consists of the methods to read Excel sheet from the specified location,
    select the TestCase data based on the TestType provided while initilizing this class.
    '''


    def __init__(self,workbookLocation,testType):
        self.testType = testType
        self.workbookLocation = workbookLocation


    def commonDataProvider(self):
        print("Started Reading Excel sheet at: "+datetime.now().strftime("%H:%M:%S"))
        location = (self.workbookLocation)
        wb = xlrd.open_workbook(location)
        sheet = wb.sheet_by_index(0)
        testData = list()
        for k in self.testCaseIdentifier(sheet,self.testType):
            testScenario = dict()
            for i in range(6,sheet.nrows):
                keyValue1 = str()
                keyValue1 = sheet.cell_value(i,1)
                if "\n" in keyValue1:
                    keyValue1 = keyValue1.rstrip('\n')
                    keyValue1 = keyValue1.rstrip()
                testScenario[keyValue1+"-"+sheet.cell_value(i,6)] = sheet.cell_value(i,k)
            for i in range(0,5):
                testScenario[sheet.cell_value(i, 6) ] = sheet.cell_value(i, k)
            testData.append(testScenario)
        print("Data read from Excel sheet completed at: " + datetime.now().strftime("%H:%M:%S"))
        return testData

    def testCaseIdentifier(self,sheet,testType):
        cellsWithTestType = sheet.row_slice(rowx=3, start_colx=7, end_colx=sheet.ncols)
        testColWithSelectedType = list()
        for i in range (0,cellsWithTestType.__len__()):
            temp = cellsWithTestType[i].value
            temp = temp.rstrip()
            if testType in temp:
                testColWithSelectedType.append(i+7)
            else: pass
        if len(testColWithSelectedType)==0:
            exit("execution type is not matched")
        return testColWithSelectedType


