from django import forms

from sign.models import Signature
from sign.validators import captcha_validator


class SignatureForm(forms.ModelForm):
    captcha_token = forms.CharField(validators=[captcha_validator])

    class Meta:
        model = Signature
        exclude = ()
