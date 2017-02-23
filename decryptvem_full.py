# Decrypt VEM codes, some information here:
# https://www.reddit.com/r/TheFamiliar/comments/5vel7q/cracking_some_literal_codes_tf04_spoilers/
# Built by /u/ellimist and /u/dradzanglor
# make executable: pyinstaller.exe --onefile decryptvem_full.py

print "\nMark Z. Danielewski's The Familiar Volume 4 AES-encrypted codes\n"
print "If using a passphrase list file, create a .txt file in this directory"
print "titled phraselist.txt with *one passphrase per line*"
x = 1
while x == 1:
	from Crypto.Cipher import AES
	from hashlib import sha256

	cipher = ['DiOOSN7FuA7IXRUBlGzC2q/eB8vNndyrIYLlsTGcfIjx9dN5FubhV3NwtJVIEkDYPJ7AU/443bfwbb9xzcFiAKOhqB5XQFM+l3zU9/ztPGmMDtK1oydWEQiwjMUmWBgYy8BatpWch7dutGRgAS0KKUxID2G0N8sB0tGhZQHl', 'E/D01z1gQBPWACDsP0eR752re3HAxsNWLcnLXa9Mj9vt050WcaBTs0UUiyVF+oUCydUBM3zusDR+dtJ0B0ONxIL2rAzYQ8OA//oQq2lLtzgdz+FuqTzHqZQCQzRsA4RrqVEqO3GE9lu0loKWJg==', 'dALUKK7nUm91W2y5zjEjJOXZ57pjtHusb3S8tStLT7cuXu+KNHw57AXFJt940SqOewI6rCPXoDx1Mn9qTXTnxEpw6Vc+GkDwA3eeCNsumqVlGG69q1PJoDnKOg7VvpMc', 'nQ3Uz8K5B4ns2e3UOJVHRan9+fKia/bJsoneV9U5TkEnQuN4ZGHJ5t605yos7H8LHQq7g8+9GcNoHT+tgU0B/DP68Q4cB4cnlX/8r2qbPxn0ey9cIBRat5uIxZIVILLntj8=','FzQrKozegTl/0PdIb2vMTC7hn1jZRfAToH4qtgvN2voqnZlVBtUZ+T32eD56lammEDRCg9/eM50OAzsrgEsqJ3ZGH7Kz/AF+wLvgds+B4i8Yf+y1VHYMyoLQu+2un10mDR/A7ms7NKTd6Q==']

	print "\n    1: "+cipher[0]+ "\n"
	print "    2: "+cipher[1]+"\n"
	print "    3: "+cipher[2]+"\n"
	print "    4: "+cipher[3]+"\n"
	print "    5: "+cipher[4]+"\n"
	print "    6: Enter a cipher\n"

	print "    Which cipher?"
	ciphernum = raw_input()
	ciphernum = int(ciphernum)-1

	if ciphernum == 5:
		print "    Enter cipher:"
		cipherpick = raw_input()
	else:
		cipherpick = cipher[ciphernum]

	aa = r"/n)"
	print "\n    Use a passphrase list text file? (y"+aa
	listq = raw_input()
	
	if 'Y' in listq or 'y' in listq:
		f = open("phraselist.txt","r")
		for phrase in f.readlines():
			print ' '+phrase.strip()+':'
			print ''
			print ''
			key = sha256(phrase.strip()).digest()
			data = cipherpick.decode('base64')
			iv = data[0:16]
			ciphertext = data[16:]
			aes = AES.new(key, AES.MODE_CFB, iv)
			print aes.decrypt(ciphertext)
			print '\n'
	else:
		print "\n    The four known passphrases: 1. VEM, 2. esse quam videri, 3. sipaapuni, 4. Let the outcome prove the side"
		print "\n    Enter a passphrase:"
		passphrase = raw_input()
		print ''
		key = sha256(passphrase).digest()
		data = cipherpick.decode('base64')
		iv = data[0:16]
		ciphertext = data[16:]
		aes = AES.new(key, AES.MODE_CFB, iv)
		print aes.decrypt(ciphertext)

	print "\n Run again? (y" + aa
	restart = raw_input()

	if 'Y' in restart or 'y' in restart:
		x=1
	else:
		x=0