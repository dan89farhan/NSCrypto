from django.test import TestCase
import string
# Create your tests here.
class PlayFairTestCase(TestCase):
    def test_play_fair_encrypt_message(self):
        message = 'farhan'
        length = len(message)
        if length%2 == 0:
            pairMessage = [ [ [] for i in range(2) ] for j in range(3) ]
            count = 0
            for i in range(len(pairMessage)):
                for j in range(len(pairMessage[0])):
                    print("index i, j {} {}".format(i, j))
                    pairMessage[i][j] = message[count]
                    count +=1
            print("Found something {} ".format( 'a' in pairMessage[0]))    
            print("Pair Message {} ".format(pairMessage))
            
            
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
        # print("Matrix is {} ".format(matrix))
        
        
        return decrypt_message