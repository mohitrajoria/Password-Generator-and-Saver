import secrets
import string
import random

'''Generating a n digit random password'''

def GeneratePass(n):
	randomSource = string.ascii_letters + string.digits + string.punctuation
	password = random.choice(string.ascii_lowercase)
	password += random.choice(string.ascii_uppercase)
	password += random.choice(string.digits)
	password += random.choice(string.punctuation)
	for i in range(0,n):
		password += random.choice(randomSource)

	passwordList = list(password)
	random.SystemRandom().shuffle(passwordList)
	password = ''.join(passwordList)
	return password
