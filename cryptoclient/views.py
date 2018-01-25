from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail

from .forms import Nameform, ContactForm, CryptoForm, Decrypt
# Create your views here.


def index(request):
    """defualt index request"""
    return render(request, "cryptoclient/index.html")


def thankspage(request):
    return render(request, 'cryptoclient/thanks.html')


def get_name(request):
    if request.method == "POST":
        form = Nameform(request.POST)

        if form.is_valid():

            return redirect('/cryptoclient/yourname')
    else:
        form = Nameform()
    return render(request, 'cryptoclient/yourname.html', {'form': form})


def contactform(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['dan89farhan@yahoo.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
            return redirect('thanks')
    else:
        form = ContactForm()
    return render(request, 'cryptoclient/contactform.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'cryptoclient/index.html', {'form': form})
    return render(request, "cryptoclient/index.html")


def crypto(request):
    # return render(request, 'cryptoclient/yourname.html')
    if request.method == 'POST':

        form = CryptoForm(request.POST)
        print("Hello %s", form.errors)
        if form.is_valid():

            algo = request.POST.get('choice')
            symmetric_tech = form.cleaned_data['symmetric_tech']
            asymmetric_tech = form.cleaned_data['asymmetric_tech']
            message = form.cleaned_data['message']
            key = int(form.cleaned_data['key'])
            data = form.cleaned_data
            encrypt = ''
            message = bytes(message, 'utf-8')
            for chars in enumerate(message):

                encrypt += chr(chars[1] + key)
                # print(bytes([chars[1] + 3]))

            print('Encrypted message is %s ', encrypt)

            if key and message and (symmetric_tech or asymmetric_tech) and algo:
                print(data)
                return render(request, 'cryptoclient/thanks.html', {'encrypt': encrypt, 'key': key})
            else:
                form = CryptoForm()
                return render(request, 'cryptoclient/cryptons.html', {'form': form})

        else:
            print("in else parts")
            form = CryptoForm()
            return render(request, 'cryptoclient/cryptons.html', {'form': form})
    else:
        form = CryptoForm()
        return render(request, 'cryptoclient/cryptons.html', {'form': form})

    # return render(request, 'cryptoclient/cryptons.html', {'form': form})


def decrypt(request):

    message = request.POST.get('ct')
    key = int(request.POST.get('key'))
    decrypt = ''
    message = bytes(message, 'utf-8')
    for chars in enumerate(message):

        decrypt += chr(chars[1] - key)
        # print(bytes([chars[1] + 3]))

    print('Decrypted message is %s ', decrypt)
    return render(request, 'cryptoclient/decrypt.html', {'message': decrypt, 'key': key})
