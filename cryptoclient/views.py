from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.views import generic

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import Nameform, ContactForm, CryptoForm, Decrypt
from .models import EncryptDecrypt

import string
# Create your views here.


def index(request):
    """defualt index request"""
    return render(request, "cryptoclient/index.html")


class ThanksView(generic.DeleteView):
    model = EncryptDecrypt
    template_name = 'cryptoclient/thanks.html'
    # return render(request, 'cryptoclient/thanks.html')


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


def encrypt(request):
    if request.method == 'POST':
        form = CryptoForm(request.POST)
        print("Error in form {} ".format(form.errors) )
        if form.is_valid():
            algo = request.POST.get('choice')
            symmetric_tech = form.cleaned_data['symmetric_tech']
            asymmetric_tech = form.cleaned_data['asymmetric_tech']
            message = form.cleaned_data['message']
            key = int(form.cleaned_data['key'])

            print("{} {} {} {} {} ".format(algo, symmetric_tech, asymmetric_tech, message, key))
            encryptdecrypt = ''
            if key and message and (symmetric_tech or asymmetric_tech) and algo:
                if algo == 'Symmetric Algo':
                    if symmetric_tech == 'ceaser cipher':
                        encryptValue = ceaserCipherEncrypt(message, key)
                        encryptdecrypt = saveToDB(algo, symmetric_tech, asymmetric_tech, encryptValue, key)
                        return HttpResponseRedirect(reverse('cryptoclient:thanks', args=(encryptdecrypt.id, )))
                    elif symmetric_tech == 'play fair':
                        print("in algo and symmetric_tech ")
                        encryptValue = playfairEncrypt(message, key)
                    
                    
                        
    else:
        form = CryptoForm()
    return render(request, 'cryptoclient/encrypt.html', {'form': form})


def decrypt(request):
    encryptdecrypt = EncryptDecrypt.objects.get(pk=1)
    algo = encryptdecrypt.symmetric_asymmetric
    symmetric_tech = encryptdecrypt.symmetric_tech
    asymmetric_tech = encryptdecrypt.asymmetric_tech
    message = encryptdecrypt.message
    key = encryptdecrypt.key
    if algo == 'Symmetric Algo':
        if symmetric_tech == 'ceaser cipher':
            message = ceaserCipherDecrypt(message, key)
    encryptdecrypt.message = message
    encryptdecrypt.save()
    return render(request, 'cryptoclient/decrypt.html', {'message': message, 'key': key})


class EncryptedView(generic.DetailView):
    model = EncryptDecrypt
    template_name = 'cryptoclient/encrypt.html'


def ceaserCipherEncrypt(message, key):
    encryptValue = ''
    message = bytes(message, 'utf-8')
    for chars in enumerate(message):

        encryptValue += chr(chars[1] + key)
        # print(bytes([chars[1] + 3]))

    print('Encrypted message is %s ', encryptValue)
    return encryptValue

def ceaserCipherDecrypt(message, key):
    
    
    decrypt_message = ''
    message = bytes(message, 'utf-8')
    for chars in enumerate(message):

        decrypt_message += chr(chars[1] - key)
        # print(bytes([chars[1] + 3]))

    print('Decrypted message is %s ', decrypt_message)
    return decrypt_message

def playfairEncrypt(message, key):
    decrypt_message = ''
    print("in playfairEncrypt method {} ".format(decrypt_message))
    matrix = [ [ [] for i in range(5)] for j in range(5)]
    lowerCase = string.ascii_lowercase
    count = 0
    for i in range(5):
        for j in range(5):
            if lowerCase[count] == 'i':
                count += 1
            matrix[i][j] = lowerCase[count]
            count += 1
    
    
    return decrypt_message

def saveToDB(algo, symmetric_tech, asymmetric_tech, encryptValue, key):
    encryptdecrypt = EncryptDecrypt.objects.get(pk=1)
    encryptdecrypt.symmetric_asymmetric = algo
    encryptdecrypt.symmetric_tech = symmetric_tech
    encryptdecrypt.asymmetric_tech = asymmetric_tech
    encryptdecrypt.message = encryptValue
    encryptdecrypt.key = key
    encryptdecrypt.save()
    return encryptdecrypt