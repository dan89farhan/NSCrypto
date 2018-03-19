from django.test import TestCase
import string
import numpy as np
# Create your tests here.
class PlayFairTestCase(TestCase):
	def test_hill_cipher(self):
		message = encrypt('farhan')
		print( message )
		message = decrypt(message)
		print( message )

global debug
debug = 0

def modMatInv(A, p):  # Finds the inverse of matrix A mod p
	n = len(A)
	A = np.matrix(A)
	adj = np.zeros(shape=(n, n))
	for i in range(0, n):
		for j in range(0, n):
			adj[i][j] = ((-1) ** (i + j) * int(round(np.linalg.det(minor(A, j, i))))) % p
	return (modInv(int(round(np.linalg.det(A))), p) * adj) % p

def modInv( a, p):  # Finds the inverse of a mod p, if it exists
	for i in range(1, p):
		if (i * a) % p == 1: return i
	raise ValueError(str(a) + " has no inverse mod " + str(p))

def minor( A, i, j):  # Return matrix A with the ith row and jth column deleted
	A = np.array(A)
	minor = np.zeros(shape=(len(A) - 1, len(A) - 1))
	p = 0
	for s in range(0, len(minor)):
		if p == i: p = p + 1
		q = 0
		for t in range(0, len(minor)):
			if q == j: q = q + 1
			minor[s][t] = A[p][q]
			q = q + 1
		p = p + 1
	return minor

def encrypt( msg):

	key = [[3, 2, 7], [4, 5, 6], [1, 9, 8]]
	# key = [[3, 2], [4, 5]]
	key = np.transpose(key)
	sz = len(key)

	msg = msg.upper()

	triple = [list(msg[i * sz:(i * sz) + sz]) for i in range(0, int(len(msg) / sz))]
	if debug > 0: print(triple)
	mul = [i[:] for i in triple]
	for x in range(len(triple)):
		for i in range(len(triple[x])):
			triple[x][i] = ord(triple[x][i]) - 65
	if debug > 0: print(triple)
	for x in range(len(triple)):
		mul[x] = np.dot(key, triple[x]) % 26
	if debug > 0: print(mul)
	enc = ""
	for x in range(len(mul)):
		for s in range(0, sz): enc += chr(mul[x][s] + 65)
	return enc

def decrypt( msg):

	key = [[3, 2, 7], [4, 5, 6], [1, 9, 8]]
	key = np.transpose(key)
	sz = len(key)

	try:
		deckey = modMatInv(key, 26)
	except ValueError:
		return
	triple = [list(msg[i * sz:(i * sz) + sz]) for i in range(0, int(len(msg) / sz))]
	mul = [i[:] for i in triple]
	for x in range(len(triple)):
		for i in range(len(triple[x])):
			triple[x][i] = ord(triple[x][i]) - 65
	if debug > 0: print(triple)
	for x in range(len(triple)):
		mul[x] = np.dot(deckey, triple[x]) % 26
	if debug > 0: print(mul)
	dec = ""
	for x in range(len(mul)):
		for s in range(0, sz): dec += chr(int(mul[x][s]) + 65)
	return dec


	