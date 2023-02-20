import utilities.CustomLogger as cl
from base.DriversClass import Driver
from base.basePage import locatorBasePage


class login:
    driver1 = Driver()
    log = cl.customLogger()

    driver = driver1.getDriverMethod()

    log.info("Launch app")

    baseObject = locatorBasePage(driver)

    # Enter Phone number in a phone field.
    baseObject.sendText("testqash0+testq@gmail.com", "com.theentertainerme.sgdaentertainer:id/et_email", "id")
    # Enter password in a field
    baseObject.sendText("Test123@", "com.theentertainerme.sgdaentertainer:id/et_password", "id")
    # click on privacy policy CTA
    baseObject.clickElement("com.theentertainerme.sgdaentertainer:id/checkbox_privacy_policy", "id")
    # click on EUAL CTA
    baseObject.clickElement("com.theentertainerme.sgdaentertainer:id/checkbox_new_user", "id")
    # click on login button
    baseObject.clickElement("com.theentertainerme.sgdaentertainer:id/btnContinue", "id")
    # Click on profile tab
    baseObject.clickElement("Profile", "text")
    # click on profile detai
    baseObject.clickElement("Profile Details", "text")

    baseObject.clickElement("com.theentertainerme.sgdaentertainer:id/iv_back", "id")
    # email_ele = baseObject.getElement("testqash0+testq@gmail.com", "text")
    # print(email_ele)
    # assert email_ele == "testqash0+testq@gmail.com"
    driver = driver1.teardown(driver)





