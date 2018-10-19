#!/usr/bin/python3
# -*- coding: utf-8 -*

import sys
sys.path.insert(0, 'lib/')
from cesar import cesar

cryptKey = int(input("Enter cryptKey in integer: "))
sentense = input("Enter sentense: ")


# Display resume
print("\nRESUME:")
print("Your cryptKey is: " + str(cryptKey))
print("Your sentense is: " + sentense)

# Warnup


# Display Cesar encryption
print("\nCesar encryption:")
crypticSentense = cesar.encrypt(sentense, cryptKey)
print("crypticSentense: '" + crypticSentense + "'")

# Display Cesar decryption
print("\nCesar decryption:")
print("decryptSentense: '" + cesar.decrypt(crypticSentense, cryptKey) + "'")
