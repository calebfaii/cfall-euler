# Each character on a computer is assigned a unique code and the preferred standard is
# ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65,
# asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR
# each byte with a given value, taken from a secret key. The advantage with the XOR function
# is that using the same encryption key on the cipher text, restores the plain text; for
# example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the
# key is made up of random bytes. The user would keep the encrypted message and the encryption
# key in different locations, and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use
# a password as a key. If the password is shorter than the message, which is likely, the key
# is repeated cyclically throughout the message. The balance for this method is using a sufficiently
# long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters.
# Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted
# ASCII codes, and the knowledge that the plain text must contain common English words, decrypt
# the message and find the sum of the ASCII values in the original text.

import time
import progressbar


def import_cipher():
    print " "
    print "Importing cipher..."
    encrypted = []
    encrypted_list = open("p059_cipher.txt")
    lines = encrypted_list.read().split(',')
    for num in lines:
        encrypted.append(int(num))
    print "Cipher imported successfully."
    print " "
    return encrypted


def int_to_binary(numlist):

    ebinary = []
    for nm in numlist:
        ebinary.append('{0:08b}'.format(nm))
    return ebinary


def XOR(byte, key):

    _xormap = {('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0', ('0', '0'): '0'}
    return ''.join([_xormap[a, b] for a, b in zip(byte, key)])


def explore_encrypted():

    lowercase_list = list(range(97, 123))
    all_combos = []
    for L1 in lowercase_list:
        for L2 in lowercase_list:
            for L3 in lowercase_list:
                triple = [int(L1), int(L2), int(L3)]
                all_combos.append(triple)
    bcombos = []
    for obj in all_combos:
        itb = int_to_binary(obj)
        bcombos.append(itb)
    binary_cypher = int_to_binary(import_cipher())
    print "Translating cipher with %d keys..." % len(bcombos)
    bar = progressbar.ProgressBar(max_value=len(bcombos))
    ticker = 1
    for key in bcombos:
        bar.update(ticker)
        ticker += 1
        translation = []
        counter = 0
        triplet = 0
        while counter < 1201:
            byte_mod = chr(int(XOR(binary_cypher[counter], key[triplet]), base=2))
            translation.append(byte_mod)
            counter += 1
            triplet += 1
            if triplet == 3:
                triplet = 0
        str_trans = ''.join(map(str, translation))
        if 'and ' in str_trans and 'the ' in str_trans:
            print " "
            print " "
            bindata = [str(unichr(int(i, 2))) for i in key]
            print "Logical translation found. Key:", ''.join(bindata)
            return [key, binary_cypher]


def run_key(key_and_cipher):

    b_key = key_and_cipher[0]
    binary_cypher = key_and_cipher[1]
    translation = []
    english_trans = []
    counter = 0
    triplet = 0
    while counter < 1201:
        byte_mod = int(XOR(binary_cypher[counter], b_key[triplet]), 2)
        translation.append(byte_mod)
        english_trans.append(str(unichr(byte_mod)))
        counter += 1
        triplet += 1
        if triplet == 3:
            triplet = 0
    print " "
    print "Translation:  ", ''.join(map(str, english_trans))
    print "Post-XOR:     ", translation
    print "Sum:          ", sum(translation)


start = time.time()
run_key(explore_encrypted())
elapsed = time.time() - start
print " "
print "Total run time:", elapsed, "seconds."
# SOLVED
