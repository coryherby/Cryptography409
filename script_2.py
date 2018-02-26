import hashlib
import random
import string
import itertools

possible_chars = string.ascii_letters
n = len(possible_chars)

def countZeroes(str):
	zeroes = 0
	for i in range(len(str)):
		if str[i]=='0':
			zeroes += 1
		else:
			break
	return zeroes

start_string = 'CO409CryptographyEngineeringRunsNowForItsFourthYear'

print(start_string)
print(hashlib.sha256(hashlib.sha256(start_string).digest()).hexdigest())
print()

print(countZeroes(hashlib.sha256(hashlib.sha256(start_string).digest()).hexdigest()))
print(countZeroes('000098873'))
print()

max_starting_zeroes = 0
additional_chars = 1

while max_starting_zeroes < 24:
	add_strings = [''.join(i) for i in itertools.product(possible_chars, repeat = additional_chars)]
	for i in range(len(add_strings)):
		new_string = start_string + add_strings[i]
		new_hash = hashlib.sha256(hashlib.sha256(new_string).digest()).digest()
		zeroes = countZeroes(new_hash)

		if zeroes > max_starting_zeroes:
			print()
			print(new_string)
			print(zeroes)
			print(new_hash)
			max_starting_zeroes = zeroes
	additional_chars += 1
	print()
	print(additional_chars)















