from selene import browser, have
import os


def test_register_student():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Nailia')
    browser.element('#lastName').type('Ales')

    browser.element('#userEmail').type('email@example.com')
    browser.all('[for^=gender-radio]').element_by(have.text('Female')).click()

    browser.element('#userNumber').type('1234567890')

    browser.element("#dateOfBirth").click()

    browser.element('.react-datepicker').element('[class$="month-select"]').click()
    browser.element('.react-datepicker').element('[class$="month-select"]').all(
        'option'
    ).element_by(have.text('February')).click()
    browser.element('.react-datepicker').element('[class$="year-select"]').click()
    browser.element('.react-datepicker').element('[class$="year-select"]').all('option').element_by(
        have.text('1999')
    ).click()
    browser.element('.react-datepicker').element('[class*="day--014"]').click()

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.element('[for=hobbies-checkbox-1]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('screen.png'))

    browser.element('#currentAddress').type('Rostov, Lenina 1')

    browser.element("#state").click()
    browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('NCR')).click()

    browser.element("#city").click()
    browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Gurgaon')).click()

    browser.element('#submit').click()
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))

    browser.element('.modal-content table').all('td:nth-child(2)').should(
        have.exact_texts(
            'Nailia Ales',
            'email@example.com',
            'Female',
            '1234567890',
            '14 February,1999',
            'Maths',
            'Sports',
            'screen.png',
            'Rostov, Lenina 1',
            'NCR Gurgaon',
        )
    )
