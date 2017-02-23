from Crypto.Cipher import AES
from hashlib import sha256
 
x=1
while x != 0:
	print "    Input passphrase for ciphertext #5:"
	print ""
	phrase = raw_input()
	key = sha256(phrase).digest()
	data = 'FzQrKozegTl/0PdIb2vMTC7hn1jZRfAToH4qtgvN2voqnZlVBtUZ+T32eD56lammEDRCg9/eM50OAzsrgEsqJ3ZGH7Kz/AF+wLvgds+B4i8Yf+y1VHYMyoLQu+2un10mDR/A7ms7NKTd6Q=='.decode('base64')
	iv = data[0:16]
	ciphertext = data[16:]
	aes = AES.new(key, AES.MODE_CFB, iv)
	print aes.decrypt(ciphertext)
	print '\n'