import pytest
from selene import browser, be, have

def test_succesfull_search_yaru():
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
   # browser.element('html').should(have.text('About this page'))
    browser.element('[id="search-result"]').should(have.text("User-oriented Web UI browser tests in Python"))


def test_succesfull_nothing_found():
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('??').press_enter()
    browser.element('[class="content__left"]').should(be.present)
    #browser.element('[id="fvzhbb8-PJgm-FE"]').should(have.text("Ничего не нашли"))
