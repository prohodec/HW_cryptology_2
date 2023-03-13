import hill
import playfair

while True:
    choose = input("choose a cipher: \n1 - playfair\n2 - hill\n0 - exit\n:::")

    if choose == "1":
        key = input("enter a key: ")
        word = input("enter a word: ")
        enc_word = playfair.playfair(key, word)
        print("encrypted word:", enc_word)
        key = input("enter a key: ")
        dec_word = playfair.playfair(key, enc_word, False)
        print("decrypted word:", dec_word)
    elif choose == "2":
        word = input("enter a word: ")
        enc_word = hill.encrypt(word)
        print("encrypted word:", enc_word)
        dec_word = hill.decrypt(enc_word)
        print("decrypted word", dec_word)
    elif choose == "0":
        break
