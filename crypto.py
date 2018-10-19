#!/usr/bin/python3
# -*- coding: utf-8 -*

import sys
sys.path.insert(0, 'lib/')
from cesar import cesar

cryptKey = 10
sentense = "I'm a computer !"



# Display Cesar encryption
crypticSentense = cesar.encrypt(sentense, cryptKey)
print("crypticSentense: '" + crypticSentense + "'")

# Display Cesar decryption
print("decryptSentense: '" + cesar.decrypt(crypticSentense, cryptKey) + "'")
