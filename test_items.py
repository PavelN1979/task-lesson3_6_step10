from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
def test_guest_should_see_button(browser):
    browser.get(link)
    time.sleep(30)
    my_element = browser.find_element(By.CSS_SELECTOR, "form > .btn.btn-lg.btn-primary.btn-add-to-basket")
    assert my_element != None, "The product page on the website does not contain an add to cart button!"
