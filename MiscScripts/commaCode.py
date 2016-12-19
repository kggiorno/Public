def commaCode(xList):
	listLength = len(xList)
	replacementString = ''
	i = 0
	while i < (listLength-1):
		replacementString = replacementString + str(xList[i])
		replacementString = replacementString + ', '
		i += 1
	replacementString = replacementString + 'and '
	replacementString = replacementString + str(xList[listLength-1])
	print(replacementString)

testList = ["cats", "dogs", "women", "men", "rain"]
print(testList)
commaCode(testList)