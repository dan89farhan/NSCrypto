from django.test import TestCase
import string
import numpy as np

import random

import sys

import math
# Create your tests here.

class PlayFairTestCase(TestCase):


 


# Test vectors from "Simplified AES" (Steven Gordon)
# (http://hw.siit.net/files/001283.pdf)
print("name is ")
plaintext = 0b1101011100101000
key = 0b0100101011110101
ciphertext = 0b0010010011101100
keyExp(key)
try:
    assert encrypt(plaintext) == ciphertext
except AssertionError:
    print("Encryption error")
    print(encrypt(plaintext), ciphertext)
    sys.exit(1)
try:
    assert decrypt(ciphertext) == plaintext
except AssertionError:
    print("Decryption error")
    print(decrypt(ciphertext), plaintext)
    sys.exit(1)
print("Test ok!")
# sys.exit()