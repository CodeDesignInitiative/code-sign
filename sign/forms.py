from django import forms

from sign.models import Signature


class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        exclude = ()
