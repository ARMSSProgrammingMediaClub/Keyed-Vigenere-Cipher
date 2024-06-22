import string

alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
keyedAlphabet = []
VTable = []
cipherX = []
cipherY = []
cipherText = []
spaceSpots = []


def reinsertSpaces(text):
    for x in spaceSpots:
        text.insert(x, ' ')
    return text


def encrypt(keystream, plaintext):
    for x in range(len(keystream)):
        cipherText.append(alphabet[(alphabet.index(keystream[x]) + alphabet.index(plaintext[x])) % 26])
    print(''.join(reinsertSpaces(cipherText)))


def decrypt(keystream, hiddenText):
    for x in range(len(keystream)):
        cipherText.append(alphabet[(alphabet.index(hiddenText[x]) - alphabet.index(keystream[x])) % 26])
    print(''.join(reinsertSpaces(cipherText)))


def generateTable(keyWord):
    for x in range(len(keyWord)):
        keyedAlphabet.append(keyWord[-x-1])
    for x in keyedAlphabet:
        alphabet.index(x)
        alphabet.remove(x)
        alphabet.insert(0, x)
    for x in alphabet:
        VTable.append(alphabet[alphabet.index(x):] + alphabet[:alphabet.index(x)])


def keystreamGen(keyWord, text, mode):
    count = -1
    keystream = []
    for x in range(len(text)):
        if text[x].isalnum() and count < len(keyWord)-1:
            count += 1
            keystream.append(keyWord[count])
        elif text[x].isalnum() and count == len(keyWord)-1:
            count = 0
            keystream.append(keyWord[0])
        elif text[x] == ' ':
            spaceSpots.append(x)
        else:
            count = -1
    if mode:
        encrypt(keystream, text.replace(' ', ''))
    else:
        decrypt(keystream, text.replace(' ', ''))


def main():
    if input('Decoding or Encoding? d/e ').lower() == 'e':
        generateTable(input('Enter key: ').upper())
        keystreamGen(input('Enter key word: ').translate(str.maketrans('', '', string.punctuation)).upper(), input('Enter phrase to encrypt: ').translate(str.maketrans('', '', string.punctuation)).upper(), True)
    else:
        generateTable(input('Enter key: ').upper())
        keystreamGen(input('Enter key word: ').translate(str.maketrans('', '', string.punctuation)).upper(), input('Enter phrase to decrypt: ').translate(str.maketrans('', '', string.punctuation)).upper(), False)


if __name__ == '__main__':
    main()
