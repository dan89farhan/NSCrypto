
def playfairEncrypt(message, key):
    print (message_to_digraphs(message))
    print (matrix(key))
    encMessage = encryptPlayFair(key, message)
    print(encMessage)
    return encMessage

def playfairDecrypt(message, key):
    return playFairDecrypt(message, key)

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
    
    message=[]
    for e in message_original:
        message.append(e)

    
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


def playFairDecrypt(cipher, key):	
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
