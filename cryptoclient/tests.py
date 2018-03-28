from django.test import TestCase
import string
import numpy as np

import random

import sys

import math
# Create your tests here.

class PlayFairTestCase(TestCase):

	def testRailFence(self):
		key = "HACK"
		message = "GeeksforGeeks"



		print("Key: " + key)
		print("Message: " + message)

		# First we encrypt the message
		encryptedMsg = EncryptMessage( key, message )

		print( "" )
		print( "-= Encryped Message =- " )
		print( encryptedMsg )

		print( "" )
		print( "-= Decryped Message =- " )
		decryptedMsg = DecryptMessage( key, encryptedMsg )
		print( ''.join(decryptedMsg) )
		

 
def EncryptMessage( aKey, aMessage ):
    concatStr = aKey + aMessage
    msgLength = aMessage.__len__()
    keyLength = aKey.__len__()
    matrixrows = math.ceil(msgLength / keyLength) + 1

    # The concat string has to be equal rows so we need to add filler #
    for x in range((keyLength - (msgLength % keyLength))):
        concatStr += random.choice(string.ascii_letters).lower()
		# print(concatStr)

	
    # Make the matrix to hold our values
    Matrix = [[ concatStr[x + (y * keyLength)] for x in range(keyLength)] for y in range(matrixrows)]

    # Get our cyphers
    cyphers = []

    # The cyper is made of a row of letters and we build it here
    for cols in range(keyLength):
         cyp = ""
         for rows in range( matrixrows ):
             cyp += Matrix[rows][cols]

         # We want to ignore the first key value
         cyphers.append( cyp )

    # Now we sort the cypers using socket
    cyphers.sort()

    # Remove the socket letters
    for x in range(keyLength):
        cyphers[x] = cyphers[x][1:]

    return " ".join(cyphers)


def DecryptMessage( aKey, encrypt):
    encryptLength = encrypt.__len__()
    keyLength = aKey.__len__()
    matrixrows = math.ceil( encryptLength/ keyLength)


    sortedKey = list(aKey)
    sortedKey.sort()


    msgList = encrypt.split()

    #Add the key to the start of the list
    for x in range(keyLength):
        msgList[x] = sortedKey[x] + msgList[x]

    #Now we have to find the original place
    isSorted = False
    concatStr = []

    while not isSorted:
        isSorted = True
        for x in range(keyLength):
            for y in range(keyLength):
                if msgList[x][0] == aKey[y] and x != y and msgList[x][0] != msgList[y][0]:
                    msgList[x], msgList[y] = msgList[y], msgList[x]
                    isSorted = False
                    break

    msgList = ''.join(msgList)



    for x in range(keyLength):
        for y in range(matrixrows):
            concatStr.append( msgList[(x * matrixrows) + y] )



    Matrix = [[ concatStr[(x * matrixrows)+ y] for x in range(keyLength)] for y in range(matrixrows)]

    return ''.join(str(Matrix))