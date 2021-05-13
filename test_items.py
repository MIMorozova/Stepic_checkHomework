import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_on_the_page(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary")
    assert button is not None, "this button is not found"
    
    
    
    #pytest --language=es test_items.py
