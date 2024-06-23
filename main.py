import string

alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
keyedAlphabet = []
cipherText = []


def encrypt(keystream, plaintext):
    for x in range(len(keystream)):
        cipherText.append(alphabet[(alphabet.index(keystream[x]) + alphabet.index(plaintext[x])) % 26])
    print(''.join(cipherText))


def decrypt(keystream, hiddenText):
    for x in range(len(keystream)):
        cipherText.append(alphabet[(alphabet.index(hiddenText[x]) - alphabet.index(keystream[x])) % 26])
    print(''.join(cipherText))


def generateTable(keyWord):
    for x in range(len(keyWord)):
        keyedAlphabet.append(keyWord[-x-1])
        alphabet.insert(0, alphabet.pop(alphabet.index(keyedAlphabet[x])))


def keystreamGen(keyWord, text, mode):
    keystream = []
    for x in range(len(text)):
        if len(keystream) != len(text):
            keystream.append(keyWord[x % 3])

    if mode:
        encrypt(keystream, text)
    else:
        decrypt(keystream, text)


def main():
    if input('Decoding or Encoding? d/e ').lower() == 'e':
        generateTable(input('Enter key: ').upper())
        keystreamGen(input('Enter key word: ').translate(str.maketrans('', '', string.punctuation)).upper(), input('Enter phrase to encrypt: ').replace(' ', '').translate(str.maketrans('', '', string.punctuation)).upper(), True)
    else:
        generateTable(input('Enter key: ').upper())
        keystreamGen(input('Enter key word: ').translate(str.maketrans('', '', string.punctuation)).upper(), input('Enter phrase to decrypt: ').replace(' ', '').translate(str.maketrans('', '', string.punctuation)).upper(), False)


if __name__ == '__main__':
    main()
