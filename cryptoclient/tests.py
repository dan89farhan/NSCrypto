from django.test import TestCase
import string
import numpy as np

import random

import sys
# Create your tests here.

class PlayFairTestCase(TestCase):

	def testRailFence(self):
		plain = "Farhan"
		print (plain)
		cipher = encrypt(plain, '1 2 3' )
		print (cipher)
		plain2 = decrypt(cipher, '1 2 3')
		print (plain2)
		
def encrypt(msg, key):
	'''
	Ciphers message using key.
		- key cannot contain repeating characters
	'''
	# ignore all the spaces
	msg = msg.replace(' ', '')
	# if there are blank boxes in matrix, fill them with random characters
	# so that it can be evenly divided by the key length
	while len(msg) % len(key) != 0:
		msg += random.choice(string.uppercase)
	# spilit the message periodically by a lenght of key and store them
	chunks = [msg[i:i+len(key)] for i in range(0, len(msg), len(key))]
	# if you don't understand, uncomment the next line for help
	print(chunks)
	# calculate the order we need to apply to it, sorted by ASCII acrrodingly
	order = [''.join(sorted(key)).find(x) for x in key]
	print (order)
	# using x to temperarally store the result row by row
	# retrive character one by one according to order
	x = map(lambda k: [c for (y,c) in sorted(zip(order, k))], chunks)
	print (x)
	# retrive the result one character by one
	result = [l[i] for i in range(len(key)) for l in x]
	result = ''.join(result)
	return result

def decrypt(msg, key):
	'''
	Deciphers message using key.
		- decrypted message may be suffixed by meaningless characters
	'''
	# calculate the order we need to apply to it, sorted by ASCII acrrodingly
	order = [key.find(x) for x in sorted(key)]
	# analyze the string so that we can reverse the result to x in encryption
	chunks = [msg[k+x*len(msg)/len(key)] for k in range( int(len(msg)/len(key)) ) for x in range(len(key))]
	print (chunks)
	# removing all the symbols
	chunks = ''.join(chunks)
	print (chunks)
	# retrive how each row was picked
	chunks = [chunks[i:i+len(key)] for i in range(0, len(chunks), len(key))]
	print (chunks)
	x = map(lambda k: ''.join([c for (y,c) in sorted(zip(order, k))]), chunks)
	return ''.join(x)