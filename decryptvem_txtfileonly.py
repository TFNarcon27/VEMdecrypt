from Crypto.Cipher import AES
from hashlib import sha256
 
key1 = sha256('Let the outcome prove the side.').digest()
data1 = 'nQ3Uz8K5B4ns2e3UOJVHRan9+fKia/bJsoneV9U5TkEnQuN4ZGHJ5t605yos7H8LHQq7g8+9GcNoHT+tgU0B/DP68Q4cB4cnlX/8r2qbPxn0ey9cIBRat5uIxZIVILLntj8='.decode('base64')
 
iv = data1[0:16]
ciphertext = data1[16:]
 
aes = AES.new(key1, AES.MODE_CFB, iv)
print aes.decrypt(ciphertext)
print '\n'


f = open("phraselist.txt","r")

for phrase in f.readlines():
	print ' '+phrase.strip()+':'
	print ''
	key = sha256(phrase.strip()).digest()
	data = 'FzQrKozegTl/0PdIb2vMTC7hn1jZRfAToH4qtgvN2voqnZlVBtUZ+T32eD56lammEDRCg9/eM50OAzsrgEsqJ3ZGH7Kz/AF+wLvgds+B4i8Yf+y1VHYMyoLQu+2un10mDR/A7ms7NKTd6Q=='.decode('base64')
	iv = data[0:16]
	ciphertext = data[16:]
	aes = AES.new(key, AES.MODE_CFB, iv)
	print aes.decrypt(ciphertext)
	print '\n'