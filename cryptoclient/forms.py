from django import forms


class Nameform(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


SYMMETRIC_ASYMMETRIC = [
    ('symmetric', 'Symmetric Algo'),
    ('asymmetric', 'ASymmetric Algo'),
]

SYMMETRIC_TECH = [
    ('ceaser cipher', 'Ceaser Ciper')
]

ASYMMETRIC_TECH = [
    ('des', 'des 8 bit  ')
]


class CryptoForm(forms.Form):
    symmetric_asymmetric = forms.ChoiceField(
        choices=SYMMETRIC_ASYMMETRIC,
        widget = forms.RadioSelect,
        required = False
    )
    symmetric_tech = forms.ChoiceField(
        choices=SYMMETRIC_TECH,
        widget = forms.RadioSelect,
        required=False
    )
    asymmetric_tech = forms.ChoiceField(
        choices = ASYMMETRIC_TECH,
        widget = forms.RadioSelect,
        required=False
    )
    message = forms.CharField(label="Your Name", max_length=100, required=False)
    key = forms.CharField( widget=forms.TextInput(attrs={'type':'number'}), required=False)

class Decrypt(forms.Form):
    abc = ''

