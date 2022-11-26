import time

from selene.support.shared import browser
from selene import be, have

EXPECTED_RESULT_TITLE = 'Thanks for submitting the form'

browser.open('https://demoqa.com/automation-practice-form')
browser.element('[id="firstName"]').should(be.blank).type('Olena')
browser.element('[id="lastName"]').should(be.blank).type('Kuznietsova')
browser.element('[id="userEmail"]').should(be.blank).type('it.kuznietsova@gmail.ua')
browser.element('label[for="gender-radio-2"]').should(be.enabled).click()
browser.element('[id="userNumber"]').should(be.blank).type('8950123456')
browser.element('[id="subjectsContainer"]').should(be.enabled).click()
browser.element('[id=dateOfBirthInput]').type('30 Nov 2000').press_enter()
browser.element('[id=subjectsInput]').should(be.blank).type('comp').press_enter()
browser.element('label[for="hobbies-checkbox-1"]').should(be.enabled).click()
browser.element('[id=currentAddress]').should(be.blank).type('79 Park Avenue')
browser.element('[id=react-select-3-input]').should(be.blank).type('nc').press_enter()
browser.element('[id=react-select-4-input]').should(be.blank).type('de').press_enter
browser.element('[id=uploadPicture]').should(be.clickable)
browser.element('[id=submit]').should(be.clickable).click()

assert browser.element('[class="modal-title h4"]').should(have.text(EXPECTED_RESULT_TITLE))


