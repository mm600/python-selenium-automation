from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"[href*='https://assets.targetimg1.com/icons/assets/glyph/Cart.svg#Cart']").click()
    sleep(6)  # wait for ads to disappear

@then("Verify “{actual_text}” message is shown")
def your_cart_is_empty(context, actual_text):

    expected_text = context.driver.find_element(By.CSS_SELECTOR,".styles__StyledHeading-sc-1xmf98v-0.lfA-Dem").text
    assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'
