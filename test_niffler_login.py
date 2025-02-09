from selene import browser, have

def test_succesfull_login():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('Nikita Goncharov')
    browser.element('input[name="password"]').type('BS$7\[}+F–q')
    browser.element('button[type="submit"]').click()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.quit()

