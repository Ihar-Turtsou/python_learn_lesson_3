from selene import be, have

def test_positive_ecosia_find(browser):
    browser.open('/')
    browser.element('[data-test-id="search-form-input"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('User-oriented Web UI browser tests in Python'))

def test_negative_ecosia_find(browser):
    browser.open('/')
    browser.element('[data-test-id="search-form-input"]').should(be.blank).type('rueiretijnkdhsfdsfs').press_enter()
    browser.element('html').should(have.text('Unfortunately we didn’t find any results'))