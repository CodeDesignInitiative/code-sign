import requests
import os

from django.core.exceptions import ValidationError


def captcha_validator(token):
    was_successful = requests.post("https://www.google.com/recaptcha/api/siteverify",
                                   data={"secret": os.getenv("RECAPTCHA_SECRET"),
                                         "response": token}).json()["success"]
    if not was_successful:
        raise ValidationError("The captcha validation was not successful")
