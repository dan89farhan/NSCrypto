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
            key = form.cleaned_data['key']  

            print("{} {} {} {} {} ".format(algo, symmetric_tech, asymmetric_tech, message, key))
            encryptdecrypt = ''
            if key and message and (symmetric_tech or asymmetric_tech) and algo:
                if algo == 'Symmetric Algo':
                    if symmetric_tech == 'ceaser cipher':
                        encryptValue = ceaserCipherEncrypt(message, key)
                        
                    elif symmetric_tech == 'play fair':
                        encryptValue = playfairEncrypt(message.upper(), key.upper())
                        encryptValue = ''.join(encryptValue)
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
            message = ceaserCipherDecrypt(message, key)
        elif symmetric_tech == 'play fair':
            message = decryptPlayFair(message, key) 
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
    print (message_to_digraphs(message))
    print (matrix(key) )
    encMessage = encryptPlayFair(key, message)
    print(encMessage)
    return encMessage

def playfairDecrypt(message, key):
    return decryptPlayFair(message, key)
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



def matrix(key):
	matrix=[]
	for e in key.upper():
		if e not in matrix:
			matrix.append(e)
	alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
	
	for e in alphabet:
		if e not in matrix:
			matrix.append(e)	
	
	#initialize a new list. Is there any elegant way to do that?
	matrix_group=[]
	for e in range(5):
		matrix_group.append('')

	#Break it into 5*5
	matrix_group[0]=matrix[0:5]
	matrix_group[1]=matrix[5:10]
	matrix_group[2]=matrix[10:15]
	matrix_group[3]=matrix[15:20]
	matrix_group[4]=matrix[20:25]
	return matrix_group

def message_to_digraphs(message_original):
	#Change it to Array. Because I want used insert() method
	message=[]
	for e in message_original:
		message.append(e)

	#Delet space
	for unused in range(int(len(message))):
		if " " in message:
			message.remove(" ")

	#If both letters are the same, add an "X" after the first letter.
	i=0
	for e in range(int(len(message)/2)):
		if message[i]==message[i+1]:
			message.insert(i+1,'X')
		i=i+2

	#If it is odd digit, add an "X" at the end
	if int(len(message))%2==1:
		message.append("X")
	#Grouping
	i=0
	new=[]
	for x in range(1,int(len(message)/2)+1):
		new.append(message[i:i+2])
		i=i+2
	return new

def find_position(key_matrix,letter):
	x=y=0
	
	for i in range(5):
		for j in range(5):
			
			if key_matrix[i][j]==letter:
				print("i = {} j = {} letter = {}".format(i , j, letter))
				x=i
				y=j

	return x,y

def encryptPlayFair(key, message):
	message=message_to_digraphs(message)
	key_matrix=matrix(key)
	cipher=[]
	
	for e in message:
		
		
		
		p1,q1=find_position(key_matrix,e[0])
		p2,q2=find_position(key_matrix,e[1])
		print("p1 = {} q1 = {} ".format(p1,q1))
		print("p2 = {} q2 = {} ".format(p2,q2))
		if p1==p2:
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			cipher.append(key_matrix[p1][q1+1])
			cipher.append(key_matrix[p1][q2+1])		
		elif q1==q2:
			if p1==4:
				p1=-1
			if p2==4:
				p2=-1
			cipher.append(key_matrix[p1+1][q1])
			cipher.append(key_matrix[p2+1][q2])
		else:
			cipher.append(key_matrix[p1][q2])
			cipher.append(key_matrix[p2][q1])
	return cipher

def cipher_to_digraphs(cipher):
	i=0
	new=[]
	for x in range(int(len(cipher)/2)):
		new.append(cipher[i:i+2])
		i=i+2
	return new


def decryptPlayFair(cipher, key):	
	cipher=cipher_to_digraphs(cipher)
	key_matrix=matrix(key)
	plaintext=[]
	for e in cipher:
		p1,q1=find_position(key_matrix,e[0])
		p2,q2=find_position(key_matrix,e[1])
		if p1==p2:
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			plaintext.append(key_matrix[p1][q1-1])
			plaintext.append(key_matrix[p1][q2-1])		
		elif q1==q2:
			if p1==4:
				p1=-1
			if p2==4:
				p2=-1
			plaintext.append(key_matrix[p1-1][q1])
			plaintext.append(key_matrix[p2-1][q2])
		else:
			plaintext.append(key_matrix[p1][q2])
			plaintext.append(key_matrix[p2][q1])

	for unused in range(len(plaintext)):
		if "X" in plaintext:
			plaintext.remove("X")
	
	output=""
	for e in plaintext:
		output+=e
	return output.lower()
