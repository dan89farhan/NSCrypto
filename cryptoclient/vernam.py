class Vernam:

    def makeVernamCypher(self, text, key):
        """ Returns the Vernam Cypher for given string and key """
        answer = ""  # the Cypher text
        p = 0  # pointer for the key
        for char in text:
            answer += chr(ord(char) ^ ord(key[p]))
            p += 1
            if p == len(key):
                p = 0
        return answer

    def encrypt(self, msg):
        key = "cvwopslweinedvq9fnasdlkfn2"
        return self.makeVernamCypher(msg,key)

    def decrypt(self, msg):
        key = "cvwopslweinedvq9fnasdlkfn2"
        return self.makeVernamCypher(msg,key)
