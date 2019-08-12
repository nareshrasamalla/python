from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebPage(ABC):

    def __init__(self,driver):
        self.driver = driver

    @abstractmethod
    def checkPage(self):
        pass

    def scrollDownToElement(self,xpath):
        self.driver.execute_script("return arguments[0].scrollIntoView();", self.getElement(xpath))
        self.driver.execute_script("scrollBy(0,-200);")
        print("Scroll down to a element.")
        self.driver.implicitly_wait(30)

    def scrollUpToElement(self, xpath):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.getElement(xpath))
        self.driver.execute_script("scrollBy(0,200);")
        print("Scroll up to a element.")
        self.driver.implicitly_wait(30)


    def sendKeys(self,xpath,keys):
        self.getElement(xpath).clear()
        self.getElement(xpath).send_keys(keys)
        self.driver.implicitly_wait(30)

    def click(self, xpath):
        self.getElement(xpath).click()
        self.driver.implicitly_wait(30)
        print('Click Action Completed.')

    def getElement(self,xpath):
        element = self.driver.find_element(By.XPATH,xpath)
        return element

    def scrollDownToElementAndClick(self,xpath):
        self.scrollDownToElement(xpath)
        self.click(xpath)

    def scrollUpToElementAndClick(self, xpath):
        self.scrollUpToElement(xpath)
        self.click(xpath)

    def scrollBy(self,x,y):
        self.driver.execute_script("window.scrollTo("+str(x)+","+str(y)+")")

    def scrollToBottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def clickUsingJS(self,xpath):
        pass

    def isDisplayed(self,xpath):
        return self.driver.find_element(By.XPATH,xpath).is_displayed()

    def getText(self,xpath):
        return self.getElement(xpath).text

    def assertText(self,xpath,expectedText,errMsg=''):
        try:
            actualText = self.getText(xpath)
            assert actualText == expectedText
        except AssertionError:
            if errMsg != '':
                print(errMsg)
                print("Expected Text: " + expectedText + " \n Actual Text: " + actualText + "\n Assertion Failed.")
            else: print("Expected Text: "+expectedText +" \n Actual Text: "+actualText+"\n Assertion Failed.")

    def getElements(self,xpath):
        return self.driver.find_elements(By.XPATH,xpath)


    def waitTillPresenceAndClick(self,xpath):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()