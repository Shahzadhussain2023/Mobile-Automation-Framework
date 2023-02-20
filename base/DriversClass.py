from appium import webdriver


class Driver:

    def getDriverMethod(self):
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                  desired_capabilities=
                                  {
                                      "platformName": "Android",
                                      "platformVersion": "11",
                                      # "platformVersion": "12L",
                                      "deviceName": "android",
                                      "automationName": "uiautomator2",
                                      #"appPackage": "com.theentertainerme.stcentertainer",
                                      "appPackage": "com.theentertainerme.sgdaentertainer",
                                      #"appActivity": "com.theentertainerme.stcentertainer.ActivityLanding",
                                      "appActivity": "com.theentertainerme.sgdaentertainer.ActivityLanding",
                                      "noReset": True
                                  })
        return driver

    def teardown(self, driver):
        driver.quit()
        return driver
