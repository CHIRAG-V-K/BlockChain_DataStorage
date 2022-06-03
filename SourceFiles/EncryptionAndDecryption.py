from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
key = b'\xa5\xa8\xc02\x00\xddI\x9e\xfdmT4\xfc/\xff\x0fE\n\xd5\x96^-\x0cG\xb6<\x9b\x10  \xe7<'
nonce = b'\xa9\x9f\xe7\xeb\xeb\xea\xe4\xeb\x85T\x81M'

chacha = ChaCha20Poly1305(key)

aad = bytes(12345)
##file_Path = "sample.jpg"
##storagePath = file_Path + ".ae"
##file = open(file_Path,'rb')
##data = file.read()
##file.close()
##edata = chacha.encrypt(nonce, data, aad)
##file = open(storagePath,'wb')
##file.write(edata)
##file.close()

file_Path = "sample.jpg.ae"
file = open(file_Path,'rb')
data = file.read()
file.close()
edata = chacha.decrypt(nonce, data, aad)
file = open("sample2.jpg",'wb')
file.write(edata)
file.close()
