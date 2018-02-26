#encrypter_decrpyter.py

class Cipher:

	def __init__(self,shift):

		encoder = [None]*26
		decoder = [None]*26

		for k in range(26):
			encoder[k] = chr((k+shift)%26+ord('A'))
			decoder[k] = chr((k-shift)%26+ord('A'))
		self._forward = ''.join(encoder)
		self._backward= ''.join(decoder)



	def encrypt(self,message):

		return self._transform(message,self._forward)

	def decrypt(self,secret):

		return self._transform(secret,self._backward)


	def _transform(self,original,code):


		message = list(original)

		for k in range(len(message)):

			if message[k].isupper():
				j = ord(message[k]) -ord('A')
				message[k]=code[j]
			
		return ''.join(message)


if __name__ == '__main__':
	cipher = Cipher(3)
	message = "THIS HAS TO BE ENCRYPTED"
	coded = cipher.encrypt(message)
	print('Secret:'+coded)
	answer = cipher.decrypt(coded)
	print("Actual:"+answer)

