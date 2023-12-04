from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given('open target main page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')


@when('click on target circle icon')
def click_on_target_circle_icon(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/circle') and contains(@id, 'utilityNav-circle')]").click()
    sleep(6)  # wait for ads to disappear


@then('verify there are 5 benefit boxes')
def verify_there_are_5_benefit_boxes(context):
     context.driver.find_element(By.CSS_SELECTOR, "li[class*='styles__BenefitCard']").text
