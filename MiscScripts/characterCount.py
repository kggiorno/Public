import pprint

def commaCode(xString):
	message = xString
	
	count = {}
	for character in message:
		count.setdefault(character, 0)
		count[character] = count[character] + 1

	pprint.pprint(count)

testString = "Count all my symbols."
print(testString)
commaCode(testString)