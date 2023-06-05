import time 
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestItem:
    def test_add_item_to_cart(self,browser):
        browser.get(link)
        add_item_to_cart_button = browser.find_element(By.XPATH, "//form[@id='add_to_basket_form']/button")
        assert add_item_to_cart_button.is_displayed, 'Element does not exist on webpage'