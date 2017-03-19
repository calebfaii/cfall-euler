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

encrypted = []  # list of initial int values of cypher -- 1201 characters
encrypted_list = open("p059_cipher.txt")
lines = encrypted_list.read().split(',')
for num in lines:
    encrypted.append(int(num))
print "Cypher values:", encrypted

key_candidates = []  # used a list of three-letter words; failed because they were capitalized
word_list = open("p059_words.txt")
wlines = word_list.read().split(',')
for word in wlines:
    key_candidates.append(word)
# print len(key_candidates)

binary_key_candidates = []  # converted text to 8-bit binary
for item in key_candidates:
    b_list = []
    for character in item:
        b_list.append('{0:08b}'.format(ord(character)))
    binary_key_candidates.append(b_list)


def int_to_binary(numlist):

    ebinary = []
    for nm in numlist:
        ebinary.append('{0:08b}'.format(nm))
    return ebinary


def XOR(byte, key):

    _xormap = {('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0', ('0', '0'): '0'}
    return ''.join([_xormap[a, b] for a, b in zip(byte, key)])


lowercase_list = list(range(97, 123))
# print lowercase_list
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

binary_cypher = int_to_binary(encrypted)
translations = 0
# f = open('out.txt', 'w')
# for key in bcombos:
#     # print "TOTAL TRANSLATIONS: ", translations
#     translation = []
#     counter = 0
#     triplet = 0
#     while counter < 1201:
#         # print counter
#         byte_mod = chr(int(XOR(binary_cypher[counter], key[triplet]), base=2))
#         # print "INT:", binary_cypher[counter]
#         # print "   :", key[triplet]
#         translation.append(byte_mod)
#         # print " "
#         counter += 1
#         triplet += 1
#         if triplet == 3:
#             triplet = 0
#         translations += 1
#         # print "+++++++++++++++++++"
#     print key, "".join(translation)
#     print >> f, key, "".join(translation)
#     # print translation[0][:-10], key,
# f.close()


def run_key():

    b_key = ['01100111', '01101111', '01100100']
    binary_cypher = int_to_binary(encrypted)
    # print len(binary_cypher)
    translation = []
    counter = 0
    triplet = 0
    while counter < 1201:
        # print b_key[triplet]
        byte_mod = int(XOR(binary_cypher[counter], b_key[triplet]), 2)
        translation.append(byte_mod)
        counter += 1
        triplet += 1
        if triplet == 3:
            triplet = 0
    print "Post-XOR:     ", translation
    print " "
    print "Sum:          ", sum(translation)

run_key()
# SOLVED
