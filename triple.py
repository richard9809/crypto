#!/usr/bin/env python
#coding:utf-8

import binascii
import base64
import pyDes
import secrets
import codecs

#IV has to be 8bit long
iv = '2132435465768797'
#Key has to be 24bit long
key = secrets.token_hex(24)
#here is the data you want to encrypt
data = "Jason Grant"

def encrypt(iv, key, data):
    iv = binascii.unhexlify(iv)
    key = binascii.unhexlify(key)
    k = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data)
    d = base64.encodebytes(d)
    return d
    
def decrypt(iv, key, data):
    iv = binascii.unhexlify(iv)
    key = binascii.unhexlify(key)
    k = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    data = base64.decodebytes(data)
    d = k.decrypt(data)
    return d

if __name__ == '__main__':
    print ("Plan Text: %s" % data)
    encryptdata = encrypt(iv, key, data)
    print ("Encrypted Text: %s" % encryptdata)
    decryptdata = decrypt(iv, key, encryptdata)
    print ("Plan Text: %s" % decryptdata)
    print(key)
    print("//////////////////////////////////////////////////////")
    testkey = input("Enter your key")
    testInput = input("Enter ciphertext")
    ciphermessage, _ = codecs.escape_decode(testInput, 'hex')
    print(decrypt(iv, testkey, ciphermessage))
    
    