from django.test import TestCase
import string
import numpy as np
# Create your tests here.
class PlayFairTestCase(TestCase):
	def test_hill_cipher(self):
			
		# if __name__ == '__main__':
			# 

			# key
			# secret = [[ 8,  6,  9, 5  ],
			# 		[ 6,  9,  5, 10 ],
			# 		[ 5,  8,  4, 9  ],
			# 		[ 10, 6, 11, 4  ]]
			secret = [ [8,9], [10, 5]]
			# plaintext
			text = "hill"

			# Use key (matrix) encryption string
			ciphertext = encrypt(secret, text)

			# Ciphertext
			print(ciphertext)
			
			# Decrypt string
			# print(decrypt(secret, ciphertext))		

# 
# encryption
# 
def encrypt(matrix, words):
	check_param(matrix, words)
	cipher = ''
	length = len(matrix)
	matrix = np.array(matrix)
	words = words.lower()
	arr = [ord(i) - ord('a') for i in words]
	count = 0
	for ch in words:
		if str.isalpha(str(ch)):
			cipher += chr(sum(matrix[count % length] * arr) % 26 + ord('a'))
			count += 1
	return cipher


# 
# Decryption
# 
def decrypt(matrix, words):
	cipher = ''
	length = len(matrix)
	matrix = (np.linalg.inv(matrix) + 26) % 26
	words = words.lower()
	arr = np.array([ord(i) - ord('a') for i in words], dtype=int)
	count = 0
	for ch in words:
		if str.isalpha(str(ch)):
			number = sum(matrix[count % length] * arr) % 26
			cipher += chr(int(str(number)[:-2]) + ord('a'))
			count += 1
	return cipher


# 
# checking
# 
def check_param(matrix, words):
	if len(matrix) * len(matrix) != \
	sum([len(matrix[i]) for i in range(len(matrix))]):
		print("Error: The matrix must be m * m")
		quit()
	elif len(matrix) != len(words):
		print("Error: The length of the plaintext must be m （Equal to the length and width of the matrix")
		quit()
	try:
		np.linalg.inv(matrix)
	except Exception:
		print("Error: Irreversible matrix: " + str(e))
		quit()



