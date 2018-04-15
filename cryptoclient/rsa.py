
import random


class RSA():


    '''
    Euclid's algorithm for determining the greatest common divisor
    Use iteration to make it faster for larger integers
    '''
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    '''
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers
    '''
    def multiplicative_inverse(self, a, b):
        """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
        """
        # r = gcd(a,b) i = multiplicitive inverse of a mod b
        #      or      j = multiplicitive inverse of b mod a
        # Neg return values for i or j are made positive mod b or a respectively
        
        x = 0
        y = 1
        lx = 1
        ly = 0
        oa = a  # Remember original a/b to remove
        ob = b  # negative values from return results
        while b != 0:
            q = a // b
            (a, b) = (b, a % b)
            (x, lx) = ((lx - (q * x)), x)
            (y, ly) = ((ly - (q * y)), y)
        if lx < 0:
            lx += ob  # If neg wrap modulo orignal b
        if ly < 0:
            ly += oa  # If neg wrap modulo orignal a
        # return a , lx, ly  # Return only positive values
        return lx

    '''
    Tests to see if a number is prime.
    '''
    def is_prime(self, num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for n in range(3, int(num**0.5)+2, 2):
            if num % n == 0:
                return False
        return True

    def generate_keypair(self, p, q):
        if not (self.is_prime(p) and self.is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')
        #n = pq
        n = p * q

        #Phi is the totient of n
        phi = (p-1) * (q-1)

        #Choose an integer e such that e and phi(n) are coprime
        e = random.randrange(1, phi)

        #Use Euclid's Algorithm to verify that e and phi(n) are comprime
        g = self.gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = self.gcd(e, phi)

        #Use Extended Euclid's Algorithm to generate the private key
        d = self.multiplicative_inverse(e, phi)
        
        #Return public and private keypair
        #Public key is (e, n) and private key is (d, n)
        return ((e, n), (d, n))

    def encrypt(self, pk, plaintext):
        
        
        p, q = pk.split(',')
        
        p = int(p)
        q = int(q)

        

        public, private = self.generate_keypair(p, q)
        
        #Unpack the key into it's components
        key, n = private
        print('key, n is ', key, n)
        #Convert each letter in the plaintext to numbers based on the character using a^b mod m
        cipher = [(ord(char) ** key) % n for char in plaintext]
        #Return the array of bytes
        return (cipher, public, private)

    def decrypt(self, pk, n, ciphertext):
        
        key = int(pk)
        n = int(n)
        # ciphertext = int(ciphertext)
        print('ciphertext is ', type(ciphertext))
        # ciphertext = list(map(int, ciphertext))
        # print('ciphertext is ', type(ciphertext) )
        #Generate the plaintext based on the ciphertext and key using a^b mod m
        plain = [chr((int(char) ** key) % n) for char in ciphertext]
        #Return the array of bytes as a string
        return ''.join(plain)
    


'''
Detect if the script is being run directly by the user
'''
# print ("RSA Encrypter/ Decrypter")
# p = int(input("Enter a prime number (17, 19, 23, etc): "))
# q = int(input("Enter another prime number (Not one you entered above): "))
# print ("Generating your public/private keypairs now . . .")
# public, private = generate_keypair(p, q)
# print ("Your public key is ", public ," and your private key is ", private)
# message = input("Enter a message to encrypt with your private key: ")
# encrypted_msg = encrypt(private, message)
# print ("Your encrypted message is: ")
# print (''.join(map(lambda x: str(x), encrypted_msg)))
# print ("Decrypting message with public key ", public ," . . .")
# print ("Your message is:")
# print (decrypt(public, encrypted_msg))