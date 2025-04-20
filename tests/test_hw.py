from model.data.users import user
from model.pages.registration_page import RegistrationPage


def test_submit_registration_page():
    practice_form = RegistrationPage()
    practice_form.open()
    practice_form.register(user)
    practice_form.should_have_registered_user(user)