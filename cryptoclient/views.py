from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.views import generic

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import Nameform, ContactForm, CryptoForm, Decrypt
from .models import EncryptDecrypt

from .ceasercipher import CeaserCipher
from .playfair import *
from .hill import Hill
from .vernam import Vernam
from .railfence import RailFence
from .columnar import Columnar
from .AES import AES
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
            key = form.cleaned_data['key']  

            print("{} {} {} {} {} ".format(algo, symmetric_tech, asymmetric_tech, message, key))
            encryptdecrypt = ''
            if key and message and (symmetric_tech or asymmetric_tech) and algo:
                if algo == 'Symmetric Algo':
                    if symmetric_tech == 'ceaser cipher':
                        encryptValue = CeaserCipher.ceaserCipherEncrypt(message, int(key))
                        
                    elif symmetric_tech == 'play fair':
                        encryptValue = playfairEncrypt(message.upper(), key.upper())
                        encryptValue = ''.join(encryptValue)
                    elif symmetric_tech == 'hill cipher':
                        hill = Hill()
                        encryptValue = hill.encrypt(message, key)
                        # print("Key is ", key.split())
                    elif symmetric_tech == 'vernam cipher':
                        vernam = Vernam()
                        encryptValue = vernam.encryptMessage(key.upper(), message.upper())
                    elif symmetric_tech == 'rail fence':
                        railfence = RailFence()
                        encryptValue = railfence.encryptFence(message, int(key) )

                    elif symmetric_tech == 'columnar':
                        columnar = Columnar()
                        encryptValue = columnar.EncryptMessage(key, message)
                    elif symmetric_tech == 'aes':
                        aes = AES()

                        #  message=bin(int(message,base=2))
                        print("Message is ", message)
                        encryptValue = aes.encrypt(bin(int(message,base=2)))
                    encryptdecrypt = saveToDB(algo, symmetric_tech, asymmetric_tech, encryptValue, key)
                    return HttpResponseRedirect(reverse('cryptoclient:thanks', args=(encryptdecrypt.id, )))
                    
                    
                        
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
            message = CeaserCipher.ceaserCipherDecrypt(message, int(key))
        elif symmetric_tech == 'play fair':
            message = playFairDecrypt(message, key)
        elif symmetric_tech == 'hill cipher':
            hill = Hill()
            # print("key is ", key)
            message = hill.decrypt(message, key)
        elif symmetric_tech == 'vernam cipher':
            vernam = Vernam()
            message = vernam.decryptMessage(key.upper(), message.upper())
        elif symmetric_tech == 'rail fence':
            railfence = RailFence()
            message = railfence.decryptFence(message, int(key))
        
        elif symmetric_tech == 'columnar':
            columnar = Columnar()
            message = columnar.DecryptMessage(key, message)
    encryptdecrypt.message = message
    print("message is ", message)
    # encryptdecrypt.save()
    return render(request, 'cryptoclient/decrypt.html', {'message': message, 'key': key})


class EncryptedView(generic.DetailView):
    model = EncryptDecrypt
    template_name = 'cryptoclient/encrypt.html'





def saveToDB(algo, symmetric_tech, asymmetric_tech, encryptValue, key):
    encryptdecrypt = EncryptDecrypt.objects.get(pk=1)
    encryptdecrypt.symmetric_asymmetric = algo
    encryptdecrypt.symmetric_tech = symmetric_tech
    encryptdecrypt.asymmetric_tech = asymmetric_tech
    encryptdecrypt.message = encryptValue
    encryptdecrypt.key = key
    encryptdecrypt.save()
    return encryptdecrypt


# PlayFair Encrypt and Decrypt Functions



