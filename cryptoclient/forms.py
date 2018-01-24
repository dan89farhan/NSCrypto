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


class CryptoForm(forms.Form):
    symmetric_asymmetric = forms.ChoiceField(
        choices=SYMMETRIC_ASYMMETRIC,
        widget = forms.RadioSelect,
    )
    symmetric_tech = forms.ChoiceField(
        choices=SYMMETRIC_TECH,
        widget = forms.RadioSelect,
    )

