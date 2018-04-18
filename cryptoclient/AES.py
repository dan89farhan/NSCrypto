class AES():
    # S-Box
    sBox  = [0x9, 0x4, 0xa, 0xb, 0xd, 0x1, 0x8, 0x5,
            0x6, 0x2, 0x0, 0x3, 0xc, 0xe, 0xf, 0x7]

    # Inverse S-Box
    sBoxI = [0xa, 0x5, 0x9, 0xb, 0x1, 0x7, 0x8, 0xf,
            0x6, 0x0, 0x2, 0x3, 0xc, 0x4, 0xd, 0xe]

    # Round keys: K0 = w0 + w1; K1 = w2 + w3; K2 = w4 + w5
    w = [0] * 6

    def mult(self, p1, p2):
        """Multiply two polynomials in GF(2^4)/x^4 + x + 1"""
        p = 0
        while p2:
            if p2 & 0b1:
                p ^= p1
            p1 <<= 1
            if p1 & 0b10000:
                p1 ^= 0b11
            p2 >>= 1
        return p & 0b1111

    def intToVec(self, n):
        """Convert a 2-byte integer into a 4-element vector"""
        return [n >> 12, (n >> 4) & 0xf, (n >> 8) & 0xf,  n & 0xf]            

    def vecToInt(self, m):
        """Convert a 4-element vector into 2-byte integer"""
        return (m[0] << 12) + (m[2] << 8) + (m[1] << 4) + m[3]

    def addKey(self, s1, s2):
        """Add two keys in GF(2^4)"""  
        return [i ^ j for i, j in zip(s1, s2)]
        
    def sub4NibList(self, sbox, s):
        """Nibble substitution function"""
        return [sbox[e] for e in s]
        
    def shiftRow(self, s):
        """ShiftRow function"""
        return [s[0], s[1], s[3], s[2]]

    def keyExp(self, key):
        """Generate the three round keys"""
        def sub2Nib(b):
            """Swap each nibble and substitute it using sBox"""
            return self.sBox[b >> 4] + (self.sBox[b & 0x0f] << 4)

        Rcon1, Rcon2 = 0b10000000, 0b00110000
        self.w[0] = (key & 0xff00) >> 8
        self.w[1] = key & 0x00ff
        self.w[2] = self.w[0] ^ Rcon1 ^ sub2Nib(self.w[1])
        self.w[3] = self.w[2] ^ self.w[1]
        self.w[4] = self.w[2] ^ Rcon2 ^ sub2Nib(self.w[3])
        self.w[5] = self.w[4] ^ self.w[3]

    def encrypt(self, ptext):
        """Encrypt plaintext block"""
        key = 0b0100101011110101

        self.keyExp(key)
        ptext =int(ptext, base = 2)
        print("new Type is  ", type(ptext))

        print("val is ",ptext)
        def mixCol(s):
            return [s[0] ^ self.mult(4, s[2]), s[1] ^ self.mult(4, s[3]),
                    s[2] ^ self.mult(4, s[0]), s[3] ^ self.mult(4, s[1])]    
        
        state = self.intToVec(((self.w[0] << 8) + self.w[1]) ^ ptext)
        state = mixCol(self.shiftRow(self.sub4NibList(self.sBox, state)))
        state = self.addKey(self.intToVec((self.w[2] << 8) + self.w[3]), state)
        state = self.shiftRow(self.sub4NibList(self.sBox, state))
        return self.vecToInt(self.addKey(self.intToVec((self.w[4] << 8) + self.w[5]), state))
        
    def decrypt(self, ctext):
        """Decrypt ciphertext block"""

        key = 0b0100101011110101
        print("Before transformation Key is ", key)

        self.keyExp(key)

        ctext =int(ctext, base = 2)


        def iMixCol(s):
            return [self.mult(9, s[0]) ^ self.mult(2, s[2]), self.mult(9, s[1]) ^ self.mult(2, s[3]),
                    self.mult(9, s[2]) ^ self.mult(2, s[0]), self.mult(9, s[3]) ^ self.mult(2, s[1])]
        
        state = self.intToVec(((self.w[4] << 8) + self.w[5]) ^ ctext)
        state = self.sub4NibList(self.sBoxI, self.shiftRow(state))
        state = iMixCol(self.addKey(self.intToVec((self.w[2] << 8) + self.w[3]), state))
        state = self.sub4NibList(self.sBoxI, self.shiftRow(state))
        return self.vecToInt(self.addKey(self.intToVec((self.w[0] << 8) + self.w[1]), state))
