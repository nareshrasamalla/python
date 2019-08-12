from selenium import webdriver
from ext import Constants
import os

class Commons():


    def launchApplication(self,application='AXIS',browser='Chrome'):
        global webDriver
        webDriver = webdriver.Chrome(executable_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\ext\chromedriver')
        print('Browser Launched Successfully.')
        webDriver.implicitly_wait(30)
        webDriver.maximize_window()
        if application == 'AXIS':
            webDriver.get(Constants.url)
        elif application == 'AXIS-E':
            webDriver.get(Constants.ext_url)
        elif application == 'LightWell':
            webDriver.get(Constants.SterlingURL)
        print('Navigated to Base URL')
        return webDriver

    def quitApplication(self):
        webDriver.quit()
        print('Closed the browser session.')


    def navigateToURL(self,URL):
        webDriver.get(URL)


    def getDriver(self):
        return webDriver