import pytest
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_button(self, browser):
        browser.get(link)
        #time.sleep(5)
        #в зависимости от параметра language при запуске меняется язык кнопок, запуск - pytest --language=es test_items.py
        browser.find_element_by_css_selector(".btn-primary")
