class CeaserCipher:
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