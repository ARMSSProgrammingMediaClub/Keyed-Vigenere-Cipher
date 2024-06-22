# Keyed Vigenere Cipher
</body>
The Vigenere Cipher is a type of substitution cipher used for data encryption (think passwords, legal documents, financial records etc.), invented by Blaise De Vigenere in 1586<br />
The Cipher requires a key to encrypt the plaintext, which is then further encrypted through a 26 X 26 table, containing all the letters of the alphabet.<br />

![Vigenere-Square](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/92757287-d116-4157-b004-c2a0aba1b048/Vigenere_square.jpg)<br />

The Vigenere cipher firstly assigns the plaintext a keystream by replacing letters of the plaintext with letters of the keystream<br />

### Plaintext: HELLO WORLD<br />Key: KEY<br />Keystream: KEYKE YKEYK<br />

Then, by using letters from the plaintext and keystream, the cipher finds at which point the letters from the plaintext and keystream intersect and selects that letter as the letter in the encrypted output<br />

![Vigenere-Demo](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/FIG-VIG-Table-EX-M.jpg)

<br />
This Vigenere Cipher differs slightly from the original Vigenere Cipher as this Vigenere Cipher supports a keyed alphabet.

