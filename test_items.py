from selenium.common.exceptions import NoSuchElementException
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def is_text_present(browser, text):
    try:
        browser.find_element_by_css_selector(text)
    except NoSuchElementException:
        return False
    return True

class TestProductPage:

    def test_button_add_to_basket_is_visible(self, browser):
        browser.get(link)
        time.sleep(30)
        exists = is_text_present(browser, "button.btn-add-to-basket")
        assert exists == True, "No add to basket button"