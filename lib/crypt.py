# -*- coding: utf-8 -*
# This is Cesar library



class cesar:
    def __init__(self):
        pass

    # Encrypt with Cesar algorithm
    def encrypt(sentenseInit, cryptKey):
        sentenseReturn = ""
        for charactere in sentenseInit:
            sentenseReturn += chr(ord(charactere) + cryptKey)
        return sentenseReturn

    # Decrypt with Cesar algorithm
    def decrypt(sentenseInit, cryptKey):
        cryptKey = cryptKey * -1
        sentenseReturn = ""
        for charactere in sentenseInit:
            sentenseReturn += chr(ord(charactere) + cryptKey)
        return sentenseReturn

class reverse:
    def __init__(self):
        pass

    def reverse(sentenseInit):
        sentenseReturn = ""
        for charactere in reversed(sentenseInit):
            sentenseReturn += charactere
        return sentenseReturn
